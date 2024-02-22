#!/bin/bash

scad_output=$(mktemp)

./qrcode_scad.py > $scad_output
echo "generating stl"
openscad $scad_output -o generated.stl

rm $scad_output
