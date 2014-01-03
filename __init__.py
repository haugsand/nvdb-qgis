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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load Nvdb class from file Nvdb
    from nvdb import Nvdb
    return Nvdb(iface)
