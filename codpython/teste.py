# import usb.core

# dev = usb.core.find(idVendor=0x1A86, idProduct=0x7523)
# ep = dev[0].interfaces().endpoint()[0]
# i = dev[0].interfaces()[0].bInterfaceNumber
# dev.reset()

# if dev.is_kernel_driver_active(i):
#     dev.detach_kernel_driver(i)

# dev.set_configuration()
# eaddr = ep.bEndpointAddress

# r=dev.read(eaddr,1024)
# print(len(r))

import usb.core
import usb.util

# find our device
dev = usb.core.find(idVendor=0x1A86, idProduct=0x7523)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# print(dev)


# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

# write the data
ep.write("teste")

print(ep)