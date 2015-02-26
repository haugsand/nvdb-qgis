# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Nvdb
                                 A QGIS plugin
 NVDB REST API Plugin
                              -------------------
        begin                : 2013-12-28
        copyright            : (C) 2013 by Magnus Haugsand
        email                : haugsand@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

import resources
from nvdbdialog import NvdbDialog

import os.path

import requests
import json

class Nvdb:

    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'nvdb_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        self.dlg = NvdbDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/nvdb/icon.png"),
            u"NVDB Plugin", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&NVDB Plugin", self.action)
        
        # Startverdier
        self.objekttype = 0
        self.fylke = 0
        self.kommune = 0
        
        self.init_objekttyper()
        self.init_omrader()
        
        # Legg til actions
        self.dlg.ui.comboBoxObjekttype.currentIndexChanged[str].connect(self.velg_objekttype)
        self.dlg.ui.comboBoxFylke.currentIndexChanged[str].connect(self.velg_fylke)
        self.dlg.ui.comboBoxKommune.currentIndexChanged[str].connect(self.velg_kommune)
        self.dlg.ui.pushButton.clicked.connect(self.leggtil_lag)


    def velg_objekttype(self, navn):
        # Setter aktiv objekttypeid
        
        if navn == 'Vegnett':
            self.objekttype = 0
        else:
            self.objekttype = self.objekttyper[navn]

    def velg_fylke(self, navn):
        # Setter aktivt fylkesnummer og oppretter tilhørende kommuneliste
    
        if navn == 'Hele Norge':
            self.fylke = 0
            self.dlg.ui.comboBoxKommune.clear()
            self.dlg.ui.comboBoxKommune.addItem('Velg fylke')
        else: 
            self.fylke = self.fylker[navn]
            self.dlg.ui.comboBoxKommune.clear()
            self.dlg.ui.comboBoxKommune.addItem('Hele fylket')
            
            for kommune in sorted(self.kommuner[self.fylke]):
                self.dlg.ui.comboBoxKommune.addItem(kommune)

    def velg_kommune(self, navn):
        # Setter aktivt kommunenummer
        
        if navn == 'Hele fylket' or navn == 'Velg fylke' or navn == '':
            self.kommune = 0
        else:
            self.kommune = self.kommuner[self.fylke][navn]
            

    def leggtil_lag(self):
        # Legger til nytt vektorlag
    
        vegkategorier = []
        if self.dlg.ui.E.isChecked():
            vegkategorier.append('E')
        if self.dlg.ui.R.isChecked():
            vegkategorier.append('R')
        if self.dlg.ui.F.isChecked():
            vegkategorier.append('F')
        if self.dlg.ui.K.isChecked():
            vegkategorier.append('K')
        if self.dlg.ui.P.isChecked():
            vegkategorier.append('P')
        if self.dlg.ui.S.isChecked():
            vegkategorier.append('S')
            
        if not vegkategorier:
            print 'Ingen vegkategorier valgt'
            return
        vegkategori = ''.join(vegkategorier)
        
        navn = 'Norge'    
        if self.fylke != 0:
            navn = self.dlg.ui.comboBoxFylke.itemText(self.dlg.ui.comboBoxFylke.currentIndex())
            if self.kommune != 0:
                navn = self.dlg.ui.comboBoxKommune.itemText(self.dlg.ui.comboBoxKommune.currentIndex())
        navn += ' ('+vegkategori+')'

        if self.objekttype != 0:
            navn = self.dlg.ui.comboBoxObjekttype.itemText(self.dlg.ui.comboBoxObjekttype.currentIndex())+' '+navn
            
            sokobjekt = {}
            sokobjekt['objektTyper'] = [{
                'id': self.objekttype, 
                'antall': 20000, 
                'filter': [{
                    'type': 'vegreferanse',
                    'operator': '=',
                    'verdi': vegkategorier
                }]
            }]

            if self.fylke != 0:
                sokobjekt['lokasjon'] = {}
                if self.kommune != 0:
                    kommune = self.fylke*100 + self.kommune
                    sokobjekt['lokasjon']['kommune'] = [kommune]
                else:
                    sokobjekt['lokasjon']['fylke'] = [self.fylke]
            
            sok = query('/sok', {'kriterie': json.dumps(sokobjekt)})
            objekter = sok['resultater'][0]['vegObjekter']
            
            self.init_geojson()
            for objekt in objekter:
                self.leggtil_geojson(objekt)
            
            data = json.dumps(self.geojson)
            
        else:
            navn = 'Vegnett '+navn
            
            sted = ''
            if self.fylke != 0:
                sted += '/'+str(self.fylke)
                if self.kommune != 0:
                    sted += '/'+str(self.kommune)
            
            path = '/vegnett'+sted+'.json?kategori='+vegkategori          
            vegnett = query(path)
            data = json.dumps(vegnett)
            

        # Registrerer lag i QGIS
        lag = QgsVectorLayer(data, navn, 'ogr')
        QgsMapLayerRegistry.instance().addMapLayer(lag)


    def init_objekttyper(self):
        self.objekttyper = {}
  
        objekttyper = query("/datakatalog/objekttyper")
        for objekttype in objekttyper['vegObjektTyper']:
            self.objekttyper[objekttype['navn']] = objekttype['id']
        for objekttype in sorted(self.objekttyper):
            self.dlg.ui.comboBoxObjekttype.addItem(objekttype)


    def init_omrader(self):
        self.fylker = {}
        
        fylker = query("/omrader/fylker")
        for fylke in fylker['fylker']:
            self.dlg.ui.comboBoxFylke.addItem(fylke['navn'])
            self.fylker[fylke['navn']] = fylke['nummer']
        
        self.kommuner = {}
        for tall in range(1, 21):
            self.kommuner[tall] = {}
        
        kommuner = query("/omrader/kommuner")
        for kommune in kommuner['kommuner']:
            if kommune['nummer'] < 1000:
                fylkesnr = int(str(kommune['nummer'])[:1])
                kommunenr = int(str(kommune['nummer'])[1:])
            else: 
                fylkesnr = int(str(kommune['nummer'])[:2])
                kommunenr = int(str(kommune['nummer'])[2:])
            
            self.kommuner[fylkesnr][kommune['navn']] = kommunenr
            
    def init_geojson(self):
    
        self.geojson = {}
        self.geojson['type'] = 'FeatureCollection'
        self.geojson['crs'] = {}
        self.geojson['crs']['type'] = 'name'
        self.geojson['crs']['properties'] = {}
        self.geojson['crs']['properties']['name'] = 'urn:ogc:def:crs:EPSG::32633'
        self.geojson['features'] = []

    def leggtil_geojson(self, objekt):
        rad = {}
        rad['type'] = 'Feature'
        rad['geometry'] = {}
        rad['geometry']['coordinates'] = []
        
        try:
            geometri = objekt['lokasjon']['geometriUtm33']
        except KeyError:
            pass
        else: 
            if 'MULTILINESTRING' in geometri:
                rad['geometry']['type'] = 'MultiLineString'          
                koordinatsett = geometri.strip('MULTILINESTRING ()')
                koordinatsett = koordinatsett.split('), (')
                for koordinater in koordinatsett:
                    koordinatrad = []
                    koordinater = koordinater.split(', ')
                    for koordinat_x in koordinater:
                        koordinater_y = koordinat_x.split(' ')
                        koordinat = []
                        for koordinat_y in koordinater_y:
                            koordinat.append(float(koordinat_y))
                        koordinatrad.append(koordinat)
                    rad['geometry']['coordinates'].append(koordinatrad)

            elif 'LINESTRING' in geometri:
                rad['geometry']['type'] = 'LineString'
                koordinater = geometri.strip('LINESTRING ()')
                koordinater = koordinater.split(', ')
                for koordinat_x in koordinater:
                    koordinater_y = koordinat_x.split(' ')
                    koordinat = []
                    for koordinat_y in koordinater_y:
                        koordinat.append(float(koordinat_y))
                    rad['geometry']['coordinates'].append(koordinat)

            elif 'POINT' in geometri:
                rad['geometry']['type'] = 'Point'
                koordinater = geometri.strip('POINT ()')
                koordinater = koordinater.split(' ')
                for koordinat in koordinater:
                    rad['geometry']['coordinates'].append(float(koordinat))
             
        rad['properties'] = {}
        try: 
            for egenskap in objekt['egenskaper']:
                rad['properties'][egenskap['navn']] = egenskap['verdi']
        except KeyError:
            pass
        
        rad['properties']['Objektid'] = objekt['objektId']
        
        try:
            rad['properties']['Strekningslengde'] = objekt['strekningslengde']
        except KeyError:
            pass
            
        self.geojson['features'].append(rad)
               
        
        
    def unload(self):
        self.iface.removePluginMenu(u"&NVDB Plugin", self.action)
        self.iface.removeToolBarIcon(self.action)


    def run(self):
        self.dlg.show()
        result = self.dlg.exec_()
        if result == 1:
            pass
            

def query(path, params=''):
    """Leverer data fra NVDB APIet på JSON-format:
    https://www.vegvesen.no/nvdb/api/
    
    Argumenter:
    path -- Sti bak adresse til NVDB API
    params -- Parametere (default: '')
    
    """
    
    api = 'https://www.vegvesen.no/nvdb/api'
    
    url = api+path
    headers = {'accept': 'application/vnd.vegvesen.nvdb-v1+json'}
    
    r = requests.get(url, headers=headers, params=params, verify=False)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        raise Exception('Feil ved henting av '+r.url+': '+str(r.status_code))
        
        

            