#!/usr/bin/env python3
# See https://github.com/AmedeeBulle/pyrak811
from rak811 import Mode, Rak811
import os

print(os.environ['HOME'])
dev_eui = os.getenv('dev_eui')
app_eui = os.getenv('app_eui')
app_key = os.getenv('app_key')

if not dev_eui:
  raise SystemExit('dev_eui empty')
if not app_eui:
  raise SystemExit('app_eui empty')
if not app_key:
  raise SystemExit('app_key empty')

lora = Rak811()
lora.hard_reset()
lora.mode = Mode.LoRaWan
lora.band = 'EU868'
lora.set_config(dev_eui=dev_eui,
                app_eui=app_eui,
                app_key=app_key)
lora.join_otaa()
lora.dr = 5
print('Joined The Things Network')
lora.send('Hello world')
print('Sent Hello message')

# Go to the Console to set the message you want to send
# The message will be repeated until changed
if lora.nb_downlinks:
  print('Received', lora.get_downlink()['data'].hex())
lora.close()
