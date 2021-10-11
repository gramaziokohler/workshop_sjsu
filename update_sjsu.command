#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate sjsu
python -m pip install --no-deps --force-reinstall git+https://github.com/compas-dev/compas.git@gltf_update
