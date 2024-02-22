#!/usr/bin/env python3

import qrcode
from solid import *
import numpy as np
import matplotlib.pyplot as plt

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=0,
)
qr.add_data(input())
qr.make(fit=True)

qr = np.array(qr.make_image(fill_color="black", back_color="white"))

scad = (
    color('white')(cube([*qr.shape, 1])) +
    color('black') (
        union()([
            translate([i, j, 1])(cube(1))
            for i, row in enumerate(qr)
            for j, cell in enumerate(row)
            if not cell
        ])
    )
)

print(scad_render(scad))

