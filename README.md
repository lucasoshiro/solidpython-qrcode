# SolidPython QR code

A simples `.scad` and `.stl` file generator that creates QR codes for 3D printing.

## How to run

### Dependencies

You'll need these Python packages:

- `solidpython`
- `qrcode`

Both are available on PyPI and can be installed using Pip. If you are using an
Arch Linux based distro you can install them using Pacman
(`sudo pacman -S python-solidpython python-qrcode`).

You'll also need OpenSCAD in order to generate the `.stl` file.

### Using `qrcode_scad.py`

Run:

```bash
python3 qrcode_scad.py > my_scad.scad

# or

./qrcode_scad.py > my_scad.scad
```

The input string will be used as the data that will be stored in the QR
code. This will generate a `.scad` file.

### Using `qrcode_stl.sh`

This script calls `qrcode_scad.py` and them calls `openscad` to generate the
`.stl` file. Run:

```bash

bash qrcode_stl.sh

# or

./qrcode_stl.sh
```

Just like before, the input string will be used as the data that will be stored
in the QR code. This will generate a `.stl` file, ready for slicing.
