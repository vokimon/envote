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

import Simulador
from PyQt4 import QtGui, QtCore
import sys

class HondtTable(QtGui.QTableWidget) :
	def __init__(self) :
		super(HondtTable, self).__init__()
		self._nSeats = 10
		self._threshold = 0
		self._votations = []
		self._descriptions = {}

		self.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
		self.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
#		self.setSelectionBehavior(QtGui.QTableWidget.SelectRows)
		self.setTabKeyNavigation(False)


	@QtCore.pyqtProperty(int)
	def nSeats(self) :
		return self._nSeats
	@nSeats.setter
	def nSeats(self, value) :
		self._nSeats = value

	@QtCore.pyqtProperty(float)
	def threshold(self) :
		return self._threshold
	@threshold.setter
	def threshold(self, value) :
		self._threshold = value

	def feedDescriptions(self, descriptions) :
		self._descriptions = descriptions

	def feedVotations(self, results) :
		# Sort Parties by votes
		self._votations = [
			(party,votes) 
			for votes, party in 
				reversed(sorted(
					(votes, party)
					for party, votes in results.iteritems()))
			 ]
		self.redistribute()

	def redistribute(self) :
		self.clear()
		nParties = len(self._votations)
		self.setRowCount(nParties)
		self.setColumnCount(self.nSeats)

		self.verticalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
		self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
		# Adding party names
		print "Adding party names"
		self.setVerticalHeaderLabels([
			party for party, votes in self._votations])
		for i, (party, votation) in enumerate(self._votations) :
			self.verticalHeaderItem(i).setToolTip(
				self._descriptions.get(party,party))

		# Excluded parties
		firstThresholdedParty = len(
			[party for party, votes in self._votations
				if votes > self._threshold])


		# Distribute seats value
		print "Distribute seats value"
		self._seats = []
		for i, (party, votes) in enumerate(self._votations) :
			for seat in xrange(1, self.nSeats+1) :
				item = QtGui.QTableWidgetItem("%i"%(votes/seat))
				item.setToolTip("%i / %i %s" % (votes, seat, party))
				item.setTextAlignment(QtCore.Qt.AlignRight)
				self.setItem(i, seat-1, item)
				if i < firstThresholdedParty :
					self._seats.append( ( (votes/seat), item) )
		self._seats.sort()

		# Mark parties under threshold
		print "Mark parties under threshold"
		for party in xrange(firstThresholdedParty, nParties) :
			for seat in xrange(self.nSeats) :
				item = self.item(party, seat)
				item.setForeground(QtGui.QColor("#bbb"))
				item.setToolTip(
					item.toolTip()+'\n'+
					self.tr("Divisor removed by %0% valid vote threshold").arg(3)
					)

		# Mark taken seats
		print "Mark taken seats"
		for number, seatItem in self._seats[-self.nSeats:] :
			seatItem.setBackground(QtGui.QColor("#55f"))
			seatItem.setForeground(QtGui.QColor("white"))

		# Mark seats next to the border
		print "Mark seats next to the border"
		borderNearSeats = self._seats[-self.nSeats-2:-self.nSeats+2]
		nearSeattooltips = [
			self.tr("Second candidate out"),
			self.tr("First candidate out"),
			self.tr("Last to get in"),
			self.tr("Last but one to get in"),
		]
		for (divisor, seat), tooltip in zip(borderNearSeats, nearSeattooltips) :
			seat.setForeground(QtGui.QColor("orange"))
			seat.setToolTip(seat.toolTip()+'\n'+tooltip)

		# Mark seats in the border between in and out
		borderSeats = self._seats[-self.nSeats-1:-self.nSeats+1]
		for seat in borderSeats :
			seat[1].setForeground(QtGui.QColor("red"))

		# Resizing
		print "Resizing"
		self.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
		self.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
		print "HondtTable done"


if __name__ == "__main__" :
	app = QtGui.QApplication(sys.argv)
	window = HondtTable()
	window.setWindowTitle("Hondt table display")
	window.nSeats = 31
	window.threshold = 2000
	window.feedVotations(dict(
		party1=7453,
		party2=15575,
		party3=23434,
		party4=5434,
		party5=3435,
		party6=2834,
		party7=3438,
		party8=1433,
		party9=431,
		))
	window.resize(600, 300)

	window.show()

	sys.exit(app.exec_())


