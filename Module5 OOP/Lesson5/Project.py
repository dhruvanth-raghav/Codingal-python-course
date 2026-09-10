from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def show_device(self, name):
        print(name)

@abstractmethod
def turn_on(self):
    pass

class SmartLight(SmartDevice):
    def turn_on(self):
        print("Light is ON💡")

class SmartFan(SmartDevice):
    def turn_on(self):
        print("Fan is ON💨")

class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Speaker is ON🔊")

light = SmartLight()
fan = SmartFan()
speaker = SmartSpeaker()

light.show_device("LIGHT")
light.turn_on()
fan.show_device("FAN")
fan.turn_on()
speaker.show_device("SPEAKER")
speaker.turn_on()

class SecurityCamera:
    def check_status(self):
        print("Camera is working🫆")

class DoorLock:
    def check_status(self):
        print("Door is locked🔒")

devices = [SecurityCamera(), DoorLock()]

for device in devices:
    device.check_status()