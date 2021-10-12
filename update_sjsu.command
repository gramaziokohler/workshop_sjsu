#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate sjsu
python -m pip install --no-deps --force-reinstall https://github.com/compas-dev/compas/archive/gltf_update.zip