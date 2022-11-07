import temp_utils, time, threading, sys, os



def runMeasurement(sample_rate, out_path):
    # configure method to be called at frequency equal to sample_rate
    print("\n")
    test_meas = temp_utils.measurement()
    test_meas.test = threading.Timer(sample_rate, measureTemperature, args=(sample_rate,out_path)).start()

    # perform measurement and store information in new class obj
    new_reading = 10.0  # TODO: sample from sensor here - should this be written into class?
    test_meas.temp = new_reading

    print(vars(test_meas))

    # write measurement to file
    test_meas.write_meas(out_path)





if __name__ == "__main__":
    print(f"running: {__file__}")

    ''' setup  - check that data log exists, if not - create one '''
    fn = "temp_log"
    # TODO: search for file, if none found, create it
    out_path = os.path.join(__file__, fn)

    ''' periodically, take sensor measurement and write it to file '''
    sample_rate = 1.0  # sec
    temp_meas = runMeasurement(sample_rate, out_path)

