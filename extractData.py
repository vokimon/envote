#!/usr/bin/env python

(
	resultadosGeneralesBarcelona2008,
	resultadosGeneralesBarcelona2004,
	resultadosGeneralesBarcelona2000,
) = zip(*[
	(
		(nom, votacions2008, percent2008, escanos2008),
		(nom, votacions2004, percent2004, escanos2004),
		(nom, votacions2000, percent2000, escanos2000),
	)
	for nom, votacions2008, percent2008, escanos2008,
		_,   votacions2004, percent2004, escanos2004,
		_,   votacions2000, percent2000, escanos2000,
	in [
		line.strip().split('\t')
		for line in file("generals.csv")
		]
	])

for year, data in [
	(2000, resultadosGeneralesBarcelona2000),
	(2004, resultadosGeneralesBarcelona2004),
	(2008, resultadosGeneralesBarcelona2008),
	] :
	f = open("parlamentoBarcelona%s.csv"%year, "w")
	for partido, votaciones, percent, escanos in data :
		print >> f, '\t'.join([partido, votaciones, percent, escanos])
	

