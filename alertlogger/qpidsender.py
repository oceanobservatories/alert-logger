#!/usr/bin/env python

import os
import sys
import json
import logging
from qpid.messaging import *
home = os.path.expanduser("~")

#---------------------------------------------
class QpidSender:
    def __init__(self, address, host="localhost", port=5672, user="guest",
            password="guest"):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.address=address

    def connect(self):
        try:
            self.connection = Connection(host=self.host, port=self.port,
                    username=self.user, password=self.password)
            self.connection.open()
            self.session = self.connection.session()
            self.sender = self.session.sender(self.address)
        except MessagingError,m:
            logging.debug(m)

    def send(self, message, content_type):
        self.sender.send(Message(content=message, content_type=content_type,
                user_id=self.user))

    def close(self):
        self.connection.close()


