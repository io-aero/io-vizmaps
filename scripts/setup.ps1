#This script sets up the enviornment required to run with QGIS
#Set these user variables here.
$OSGEO4W_ROOT="C:\OSGeo4W64"
$QGISNAME="qgis"
$QGIS="$OSGEO4W_ROOT\apps\$QGISNAME"
$QGIS_PREFIX_PATH=$QGIS
#$PYCHARM="C:\PyCharm\bin\pycharm64.exe"

$env:Path = "$OSGEO4W_ROOT\bin;$env:Windir\system32;$env:Windir;$env:Windir\system32\WBem"
$env:GDAL_DATA="$OSGEO4W_ROOT%\share\gdal"
$env:GDAL_DRIVER_PATH="$OSGEO4W_ROOT\bin\gdalplugins"
$env:GEOTIFF_CSV="$OSGEO4W_ROOT\share\epsg_csv"
$env:JPEGMEM=1000000
#$env:PROJ_LIB="C:\Program Files\GDAL\projlib"
$env:PROJ_LIB="$OSGEO4W_ROOT\share\proj"
#$env:Path += ";$env:PROJ_LIB"
#CALL %OSGEO4W_ROOT%\bin\o4w_env.bat

$env:PYTHONHOME = "$OSGEO4W_ROOT\apps\Python37"
$env:PYTHONPATH = $env:PYTHONPATH + ";$env:PYTHONHOME" + ";$env:PYTHONHOME\Scripts"
$env:Path += ";$env:PYTHONPATH"
#CALL %OSGEO4W_ROOT%\bin\py3_env.bat
$env:Path = "$OSGEO4W_ROOT\apps\qt5\bin;" + $env:Path

$env:QT_PLUGIN_PATH="$OSGEO4W_ROOT\apps\Qt5\plugins"
$env:QT_QPA_PLATFORM_PLUGIN_PATH=$env:qt_plugin_path

$env:O4W_QT_PREFIX="$OSGEO4W_ROOT/apps/Qt5"
$env:O4W_QT_BINARIES="$OSGEO4W_ROOT/apps/Qt5/bin"
$env:O4W_QT_PLUGINS="$OSGEO4W_ROOT/apps/Qt5/plugins"
$env:O4W_QT_LIBRARIES="$OSGEO4W_ROOT/apps/Qt5/lib"
$env:O4W_QT_TRANSLATIONS="$OSGEO4W_ROOT/apps/Qt5/translations"
$env:O4W_QT_HEADERS="$OSGEO4W_ROOT/apps/Qt5/include"
$env:O4W_QT_DOC="$OSGEO4W_ROOT/apps/Qt5/doc"
#CALL %OSGEO4W_ROOT%\bin\qt5_env.bat
$env:GRASS_PROJSHARE="$OSGEO4W_ROOT\share\proj"
#CALL %OSGEO4W_ROOT%\apps\grass\grass78\etc\env.bat

$env:Path += ";$QGIS/bid"
$env:PATH += ";$OSGEO4W_ROOT\apps\QT5\bin"
$env:PATH += ";$OSGEO4W_ROOT\apps\Python37\Scripts"
$env:PATH += ";$OSGEO4W_ROOT\apps\Python37\lib"
$env:PATH += ";C:\Program Files\GDAL"
$env:PATH += ";C:\Program Files\GDAL\gdalplugins"
echo "PATH=$PATH"
$env:PYTHONPATH = "$QGIS\python;" + $env:PYTHONPATH
$env:PYTHONPATH += ";$OSGEO4W_ROOT\apps\Python37\lib\site-packages"

echo "PYTHONPATH=$PYTHONPATH"
echo "PYTHONHOME=$PYTHONHOME"
#start "PyCharm aware of QGIS" /B %PYCHARM% %*