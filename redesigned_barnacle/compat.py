from enum import Enum
import os


class Stub():
  pass

class Platform(Enum):
  Unknown = 0
  X86 = 1
  ESP32 = 10
  ATSADM21 = 20
  ATSAMD51 = 21

def get_platform():
  uname = os.uname()

  if uname.machine == 'ESP32 module with ESP32':
    return Platform.ESP32
  elif uname.machine == 'x86_64':
    return Platform.X86
  else:
    return Platform.Unknown

# globals
platform = get_platform()
if platform == Platform.ESP32:
  import machine 
  import network 

  I2C = machine.I2C
  LAN = network.LAN
  Pin = machine.Pin
  WLAN = network.WLAN
elif platform == Platform.X86:
  I2C = Stub
  LAN = None
  Pin = None
  WLAN = None
else:
  I2C = None
  LAN = None
  Pin = None
  WLAN = None

