
import bluepy.btle as btle
import sys
import binascii

devicemac = "e7:5b:f9:bf:02:52"

class MyDelegate(btle.DefaultDelegate):
  def __init__(self, params):
    btle.DefaultDelegate.__init__(self)
    # ... initialise here

  def handleNotification(self, cHandle, data):
    pass
    # ... perhaps check cHandle
    # ... process 'data'


# Initialisation  -------

# random address type is needed to connect to turntouch.
p = btle.Peripheral(devicemac, addrType=btle.ADDR_TYPE_RANDOM).withDelegate( MyDelegate({}) )
print("connected")

print("waiting for notif")
p.waitForNotifications(4)
print("done waiting for notif")

buttonc = None

for s in p.getCharacteristics():
  if str(s.uuid) == '99c31525-dc4f-41b1-bb04-4e4deb81fadd':
    buttonc = s

if not buttonc:
  print("did not find button characteristic, so.. not much we can do from here.")
  sys.exit(-1)

#for s in p.getServices():
#  print(s, str(s.uuid))
  # sample services; xref with the api page: https://shop.turntouch.com/pages/open-source

bret = buttonc.read()
print(bret)
print(binascii.b2a_hex(bret).decode('utf-8'))
# is returning ff00.

# TODO: write 'NOTIFY' and then listen




# Setup to turn notifications on, e.g.
#   svc = p.getServiceByUUID( service_uuid )
#   ch = svc.getCharacteristics( char_uuid )[0]
#   ch.write( setup_data )

# Main loop --------

while False:
    if p.waitForNotifications(1.0):
        # handleNotification() was called
        continue

    #print("Waiting...")
    # Perhaps do something else here
