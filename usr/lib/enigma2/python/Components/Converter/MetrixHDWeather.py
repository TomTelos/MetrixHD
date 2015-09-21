#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#######################################################################
#
#    UserSkin for Enigma2
#    Coded by iMaxxx (c) 2013
#    Support: www.vuplus-support.com
#
#
#  This plugin is licensed under the Creative Commons
#  Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#  To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
#  or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
#
#
#
#  This plugin is NOT free software. It is open source, you are allowed to
#  modify it (if you keep the license), but it may not be commercially
#  distributed other than under the conditions noted above.
#
#
#######################################################################
from Components.Converter.Converter import Converter
from Components.config import config, ConfigText, ConfigNumber, ConfigDateTime
from Components.Element import cached

class MetrixHDWeather(Converter, object):
	
	def __init__(self, type):
		Converter.__init__(self, type)
		self.type = type
			
	@cached
	def getText(self):
		try:
			if self.type == "currentLocation":
				return config.plugins.UserSkin.currentLocation.value
			if self.type == "currentWeatherTemp":
				return config.plugins.UserSkin.currentWeatherTemp.value
			elif self.type == "currentWeatherText":
				return config.plugins.UserSkin.currentWeatherText.value
			elif self.type == "currentWeatherCode":
				return config.plugins.UserSkin.currentWeatherCode.value
			elif self.type == "forecastTodayCode":
				return config.plugins.UserSkin.forecastTodayCode.value
			elif self.type == "forecastTodayTempMin":
				return config.plugins.UserSkin.forecastTodayTempMin.value + " " + self.getCF()
			elif self.type == "forecastTodayTempMax":
				return config.plugins.UserSkin.forecastTodayTempMax.value + " " + self.getCF()
			elif self.type == "forecastTodayText":
				return config.plugins.UserSkin.forecastTodayText.value
			elif self.type == "forecastTomorrowCode":
				return config.plugins.UserSkin.forecastTomorrowCode.value
			elif self.type == "forecastTomorrowTempMin":
				return config.plugins.UserSkin.forecastTomorrowTempMin.value + " " + self.getCF()
			elif self.type == "forecastTomorrowTempMax":
				return config.plugins.UserSkin.forecastTomorrowTempMax.value + " " + self.getCF()
			elif self.type == "forecastTomorrowText":
				return config.plugins.UserSkin.forecastTomorrowText.value
			elif self.type == "title":
				return self.getCF() + " | " + config.plugins.UserSkin.currentLocation.value
			elif self.type == "CF":
				return self.getCF() 
			else:
				return ""
		except:
			return ""
		
		
	def getCF(self):
		if config.plugins.UserSkin.tempUnit.value == "Fahrenheit":
			return "°F"
		else: 
			return "°C"
		

	text = property(getText)