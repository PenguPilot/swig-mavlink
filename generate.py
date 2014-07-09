# SWIG interface / Makefile generator for MAVLink Python Bindings

from sys import argv
from os import walk, mkdir


base_path_top = '../c_library/'
modules = []
for (dirpath, dirnames, filenames) in walk(base_path_top):
   for dir in dirnames:
      if dirpath == base_path_top and dir != '.git':
         modules.append(dir)

for module in modules:
   try:
      mkdir(module)
   except:
      pass
   base_path = '../' + base_path_top
   mod_path = base_path + module + '/'
   msg_files = []
   for (dirpath, dirnames, filenames) in walk(base_path_top + module):
      for name in filenames:
         try:
            if name[0:11] == 'mavlink_msg':
               msg_files.append(name)
         except:
            pass

   # create SWIG interface file:
   print 'creating SWIG interface for', module
   str = '%feature("autodoc", "1");\n'
   str += '%include "stdint.i"\n'
   str += '%module ' + '%s\n' % module
   str += '%{\n'
   str += '   #include "%smavlink.h"\n' % mod_path
   str += '   #include "../mavlink_swig.h"\n'
   str += '%}\n'
   str += '%include ' + '"%smavlink_types.h"\n' % base_path
   str += '%include ' + '"../mavlink_swig.h"\n'
   for file in msg_files:
      str += '%include ' + '"%s"\n' % (mod_path + file)
   file = open(module + '/' + module + '.i', 'w')
   file.write(str)
   file.close()

   print 'creating Makefile for', module
   # create Sub-Makefile:
   str = 'MODULE=%s\n' % module
   str += 'all: $(MODULE).i\n'
   str += '\tswig -python $(MODULE).i\n'
   str += '\tgcc -O3 -shared -o _$(MODULE).so -fPIC `pkg-config python --cflags` $(MODULE)_wrap.c\n'
   str += 'clean:\n'
   str += '\trm -f *.o *.pyc *.so *.c *.py\n'
   file = open(module + '/Makefile', 'w')
   file.write(str)
   file.close()

# create master Makefile
print 'creaing Makefile'
str = 'all:\n'
for module in modules:
   str += '\tmake -C %s\n' % module
str += 'clean:\n'
for module in modules:
   str += '\tmake -C %s clean\n' % module
file = open('Makefile', 'w')
file.write(str)
file.close()

print 'done'

