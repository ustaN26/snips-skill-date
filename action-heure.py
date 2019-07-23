#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from datetime import datetime
from pytz import timezone

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

def intent_received(hermes, intent_message):
	print(intent_message.intent.intent_name)

	if intentMessage.intent.intent_name == 'ustaN:date':
		MonthList = ['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']
		DayList = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
		dayNumber = date.today().day
		weekday = DayList[date.today().weekday()-1]
		sentence = "On est le " + weekday + " " + str(dayNumber) + " "+ MonthList[date.today().month-1]
		print(sentence)
		hermes.publish_end_session(intentMessage.session_id, sentence)

with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()