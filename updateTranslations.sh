#!/bin/sh

LANGS="
	es_ES
	ca_ES
	eu_ES
	gl_ES
"
ln -sf envote envote.py
for lang in $LANGS
do
	pylupdate4 envote.py envotelib/*py -ts i18n/envote_$lang.ts 
done
rm envote.py
lrelease i18n/*.ts

