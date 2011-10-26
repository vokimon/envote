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
	

print resultadosGeneralesBarcelona2004


class Simulador(object) :

	def __init__(
			self,
			representantes,
			abstenciones,
			blancos,
			nulos,
			umbral = 30,
			** votacions
			) :
		self._votacions = dict(votacions)
		self._votacions.update(
			blancos = blancos,
			abstenciones = abstenciones,
			nulos = nulos,
			)

	def opciones(self) :
		return self._votacions.keys()

	def partidos(self) :
		return [
			p for p in self.opciones()
			if p not in [
				'abstenciones',
				'blancos',
				'nulos',
				]
			]
	def votosValidos(self) :
		return sum((
			votos 
			for partido, votos in self._votacions.iteritems()
			if partido not in [
				'abstenciones',
				'nulos',
				]
			))
	def reparto(self, representants) :
		numeros = sum([
			[
				(votos/(i+1), partido)
				for i in xrange(representants)
			]
			for partido, votos in self._votacions.iteritems()
			if partido not in [
				'abstenciones',
				'nulos',
				'blancos',
				]
		],[])[:representants]

import unittest

prova1 = dict(
	abstenciones = 2000,
	blancos = 500,
	nulos = 100,
	partido1 = 1000,
	partido2 = 1100,
	partido3 = 800,
	partido4 = 900,
	partido5 = 200,
	)

class SimuladorTest(unittest.TestCase) :
	def test_partidos(self) :
		s = Simulador(representantes=31, **prova1)
		self.assertEquals(
			[
				'partido1',
				'partido2',
				'partido3',
				'partido4',
				'partido5',
			],
			sorted(s.partidos()))

	def test_opciones(self) :
		s = Simulador(representantes=31, **prova1)
		self.assertEquals(
			sorted(prova1.keys()),
			sorted(s.opciones()))

	def test_votosValidos(self) :
		s = Simulador(representantes=31, **prova1)
		self.assertEquals(
			4500,
			s.votosValidos())

	def test_reparto(self) :
		s = Simulador(representantes=31, **prova1)
		self.assertEquals(
			dict(),
			s.reparto(31))





if __name__ == "__main__" :
	unittest.main()



