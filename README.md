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

```
python3 qrcode_scad.py

# or

./qrcode_scad.py
```

The input string will be used as the data that will be stored in the QR code.
