
import bluepy.btle as btle

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

# TODO failing to connect; probably because we should handle notifications but not connect?
p = btle.Peripheral( devicemac ).withDelegate(MyDelegate({}) )
for s in p.getServices():
  print(s)

# Setup to turn notifications on, e.g.
#   svc = p.getServiceByUUID( service_uuid )
#   ch = svc.getCharacteristics( char_uuid )[0]
#   ch.write( setup_data )

# Main loop --------

while True:
    if p.waitForNotifications(1.0):
        # handleNotification() was called
        continue

    print("Waiting...")
    # Perhaps do something else here
