import temp_utils
from temp_utils import *

def testFunc():
    test_meas = temp_utils.measurement()

    print(vars(test_meas))


if __name__ == "__main__":
    print("running")

    testFunc()

    print("run complete.")