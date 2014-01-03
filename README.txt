Plugin Builder Results



Your plugin Nvdb was created in:

    C:\Users\Magnus Haugsand\.qgis2\python\plugins\Nvdb



Your QGIS plugin directory is located at:

    C:/Users/Magnus Haugsand/.qgis2/python/plugins



What's Next:


  * Copy the entire directory containing your new plugin to the QGIS plugin directory


  * Compile the ui file using pyuic4


         pyuic4 ui_nvdb.ui > ui_nvdb.py
  * Compile the resources file using pyrcc4


         pyrcc4 resources.qrc > resources.py
  * Test the plugin by enabling it in the QGIS plugin manager


  * Customize it by editing the implementation file:

         nvdb.py


  * Create your own custom icon, replacing the default icon.png


  * Modify your user interface by opening nvdb.ui
 in Qt Designer (don't forget to compile it with pyuic4 after changing it)


  * You can use the Makefile to compile your Ui and resource files when
 you make changes. This requires GNU make (gmake)



For more information, see the PyQGIS Developer Cookbook at:

http://www.qgis.org/pyqgis-cookbook/index.html



(C) 2013 GeoApt LLC - geoapt.com
