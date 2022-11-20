from datetime import datetime
import adafruit_dht
from board import D4

class measurement:
    ''' <> '''

    def __init__(self):
        print("\nTaking Measurement...")
        self.time = datetime.now().time()
        #self.take_measurement()

    def take_measurement(self):
        dht_device = adafruit_dht.DHT22(D4)
        self.temperature = dht_device.temperature
        self.humidity = dht_device.humidity



if __name__ == "__main__":
    print("Starting Sensor Measurement File.")
    
    meas = measurement()
    
    print("Script Completed Successfully.")
