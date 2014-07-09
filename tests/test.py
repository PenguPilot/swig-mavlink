
# a simple performance comparison

from time import time
import os
import sys

def import_path(fullpath):
    path, filename = os.path.split(fullpath)
    filename, ext = os.path.splitext(filename)
    sys.path.append(path)
    module = __import__(filename)
    reload(module) # Might be out of date
    del sys.path[-1]
    return module

minimal = import_path('../minimal/minimal.py')


from mavlinkv10 import MAVLink

ml = MAVLink(None)


start = time()
for _ in range(100000):
   ml.heartbeat_encode(0, 1, 1, 2, 1)
a = time() - start

start = time()
msg = minimal.mavlink_message_t()
for _ in range(100000):
   minimal.mavlink_msg_heartbeat_pack(8, 9, msg, 3, 4, 5, 6, 7)
   minimal.mavlink_dumps(msg)
b = time() - start

print 'serialization speedup:', a / b

