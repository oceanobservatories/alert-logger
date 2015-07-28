#!/usr/bin/env python
'''
 AlertAlarm Python API
'''

import os
from qpidsender import *
home = os.path.expanduser("~")

MQ_ALARM = -1
MQ_ALERT = 1


#---------------------------------------------
class Severity:
    def __init__(self):
        self.ALARM = MQ_ALARM 
        self.ALERT = MQ_ALERT

    def getAlarm(self):
        return self.ALARM

    def getAlert(self):
        return self.ALERT

#---------------------------------------------
# for sending a message directly to AlertAlarm
class AlertAlarmMessage:
    def __init__(self, severity=MQ_ALERT):
        self.severity = severity
        self.payload = None
        self.attributes = dict([('severity', severity)])
        self.document = "alert"

    def setMessageText(self, msg):
        self.messageText = msg

    def getMessageText(self):
        return self.messageText

    def setSeverity(self, sev):
        self.severity = sev

    def getSeverity(self):
        return self.severity

    def addAttribute(self, name, value):
        self.dict[name] = value;

    def getDocumentName(self):
        return self.document

#---------------------------------------------
# for sending a message to EDEX AA-relay queue
class AlertAlarmRelay:
    def __init__(self, severity=MQ_ALERT):
        self.severity = severity
        self.document = "AlertAlarmRelay"

    def setMessageText(self, msg):
        self.messageText = msg

    def setSeverity(self, sev):
        self.severity = sev

    def getSeverity(self):
        return self.severity

    def getDocumentName(self):
        return self.document

#---------------------------------------------

class AlertLoggerConfig:
    def __init__(self):    
        try:
            self.config_file = os.environ['ALERT_LOGGER_CONF']
            with open(self.config_file) as conf_data:
                data = json.load(conf_data)

            self.host  =data["host"]
            self.port    =data["port"]
            self.address =data["address"]

        except:
            self.host  ="localhost"
            self.port  ="5672"
            self.address = "alertalarm.relay"

    def getHost(self):
        return self.host

    def getAddress(self):
        return self.address

    def getPort(self):
        return self.port

    def close(self):
        self.data_file.close

#---------------------------------------------

class AlertLogger:
    def __init__(self):
        config = AlertLoggerConfig()
        self.host  = config.getHost()
        self.qport    = config.getPort()
        self.address = config.getAddress()
        self.iport = int(self.qport)
        self.queue = QpidSender(self.address,self.host,self.iport)
        logging.debug("QpidSender(" + self.address + ", " + self.host + ", " + self.qport + ")")
        self.queue.connect()

    def send(self, message, severity = 1):
        mqm = AlertAlarmRelay()
        mqm.setMessageText(message)
        mqm.setSeverity(severity)
        jsondata = json.dumps(mqm.__dict__)
        self.queue.send(jsondata, "text/plain")

