# -*- coding: UTF-8 -*-
#######################################################################
#
#    MyMetrixLite by arn354 & svox
#    based on
#    MyMetrix
#    Coded by iMaxxx (c) 2013
#
#
#  This plugin is licensed under the Creative Commons
#  Attribution-NonCommercial-ShareAlike 3.0 Unported License.
#  To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
#  or send a letter to Creative Commons, 559 Nathan Abbott Way, Stanford, California 94305, USA.
#
#  This plugin is NOT free software. It is open source, you are allowed to
#  modify it (if you keep the license), but it may not be commercially
#  distributed other than under the conditions noted above.
#
#
#######################################################################

from Components.config import config, ConfigSubsection, ConfigSelection, ConfigNumber, ConfigYesNo, ConfigText
from os import path
import gettext

#############################################################

def initWeatherConfig():
    config.plugins.AtileHD = ConfigSubsection()

    #AtileHD

    config.plugins.AtileHD.enabled = ConfigYesNo(default=True)
    config.plugins.AtileHD.MoviePlayer = ConfigYesNo(default=True)
    config.plugins.AtileHD.refreshInterval = ConfigNumber(default=60)
    config.plugins.AtileHD.woeid = ConfigNumber(default=676757) #Location (visit metrixhd.info)
    config.plugins.AtileHD.tempUnit = ConfigSelection(default="Celsius", choices = [
        ("Celsius", _("Celsius")),
        ("Fahrenheit", _("Fahrenheit"))
    ])


    ## RENDERER CONFIG:

    config.plugins.AtileHD.currentLocation = ConfigText(default="N/A")
    config.plugins.AtileHD.currentWeatherCode = ConfigText(default="(")
    config.plugins.AtileHD.currentWeatherText = ConfigText(default="N/A")
    config.plugins.AtileHD.currentWeatherTemp = ConfigText(default="0")

    config.plugins.AtileHD.forecastTodayCode = ConfigText(default="(")
    config.plugins.AtileHD.forecastTodayText = ConfigText(default="N/A")
    config.plugins.AtileHD.forecastTodayTempMin = ConfigText(default="0")
    config.plugins.AtileHD.forecastTodayTempMax = ConfigText(default="0")

    config.plugins.AtileHD.forecastTomorrowCode = ConfigText(default="(")
    config.plugins.AtileHD.forecastTomorrowText = ConfigText(default="N/A")
    config.plugins.AtileHD.forecastTomorrowTempMin = ConfigText(default="0")
    config.plugins.AtileHD.forecastTomorrowTempMax = ConfigText(default="0")

#######################################################################