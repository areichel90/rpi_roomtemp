from datetime import datetime

class measurement:
    ''' <> '''

    def __init__(self):
        self.time = datetime.now().time()

    def write_meas(self, fp_out:str):
        print(f"writing measurement to {fp_out}")
