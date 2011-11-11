#!/bin/bash

# This scripts is a unix/linux scripts that builds the windows binaries
# Requires wine installed
# Requires windows versions (installed on wine) of python27, pyqt and cx_freeze

set -e

version=$(cat VERSION)
WINE_DRIVE_C=~/.wine/drive_c
PYTHON_PREFIX=$WINE_DRIVE_C/Python27
PYTHON_DLL=$WINE_DRIVE_C/windows/system32/python27.dll

$PYTHON_PREFIX/python.exe $PYTHON_PREFIX/Scripts/cxfreeze  envote --target-dir envote-$version-win32
cp -vr data cookedData envote-$version-win32/
cp -v $PYTHON_DLL README COPYING TODO VERSION envote-$version-win32/
for dll in QtCore4 QtGui4
do
	cp -v $PYTHON_PREFIX/Lib/site-packages/PyQt4/$dll.dll envote-$version-win32/
done
zip -r envote-$version-win32.zip envote-$version-win32/


