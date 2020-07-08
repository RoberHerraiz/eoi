import time

class Sensor:

    ''' Lo vamos a simular '''

    def is_detecting_movement(self) -> bool:
        pass


class Recorder:

    ''' Lo vamos a simular '''

    def start_recording(self):
        pass

    def stop_recording(self):
        pass


class Controller:

    ''' Lo vamos a desarrollar '''

    sensor: Sensor #dependency
    recorder: Recorder #dependency


    def __init__(self, sensor, recorder):
        self.sensor = sensor
        self.recorder = recorder

    def record_movement(self, number_of_seconds=1):

        for _ in range(number_of_seconds):
            try:
                if self.sensor.is_detecting_movement():
                    self.recorder.start_recording()
                else:
                    self.recorder.stop_recording()
                    
            except ValueError as e:
                self.recorder.stop_recording()
        time.sleep(1)