#!/bin/sh

version=0.1

~/.wine/drive_c/Python27/python.exe /home/vokimon/.wine/drive_c/Scripts/cxfreeze  envote --target-dir envote-$version
cp -r data envote-$version/
zip -r envote-$version.zip envote-$version/


