#!/usr/bin/env python3
from hermes_python.hermes import Hermes
from datetime import datetime
from pytz import timezone
import os

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def verbalise_day(i):
	if i == 1:
		return "Lundi"
	elif i == 2:
		return "Mardi"
	elif i == 3:
		return "Mercredi"
	elif i == 4:
		return "Jeudi"
	elif i == 5:
		return "Vendredi"
	elif i == 6:
		return "Samedi"
	elif i == 7:
		return "Dimanche"
	else:
		return "erreur"

def verbalise_mounth(i):
	if i == 1:
		return "Janvier"
	elif i == 2:
		return "Fevrier"
	elif i == 3:
		return "Mars"
	elif i == 4:
		return "Avril"
	elif i == 5:
		return "Mai"
	elif i == 6:
		return "Juin"
	elif i == 7:
		return "Juillet"
	elif i == 8:
		return "Aout"
	elif i == 9:
		return "Septembre"
	elif i == 10:
		return "Octobre"
	elif i == 11:
		return "Novembre"
	elif i == 12:
		return "Decembre"
	else:
		return "erreur"


def intent_received(hermes, intent_message):
	print(intent_message.intent.intent_name)

	if intent_message.intent.intent_name == 'ustaN:date':

		sentence = 'Nous sommes le '
		print(intent_message.intent.intent_name)

		now = datetime.now(timezone('Europe/Paris'))

		sentence += verbalise_day(now.date().isoweekday()) + " " + str(now.day) + " " + verbalise_mounth(now.month) + " " + str(now.year)
		print(sentence)

		os.system("python ./adds/tare.py")

		hermes.publish_end_session(intent_message.session_id, sentence)

with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()