
SWIG Python MAVLink Implementation
----------------------------------

Compiling the Bindings
----------------------

```
mkdir new_dir
cd new_dir
git clone https://github.com/mavlink/c_library
git clone https://github.com/PenguPilot/swig-mavlink
cd swig_mavlink
python generate.py
make
cd tests
python test.py
```

Required Packages
-----------------

- Python headers
- SWIG
- GCC
- pkg-config
