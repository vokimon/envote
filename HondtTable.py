#!/usr/bin/env python

import Simulador
from PyQt4 import QtGui, QtCore
import sys

class HondtTable(QtGui.QTableWidget) :
	def __init__(self) :
		super(HondtTable, self).__init__()
		self._nSeats = 10
		self._threshold = .03

		self.verticalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)
		self.horizontalHeader().setResizeMode(QtGui.QHeaderView.ResizeToContents)


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


	def feedVotations(self, results) :
		nParties = len(results)
		self.clear()
		self.setRowCount(nParties)
		self.setColumnCount(self.nSeats)

		# Sort Parties by votes
		self._votations = [
			(party,votes) 
			for votes, party in 
				reversed(sorted(
					(votes, party) for party, votes in results.iteritems()))
			 ]

		# Adding party names
		self.setVerticalHeaderLabels([
			party for party, votes in self._votations])

		# Distribute seats value
		self._seats = []
		for i, (party, votes) in enumerate(self._votations) :
			for seat in xrange(1, self.nSeats+1) :
				item = QtGui.QTableWidgetItem("%i"%(votes/seat))
				item.setTextAlignment(QtCore.Qt.AlignRight);
				self.setItem(i, seat-1, item)
				self._seats.append( ( (votes/seat), item) )
		self._seats.sort()

		# Mark parties under threshold
		# TODO: Blank votes not considered yet
		firstThresholdedParty = len(
			[party for party, votes in self._votations
				if votes > self._threshold])

		for party in xrange(firstThresholdedParty, nParties) :
			for seat in xrange(self.nSeats) :
				item = self.item(party, seat)
				item.setForeground(QtGui.QColor("#bbb"))

		# Mark taken seats
		for number, seatItem in self._seats[-self.nSeats:] :
			seatItem.setBackground(QtGui.QColor("#ddb"))

		# Mark seats in the border between in and out
		self._seats[-self.nSeats][1].setForeground(
			QtGui.QColor("red"))
		self._seats[-self.nSeats-1][1].setForeground(
			QtGui.QColor("red"))

		# Mark seats next to the border
		self._seats[-self.nSeats+1][1].setForeground(
			QtGui.QColor("orange"))
		self._seats[-self.nSeats-2][1].setForeground(
			QtGui.QColor("orange"))


if __name__ == "__main__" :
	app = QtGui.QApplication(sys.argv)
	window = HondtTable()
	window.setWindowTitle("Simulador de votacions")
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

	window.show()

	sys.exit(app.exec_())






