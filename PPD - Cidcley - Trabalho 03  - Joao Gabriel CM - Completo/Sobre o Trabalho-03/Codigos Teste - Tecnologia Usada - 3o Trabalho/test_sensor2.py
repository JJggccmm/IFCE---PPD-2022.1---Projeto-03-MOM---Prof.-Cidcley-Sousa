import paho.mqtt.client as mqtt #import the client1
from random import randrange, uniform
import time

broker_address="mqtt.eclipseprojects.io"


client = mqtt.Client("P3") #create new instance

client.connect(broker_address) #connect to broker

client.subscribe("house/bulbs/bulb1")

while True:
    client.publish("house/bulbs/bulb1", "AAAAAAAAAAAAAAA")
    print("Just published 'AAAAAAAAAAAAAAA' to topic house/bulbs/bulb1")
    time.sleep(1)

# Links que ajudaram:
# https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4
# http://www.steves-internet-guide.com/into-mqtt-python-client/
# https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

