
# encode message using Python/C and decode it using plain Python interface


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

msg = minimal.mavlink_message_t()
packed_size = minimal.mavlink_msg_heartbeat_pack(8, 9, msg, 3, 4, 5, 6, 7)

s = minimal.mavlink_dumps(msg)
for c in s:
   m = ml.parse_char(c)
   if m:
      print m

