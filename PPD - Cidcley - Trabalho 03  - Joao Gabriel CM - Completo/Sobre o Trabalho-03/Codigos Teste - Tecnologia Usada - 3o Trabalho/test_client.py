import paho.mqtt.client as mqtt #import the client1
import time
from queue import Queue

q = Queue()

############
def on_message(client, userdata, message):
    global q
    q.put(str(message.payload.decode("utf-8")))
    print(q.get())
    #print("message received " ,str(message.payload.decode("utf-8")))
    
########################################
    
broker_address="mqtt.eclipseprojects.io"

client = mqtt.Client("P2") #create new instance

client.connect(broker_address) #connect to broker

client.subscribe("house/bulbs/bulb1")

client.loop_start()

client.on_message=on_message #attach function to callback

#time.sleep(30)
#client.loop_stop()


