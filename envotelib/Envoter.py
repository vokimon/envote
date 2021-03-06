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

import Simulador as Simulador
from HondtTable import HondtTable
from PieChart import PieChart

from PyQt4 import QtGui, QtCore

import os
import glob

threshold = .03


class Envoter(QtGui.QDialog) :
	def __init__(self, dataPath, version) :
		QtGui.QDialog.__init__(self)
		self.setWindowTitle(self.tr("enVote %1 - Votation simulator").arg(version))
		self._dataPath = dataPath
		files = sorted(glob.glob(self.dataPath("*")))
		if not files :
			QtGui.QMessageBox.critical(self,
				self.tr("Error loading data"),
				self.tr("The application is unable to find out the data set"))
			raise RuntimeError("The application is unable to find the data set")

		self.cases = sorted([
			(os.path.splitext(os.path.basename(name))[0], Simulador.Resultats(file(name)))
			for name in files
			])
	
		self.currentCase = 0
		self.case = None

		colors = dict(
			abstencion="darkgrey",
			blancos="white",
			nulos="#F44",
			CiU="blue",
			CIU="blue",
			PP="cyan",
			ERC="orange",
			ESQUERRA="orange",
			** {
			"PSOE" : "red",
			"PSC" : "red",
			"PSC-PSOE" : "red",
			"ICV-EUiA" : "green",
			"IC-V" : "green",
			"IC" : "green",
			"IC-EV" : "green",
			"IU" : "green",
			"PSUC" : "green",
			"PSUC-PCE" : "green",
			})

		layout = QtGui.QVBoxLayout()
		self.setLayout(layout)

		chartLayout = QtGui.QGridLayout()
		layout.addLayout(chartLayout)

		self.votesChart = PieChart()
		self.votesChart.setToolTip(self.tr("Whole census"))
		chartLayout.addWidget(self.votesChart,0,0)
		self.votesChart.setSectorColors(colors)

		self.candidaturesChart = PieChart()
		self.candidaturesChart.setToolTip(self.tr("Just votes to candidatures"))
		chartLayout.addWidget(self.candidaturesChart, 0,1)
		self.candidaturesChart.setSectorColors(colors)

		self.sconsChart = PieChart()
		self.sconsChart.setToolTip(self.tr("Hondt distribution (legal)"))
		chartLayout.addWidget(self.sconsChart,0,2)
		self.sconsChart.setSectorColors(colors)

		self.proportionalChart = PieChart()
		self.proportionalChart.setToolTip(self.tr("Hamilton distribution (proportional)"))
		chartLayout.addWidget(self.proportionalChart, 0,3)
		self.proportionalChart.setSectorColors(colors)

		titleBox = QtGui.QHBoxLayout()
		layout.addLayout(titleBox)
		self.title = QtGui.QComboBox()
		titleBox.addWidget(self.title)
		self.title.setToolTip(self.tr("Current case being displayed"))
		self.title.addItems([name for name, case in self.cases])
		self.title.currentIndexChanged.connect(self.titleChanged)
		titleBox.addWidget(QtGui.QWidget()) # spacer
		prevButton = QtGui.QPushButton(self.tr("&Previous"))
		prevButton.setToolTip(self.tr("Switch to the previous case"))
		titleBox.addWidget(prevButton)
		nextButton = QtGui.QPushButton(self.tr("&Next"))
		nextButton.setToolTip(self.tr("Switch to the next case"))
		titleBox.addWidget(nextButton)

		buttonBox = QtGui.QHBoxLayout()
		layout.addLayout(buttonBox)
		self._from = QtGui.QComboBox()
		self._from.setToolTip(self.tr("Vote transfer origin"))
		self._to = QtGui.QComboBox()
		self._to.setToolTip(self.tr("Vote transfer destination"))
		transfer = QtGui.QPushButton(self.tr("&Transfer"))
		transfer.setToolTip(self.tr("Transfer votes"))
		invert = QtGui.QPushButton(self.tr("&Invert"))
		invert.setToolTip(self.tr("Swap transfer sides"))
		self._tranferSize = QtGui.QSpinBox()
		self._tranferSize.setToolTip(self.tr("Number of votes to be transferred"))
		self._tranferSize.setMinimum(1)
		self._tranferSize.setMaximum(1000000)
		self._tranferSize.setValue(10000)
		self._tranferSize.setSuffix(self.tr(" votes"))
		arrow = QtGui.QLabel("->")
		arrow.setSizePolicy(
			QtGui.QSizePolicy.Fixed,
			QtGui.QSizePolicy.Fixed,
			)
		buttonBox.addWidget(self._from)
		buttonBox.addWidget(arrow)
		buttonBox.addWidget(self._to)
		buttonBox.addWidget(self._tranferSize)
		buttonBox.addWidget(transfer)
		buttonBox.addWidget(invert)
		buttonBox.addWidget(QtGui.QWidget()) # spacer

		copyButton = QtGui.QPushButton(self.tr("&Save As"))
		copyButton.setToolTip(self.tr("Save a copy the current case with a new name"))
		buttonBox.addWidget(copyButton)
		resetButton = QtGui.QPushButton(self.tr("&Reset"))
		resetButton.setToolTip(self.tr("Restore the case to the latest saved state"))
		buttonBox.addWidget(resetButton)
		saveButton = QtGui.QPushButton(self.tr("&Save"))
		saveButton.setToolTip(self.tr("Save the changes done to the case"))
		buttonBox.addWidget(saveButton)

		statLayout = QtGui.QHBoxLayout()
		layout.addLayout(statLayout)
		def label() :
			label=QtGui.QLabel()
			statLayout.addWidget(label)
			return label
		self.censusLabel = label()
		self.abstentionLabel = label()
		self.nullLabel = label()
		self.blankLabel = label()
		self.thresholdLabel = label()
		self.seatsLabel = label()
		self.seatsSpiner = QtGui.QSpinBox()
		self.seatsSpiner.setMinimum(1)
		self.seatsSpiner.setMaximum(99999)
		statLayout.addWidget(self.seatsSpiner)

		self.restLabelHondt = QtGui.QLabel()
		layout.addWidget(self.restLabelHondt)
		self.restLabelProportional = QtGui.QLabel()
		layout.addWidget(self.restLabelProportional)

		transfer.clicked.connect(self.transfer)
		invert.clicked.connect(self.invertTransfer)
		nextButton.clicked.connect(self.nextDatabase)
		prevButton.clicked.connect(self.previousDatabase)
		saveButton.clicked.connect(self.save)
		resetButton.clicked.connect(self.reset)
		copyButton.clicked.connect(self.copy)
		self.votesChart.sectorLeftClicked.connect(self.selectFrom)
		self.votesChart.sectorRightClicked.connect(self.selectTo)
		self.candidaturesChart.sectorLeftClicked.connect(self.selectFrom)
		self.candidaturesChart.sectorRightClicked.connect(self.selectTo)
		self.proportionalChart.sectorLeftClicked.connect(self.selectFrom)
		self.proportionalChart.sectorRightClicked.connect(self.selectTo)
		self.sconsChart.sectorLeftClicked.connect(self.selectFrom)
		self.sconsChart.sectorRightClicked.connect(self.selectTo)

		self.seatsSpiner.valueChanged.connect(self.changeSeats)

		self.hondtTable = HondtTable()
		layout.addWidget(self.hondtTable)

		self.updateDatabase()


	def changeSeats(self, seats) :
		print "Value changed"
		if self._updatingSeatsSpinner : return
		self.case.representants = self.seatsSpiner.value()
		self.case.recomputeSeats()
		self.updateViews()

	def dataPath(self, name) :
		return os.path.join(self._dataPath, name+".csv")

	def reset(self) :
		name, case = self.cases[self.currentCase]
		dataFile = file(self.dataPath(name))
		self.cases[self.currentCase] = (name, Simulador.Resultats(dataFile))

		self.updateDatabase()

	def selectFrom(self, candidature) :
		index = self._from.findText(candidature)
		if index < 0 : return
		self._from.setCurrentIndex(index)

	def selectTo(self, candidature) :
		index = self._to.findText(candidature)
		if index < 0 : return
		self._to.setCurrentIndex(index)

	def copy(self) :
		name, case = self.cases[self.currentCase]
		newName, ok = QtGui.QInputDialog.getText(self,
			self.tr("Copy Data Set as"),
			self.tr("Give a new name for the copied case"),
			QtGui.QLineEdit.Normal,
			name+self.tr("-copy","default file suffix"))
		if not ok : return
		newName = str(newName)
		dataFile = file(self.dataPath(newName), "w")
		case.save(dataFile)
		dataFile = file(self.dataPath(newName), "r")
		self.cases.append((newName, Simulador.Resultats(dataFile)))
		self.currentCase=len(self.cases)-1
		self.title.addItem(newName)
		self.title.setCurrentIndex(self.currentCase)

	def save(self) :
		name, case = self.cases[self.currentCase]
		dataFile = file(self.dataPath(name), "w")
		case.save(dataFile)

	def previousDatabase(self) :
		self.currentCase -= 1
		self.currentCase %= len(self.cases)
	
		self.title.setCurrentIndex(self.currentCase)
		
	def nextDatabase(self) :
		self.currentCase += 1
		self.currentCase %= len(self.cases)

		self.title.setCurrentIndex(self.currentCase)

	def titleChanged(self, current) :
		self.currentCase = current

		self.updateDatabase()

	def transfer(self) :
		vots = self.case.vots
		fromOption = str(self._from.currentText())
		toOption = str(self._to.currentText())
		transferSize = min(vots[fromOption], self._tranferSize.value())
		vots[fromOption] -= transferSize
		vots[toOption] += transferSize
		self.case.recomputeSeats()
		self.updateViews()

	def invertTransfer(self) :
		fromOption = self._from.currentIndex()
		toOption = self._to.currentIndex()
		self._from.setCurrentIndex(toOption)
		self._to.setCurrentIndex(fromOption)

	def updateDatabase(self) :
		name, self.case = self.cases[self.currentCase]
		print "Changint to", name
		options = sorted(self.case.vots.keys())
		self._to.clear()
		self._to.addItems(options)
		self._from.clear()
		self._from.addItems(options)
		self.updateViews()

	def updateViews(self) :

		print "Computing proportional"
		toCandidatures = dict((
			(party, votes) 
			for party, votes in self.case.vots.iteritems()
			if party not in [
				'abstencion',
				'blancos',
				'nulos',
				]
			))

		print "Computing Seats"
		s = Simulador.Simulador(self.case.representants, **self.case.vots)
		scons = self.case.scons
		if not sum(self.case.scons.values()) :
			scons = s.repartiment(self.case.representants)
		proportional = s.repartimentProporcional(self.case.representants)
		integer = s.repartimentSencer(self.case.representants)
		restosHondt = [
			(party, scons[party] - integer[party])
			for party in s.partidos()
			if scons[party] != integer[party]
			]
		restosProportional = [
			(party, proportional[party] - integer[party])
			for party in s.partidos()
			if proportional[party] != integer[party]
			]
		self.restLabelHondt.setText(
			self.tr("Rests Hondt: ")+ ("".join([" %s: %+i"%rest for rest in sorted(restosHondt)])))
		self.restLabelProportional.setText(
			self.tr("Rests Hamilton: ")+ ("".join([" %s: %+i"%rest for rest in sorted(restosProportional)])))

		print "Updating Pies"
		self.votesChart.setSectorDescriptions(self.case.descripcions)
		self.votesChart.setSectorValues(**self.case.vots)
		self.candidaturesChart.setSectorDescriptions(self.case.descripcions)
		self.candidaturesChart.setSectorValues(**toCandidatures)
		self.proportionalChart.setSectorDescriptions(self.case.descripcions)
		self.proportionalChart.setSectorValues(**proportional)
		self.sconsChart.setSectorDescriptions(self.case.descripcions)
		self.sconsChart.setSectorValues(**scons)
		print "Hondt Table"
		self.hondtTable.threshold = self.case.votsValids * threshold
		self.hondtTable.nSeats = self.case.representants
		self.hondtTable.feedDescriptions(self.case.descripcions)
		self.hondtTable.feedVotations(toCandidatures)
		print "Stats"
		census = sum(self.case.vots.values())
		def displayStats(widget, text, quantity) :
			percent = 100.*quantity/census
			widget.setText("<b>%s:</b> %i (%.2f%%)"%(
				text, quantity, percent))
		self.censusLabel.setText("<b>%s:</b> %s"%(self.tr("Census"),census))

		displayStats(self.abstentionLabel, self.tr("Abstention"), self.case.vots['abstencion'])
		displayStats(self.nullLabel, self.tr("Nulls"), self.case.vots['nulos'])
		displayStats(self.blankLabel, self.tr("Blanks"), self.case.vots['blancos'])
		displayStats(self.thresholdLabel, self.tr("Threshold (%0%)").arg(threshold*100),
			threshold*(census-self.case.vots['abstencion']-self.case.vots['nulos']))
		self.seatsLabel.setText(self.tr("<b>Seats:</b>"))
		self.seatsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
		print "Updating seat spinner"
		self._updatingSeatsSpinner = True
		self.seatsSpiner.setValue(self.case.representants)
		self._updatingSeatsSpinner = False
		print "end"



