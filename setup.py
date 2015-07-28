
#from setuptools import setup, find_packages
#    packages=find_packages(),
from distutils.core import setup

setup(
    name='AlertLogger',
    version='1.0',
    description='Interface to UFrame Alert/Alarm notification facility',
    url="http://github.com/oceanobservatories/alarm-logger",
    keywords=['oceanography', 'AlertAlarm','uframe'],
    packages=['alertlogger'],
    package_data={'alertlogger': ['etc/alertalarm.conf']},
)

