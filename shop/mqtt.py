'''Publish topics to mqtt broker'''

__author__ = "Lukas Beck"
__email__ = "st166506@stud.uni-stuttgart.de"
__copyright__ = "Lukas Beck"

__license__ = "GPL"
__version__ = "2024.03.14"

import json
import paho.mqtt.client as mqtt

class MqttPublish():
    '''Handels Publishing to mqtt broker.
    '''

    __BROKER_ADDR = "MiniFactory"
    __PORT = 1883

    def __init__(self) -> None:
        '''Init MqttInterface.'''

        # self.__BROKER_ADDR = "test.mosquitto.org"

        self.topic = "MiniFactory/Webshop/Data"

        self.client = mqtt.Client()


    def send_data(self, data: dict):
        '''Send data to given topic

        Args:
            data(dict): The data to send, if None the default data for the given topic will be sent.
        '''
        self.client.connect(self.__BROKER_ADDR, self.__PORT)
        self.client.publish(self.topic, json.dumps(data))
        print(f"Mqtt send: {json.dumps(data)}")


mqtt_handler = MqttPublish()