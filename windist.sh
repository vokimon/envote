#!/bin/sh

# This scripts is a unix/linux scripts that builds the windows binaries
# Requires wine
# Requires windows versions (installed on wine) of python27, pyqt and cxfreeze


version=0.1

~/.wine/drive_c/Python27/python.exe /home/vokimon/.wine/drive_c/Scripts/cxfreeze  envote --target-dir envote-$version
cp -r data envote-$version/
zip -r envote-$version.zip envote-$version/


