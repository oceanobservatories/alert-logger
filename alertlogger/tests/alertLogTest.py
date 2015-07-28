#!/usr/bin/env python

from alertlogger.alertlogger import AlertLogger

def testMessageQueue():
    alert = AlertLogger()

    # Send an "Alarm" (-1) -- EDEX will write this to the DB
    message1 = "Python says, the sensors are exploding!"
    alert.send(message1, -1)

    # Sendan "Alert", default (1)
    message2 = "Python says, sensors are boiling water!"
    alert.send(message2)

testMessageQueue()

