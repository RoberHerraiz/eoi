import unittest

from camera import Controller, Sensor, Recorder
from doublex import Spy, Stub, assert_that, called


class CameraTestsUsingLibrary(unittest.TestCase):
    def test_asks_the_recorder_to_stop_recording_when_no_information_received_from_sensor(self):
        sensor = Stub(Sensor)
        recorder = Spy(Recorder)
        controller = Controller(sensor, recorder)

        controller.record_movement()

        assert_that(recorder.stop_recording, called())

    def test_stops_the_recording_if_sensor_raises_an_exception(self):
        with Stub(Sensor) as sensor:
            sensor.is_detecting_movement().raises(ValueError)
        recorder = Spy(Recorder)
        controller = Controller(sensor, recorder)

        controller.record_movement()

        assert_that(recorder.stop_recording, called())
    
    def test_check_the_sensor_once_per_second(self):
        sensor = Stub(Sensor)
        recorder = Spy(Recorder)
        controller = Controller(sensor, recorder)
        # medir aqui la hora
        controller.record_movement(3)
        # volver a medir aquí la hora
        assert_that(recorder.stop_recording, called().times(3))
        # assert que los segundos transcurridos son 3


class StubMovementSensor(Sensor):
    def is_detecting_movement(self) -> bool:
        return True


class StubNoMovementSensor(Sensor):
    def is_detecting_movement(self) -> bool:
        return False


class SpyRecorder(Recorder):
    start_called = False
    start_call_count = 0
    stop_called = False
    stop_call_count = 0

    def start_recording(self):
        self.start_called = True
        self.start_call_count += 1

    def stop_recording(self):
        self.stop_called = True
        self.stop_call_count += 1


class CameraTestsUsingInheritanceMocks(unittest.TestCase):
    def test_asks_the_recorder_to_stop_recording_when_no_information_received_from_sensor(self):
        sensor = StubNoMovementSensor()
        recorder = SpyRecorder()
        controller = Controller(sensor, recorder)

        controller.record_movement()

        self.assertTrue(recorder.stop_called)

    def test_asks_the_recorder_to_start_recording_when_no_sensor_detects_movement(self):
        sensor = StubMovementSensor()
        recorder = SpyRecorder()
        controller = Controller(sensor, recorder)

        controller.record_movement()

        self.assertTrue(recorder.start_called)


class CameraTestsUsingMonkeyPatchingForMocks(unittest.TestCase):
    sensor: Sensor
    recorder: Recorder
    controller: Controller

    def setUp(self) -> None:
        self.sensor = Sensor()  # mocks
        self.recorder = Recorder()  # mocks
        self.controller = Controller(self.sensor, self.recorder)
        self.called = False

    def test_asks_the_recorder_to_stop_recording_when_no_information_received_from_sensor(self):
        self.sensor.is_detecting_movement = lambda: False
        self.recorder.stop_recording = self.save_call

        self.controller.record_movement()

        self.assertTrue(self.called)

    def test_asks_the_recorder_to_start_recording_when_no_sensor_detects_movement(self):
        self.sensor.is_detecting_movement = lambda: True
        self.recorder.start_recording = self.save_call

        self.controller.record_movement()

        self.assertTrue(self.called)

    def save_call(self):
        self.called = True