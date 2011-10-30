#!/usr/bin/env python

import Simulador
from PyQt4 import QtGui, QtCore
import sys

class HondtTable(QtGui.QTableWidget) :
	def __init__(self) :
		super(HondtTable, self).__init__()
		self._nSeats = 10
		self._threshold = .03

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
		self._votations = [
			(party,votes) 
			for votes, party in 
				reversed(sorted(
					(votes, party) for party, votes in results.iteritems()))
			 ]
		self.setVerticalHeaderLabels([
			party for party, votes in self._votations])

		self._seats = []
		for i, (party, votes) in enumerate(self._votations) :
			for seat in xrange(1, self.nSeats+1) :
				item = QtGui.QTableWidgetItem("%i"%(votes/seat))
				self.setItem(i, seat-1, item)
				self._seats.append( ( (votes/seat), item) )
		self._seats.sort()

		# Mark taken seats
		for number, seatItem in self._seats[-self.nSeats:] :
			seatItem.setBackground(QtGui.QColor("#ddb"))

		# Mark last competition in red
		self._seats[-self.nSeats][1].setForeground(
			QtGui.QColor("red"))
		self._seats[-self.nSeats-1][1].setForeground(
			QtGui.QColor("red"))

		# Mark next competition in orange
		self._seats[-self.nSeats+1][1].setForeground(
			QtGui.QColor("orange"))
		self._seats[-self.nSeats-2][1].setForeground(
			QtGui.QColor("orange"))

		self.resizeColumnsToContents()
		self.resizeRowsToContents()



if __name__ == "__main__" :
	app = QtGui.QApplication(sys.argv)
	window = HondtTable()
	window.setWindowTitle("Simulador de votacions")
	window.nSeats = 31
	window.feedVotations(dict(
		unos=7453,
		esos=15575,
		otros=23434,
		aquellos=3434,
		))

	window.show()

	sys.exit(app.exec_())






