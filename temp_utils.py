from datetime import datetime
import adafruit_dht
from board import D4

def takeMeasurement(*args):
    print(args)
    dht_device = adafruit_dht.DHT22(D4)
    #measurement.temperature = dht_device.temperature
    #measurement.humidity = dht_device.humidity
    measurement.temperature = 10
    measurement.humidity = .50
    


class measurement:
    ''' <> '''

    def __init__(self):
        print("\nTaking Measurement...")
        self.time = datetime.now().time()
        #self.take_measurement()

    def take_measurement(self, *args):
        print(args)
        dht_device = adafruit_dht.DHT22(D4)
        self.temperature = dht_device.temperature
        self.humidity = dht_device.humidity

    def write_meas(self, *args):
        print("here")



if __name__ == "__main__":
    print("Starting Sensor Measurement File.")
    
    meas = measurement()
    
    print("Script Completed Successfully.")
