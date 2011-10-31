#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright 2011 David García Garzón

This file is part of enVote

enVote is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

enVote is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class Resultats(object) :
	__slots__ = [
		'vots',
		'scons',
		'representants',
		'descripcions',
		'votsValids',
		]
	def __init__(self, afile) :
		tabSeparated = [line.split('\t') for line in afile]
		for i, line in enumerate(tabSeparated) :
			assert len(line) == 4, "line"

		data = [
			(
				nom,
				int(vots) if vots else 0,
				int(scons) if scons else 0,
				descripcions.strip())
			for nom, vots, scons, descripcions
			in tabSeparated[1:]
			]
		self.vots = dict((
			(nom, int(vots) if vots else 0)
			for nom, vots, scons, descripcions in data))
		self.scons = dict(( 
			(nom, int(scons) if scons else 0)
			for nom, vots, scons, descripcions in data))

		self.representants = self.scons['censo']
		totalCensats = self.vots['censo']
		participacio = self.vots['participacion']

		del self.vots['censo']
		del self.vots['participacion']
		del self.scons['censo']
		del self.scons['participacion']
		del self.scons['abstencion']
		del self.scons['blancos']
		del self.scons['nulos']

		assert totalCensats == participacio + self.vots['abstencion']
		assert participacio == sum((
			vots for partit, vots in self.vots.iteritems()
			if partit != 'abstencion' ))

		sconsRepartits = sum(self.scons.itervalues())
		assert sconsRepartits == 0 or sconsRepartits == self.representants
		self.votsValids = participacio - self.vots['nulos']


class Simulador(object) :

	def __init__(
			self,
			representantes,
			abstencion,
			blancos,
			nulos,
			umbral = 30,
			** votacions
			) :
		self._votacions = dict(votacions)
		self._votacions.update(
			blancos = blancos,
			abstencion = abstencion,
			nulos = nulos,
			)

	def opciones(self) :
		return self._votacions.keys()

	def partidos(self) :
		return [
			p for p in self.opciones()
			if p not in [
				'abstencion',
				'blancos',
				'nulos',
				]
			]
	def votosValidos(self) :
		return sum((
			votos 
			for partido, votos in self._votacions.iteritems()
			if partido not in [
				'abstencion',
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
import glob


prova1 = dict(
	abstencion = 2000,
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

	def test_repartiment_cassosReals(self) :
		for dataFile in glob.glob("data/congresoBarcelona-2011*csv") :
			print dataFile
			case = Resultats(file(dataFile))
			s = Simulador(case.representants, **case.vots)
			self.assertEquals(
				case.scons,
				s.repartiment(case.representants))

	def test_repartiment_cassosReals(self) :
		for dataFile in glob.glob("data/congresoBarcelona-????-??.csv") :
			print dataFile
			case = Resultats(file(dataFile))
			s = Simulador(case.representants, **case.vots)
			self.assertEquals(
				case.scons,
				s.repartiment(case.representants))

	def test_repartiment_parlamentoBarcelona2000(self) :
		case = Resultats(file("data/congresoBarcelona-2000-03.csv"))
		s = Simulador(case.representants, **case.vots)
		self.assertEquals(
			case.scons,
			s.repartiment(case.representants))

	def _test_repartiment_parlamentoBarcelona2000(self) :
		case = Resultats(file("parlamentoBarcelona2000.csv"))
		s = Simulador(case.representants, **case.vots)
		self.assertEquals(
			case.scons,
			s.repartiment(case.representants))

	def _test_repartiment_parlamentoBarcelona2004(self) :
		case = Resultats(file("parlamentoBarcelona2004.csv"))
		s = Simulador(case.representants, **case.vots)
		self.assertEquals(
			case.scons,
			s.repartiment(case.representants))

	def _test_repartiment_parlamentoBarcelona2008(self) :
		case = Resultats(file("parlamentoBarcelona2008.csv"))
		s = Simulador(case.representants, **case.vots)
		self.assertEquals(
			case.scons,
			s.repartiment(case.representants))




if __name__ == "__main__" :
	unittest.main()



