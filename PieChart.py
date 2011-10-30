#!/usr/bin/env python

import Simulador
from PyQt4 import QtGui, QtCore
from HondtTable import HondtTable


import sys
import math
import glob

class Sector(QtGui.QGraphicsEllipseItem) :
	class Updater(QtCore.QObject) :
		def __init__(self, sector) :
			super(QtCore.QObject, self).__init__()
			self.sector = sector

		@QtCore.pyqtProperty(int)
		def start(self) :
			return self.sector.startAngle()
		@start.setter
		def start(self, value) :
			self.sector.setStartAngle(value)
			self.sector.updateLabel()

		@QtCore.pyqtProperty(int)
		def span(self) :
			return self.sector.spanAngle()
		@span.setter
		def span(self, value) :
			self.sector.setSpanAngle(value)
			self.sector.updateLabel()

		@QtCore.pyqtProperty(float)
		def opacity(self) :
			return self.sector.opacity()
		@opacity.setter
		def opacity(self, value) :
			self.sector.setOpacity(value)

	def __init__(self, parent, rect, label) :
		super(QtGui.QGraphicsEllipseItem,self).__init__(rect)
		self.parent = parent
		self.setToolTip(label)
		self.line = QtGui.QGraphicsLineItem(self)
		self.label = QtGui.QGraphicsSimpleTextItem(label, self)
		self.labelBox = QtGui.QGraphicsRectItem(self.label.boundingRect(), self)
		self.labelBox.setBrush(QtGui.QColor("white"))
		self.labelBox.setPen(QtGui.QColor("black"))
		self.labelBox.setZValue(20)
		self.label.setZValue(30)
		duration = 200
		self.updater = Sector.Updater(self)
		self.startAnimation = QtCore.QPropertyAnimation(self.updater, 'start')
		self.spanAnimation = QtCore.QPropertyAnimation(self.updater, 'span')
		self.fadeIn = QtCore.QPropertyAnimation(self.updater, 'opacity')
		self.fadeOut = QtCore.QPropertyAnimation(self.updater, 'opacity')
		self.startAnimation.setDuration(duration);
		self.spanAnimation.setDuration(duration);
		self.fadeIn.setDuration(duration/3);
		self.fadeOut.setDuration(duration/3);
		self.fadeOut.setKeyValueAt(0., 1.)
		self.fadeOut.setKeyValueAt(1, .8)
		self.fadeIn.setKeyValueAt(0, .8)
		self.fadeIn.setKeyValueAt(1., 1.)
		self.animation = QtCore.QSequentialAnimationGroup(self.updater)
		self.animation.addAnimation(self.fadeOut)
		self.animation.addAnimation(self.spanAnimation)
		self.animation.addAnimation(self.startAnimation)
		self.animation.addAnimation(self.fadeIn)

	def move(self, start, span) :
		self.startAnimation.setEndValue(start)
		self.spanAnimation.setEndValue(span)
		self.animation.start()

	def updateLabel(self) :
		angle = (self.spanAngle()/2 + self.startAngle())/16
		radius = self.parent.radius
		pos = QtCore.QPointF(
				radius*1.1*math.cos(math.radians(angle))-self.labelBox.rect().width()/2,
				-radius*1.1*math.sin(math.radians(angle))+self.labelBox.rect().height()/2,
				)
		self.line.setLine(
			QtCore.QLineF(
				QtCore.QPointF(0,0),
				pos,
			))
		self.label.setPos(pos)
		self.labelBox.setPos(pos)

		self.line.setPen(self.brush().color())
		self.labelBox.setPen(self.brush().color())
		self.labelBox.setBrush(self.brush().color().lighter())

class PieChart(QtGui.QGraphicsView) :

	def __init__(self, radius=100, maxAngle = 360) :
		QtGui.QGraphicsView.__init__(self)
		self.setRenderHints(
			QtGui.QPainter.Antialiasing | 
			QtGui.QPainter.SmoothPixmapTransform);
		self.scene = QtGui.QGraphicsScene()
		self.setScene(self.scene)
		self.colors = (
			"green orange purple magenta yellow blue red aquamarine "+
			"gold greenyellow khaki sienna sandybrown skyblue Thistle orchid tomato "
			"darkcyan "
		).split()
		self.maxAngle = maxAngle * 16 # 16th of degree
		self.radius = 100
		self.sectors = {}
		self._sectorColors = {}

	def setSectorColors(self, sectorColors) :
		self._sectorColors = sectorColors

	def resizeEvent(self, event) :
		super(PieChart, self).resizeEvent(event)
		size = event.size()
		self.radius = min(size.width(), size.height())/2.5
		self.rect = QtCore.QRectF(-self.radius, -self.radius, 2*self.radius, 2*self.radius)
		for sector in self.sectors.itervalues() :
			sector.setRect(self.rect)

	def setSectorValues(self, **sectors) :
		removedNames = [ name 
			for name, sector in self.sectors.iteritems()
			if name not in sectors ]
		for name in removedNames :
			self.scene.removeItem(self.sectors[name])
			del self.sectors[name]
		total = sum((quantity for quantity in sectors.values()))
		sortedSectors = sorted(((value, name) for name, value in sectors.iteritems()))
		angle = 0
		for i, (value, name) in enumerate(sortedSectors) :
			try :
				colorName = self._sectorColors[name]
			except KeyError :
				colorName = self.colors[i%len(self.colors)]
			color = QtGui.QColor(colorName)
			try :
				sector = self.sectors[name]
			except KeyError :
				sector = Sector(self, self.rect, name)
				sector.setPen(color.lighter())
				sector.setStartAngle(0)
				sector.setSpanAngle(0)
				sector.setBrush(color)
				self.scene.addItem(sector)
			span = self.maxAngle*(float(value)/total)
			sector.move(angle,span)
			angle += span
			self.sectors[name]=sector


if __name__ == "__main__" :
	import random

	app = QtGui.QApplication(sys.argv)
	window = QtGui.QDialog()
	window.setLayout(QtGui.QVBoxLayout())
	pie = PieChart()
	sectors = pie.colors
	def switch() :
		pie.setSectorValues(**dict((
			(v, random.randint(1,1000))
			for v in sectors)))
	window.layout().addWidget(pie)
	button = QtGui.QPushButton("switch")
	window.layout().addWidget(button)
	colors = dict((v,v) for v in sectors)
	pie.setSectorColors(colors)
	button.clicked.connect(switch)

	window.setWindowTitle("Simulador de votacions")
	window.resize(500,500)
	window.show()

	sys.exit(app.exec_())






