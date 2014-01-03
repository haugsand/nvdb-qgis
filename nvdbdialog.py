# -*- coding: utf-8 -*-
"""
/***************************************************************************
 NvdbDialog
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

from PyQt4 import QtCore, QtGui
from ui_nvdb import Ui_Nvdb
# create the dialog for zoom to point


class NvdbDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_Nvdb()
        self.ui.setupUi(self)
        
