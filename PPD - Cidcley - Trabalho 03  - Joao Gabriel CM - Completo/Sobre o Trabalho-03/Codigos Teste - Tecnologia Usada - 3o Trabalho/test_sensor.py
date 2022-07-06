import paho.mqtt.client as mqtt #import the client1
from random import randrange, uniform
import time

broker_address="mqtt.eclipseprojects.io"


client = mqtt.Client("P1") #create new instance

client.connect(broker_address) #connect to broker

client.subscribe("house/bulbs/bulb1")

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("house/bulbs/bulb1", randNumber)
    print("Just published " + str(randNumber) + " to topic house/bulbs/bulb1")
    time.sleep(1)

# Links que ajudaram:
# https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4
# http://www.steves-internet-guide.com/into-mqtt-python-client/
# http://www.steves-internet-guide.com/receiving-messages-mqtt-python-client/
# https://www.emqx.com/en/blog/how-to-use-mqtt-in-python

