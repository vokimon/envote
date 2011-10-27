#!/usr/bin/env python

class Resultats(object) :
	__slots__ = [
		'vots',
		'scons',
		'percents',
		'representants',
		]
	def __init__(self, afile) :
		data = [
			(nom, vots, percent, scons)
			for nom, vots, percent, scons,
			in (
				line.strip().split('\t')
				for line in afile
				)
			if vots!='-'
			]
		self.vots = dict((
			(nom, int(vots))
			for nom, vots, percent, scons in data))
		self.percents = dict((
			(nom, float(percent) if percent!='-' else 0)
			for nom, vots, percent, scons in data))
		self.scons = dict(( 
			(nom, int(scons) if scons!='-' else 0)
			for nom, vots, percent, scons in data))
		self.representants = self.scons['participacion']
		assert sum(self.vots.values()) == 2*self.vots['participacion'] + self.vots['abstenciones']
		del self.vots['participacion']
		del self.percents['participacion']
		del self.scons['participacion']
		del self.scons['abstenciones']
		del self.scons['blancos']
		del self.scons['nulos']



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
	def repartiment(self, representants) :
		numeros = sorted(sum((
			[
				(self._votacions[partido]/(i+1), partido)
				for i in xrange(representants)
			]
			for partido in self.partidos()
		),[]))
		numeros.reverse()
		numeros = numeros[:representants]
		import collections
		counter = collections.Counter((partit for num, partit in numeros))
		return dict((
			(partit, counter[partit]) 
			for partit in self.partidos()))

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

	def test_repartiment_parlamentoBarcelona2000(self) :
		case = Resultats(file("parlamentoBarcelona2000.csv"))
		s = Simulador(case.representants, **case.vots)
		self.assertEquals(
			case.scons,
			s.repartiment(case.representants))

	def test_repartiment_parlamentoBarcelona2004(self) :
		case = Resultats(file("parlamentoBarcelona2004.csv"))
		s = Simulador(case.representants, **case.vots)
		self.assertEquals(
			case.scons,
			s.repartiment(case.representants))

	def test_repartiment_parlamentoBarcelona2008(self) :
		case = Resultats(file("parlamentoBarcelona2008.csv"))
		s = Simulador(case.representants, **case.vots)
		self.assertEquals(
			case.scons,
			s.repartiment(case.representants))




if __name__ == "__main__" :
	unittest.main()



