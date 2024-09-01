# !/bin/bash

# Install miniconda

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

# Activate miniconda
export PATH=~/miniconda3/bin:$PATH
conda init bash

# create conda environment
conda create -n frontend python=3.11
conda activate frontend

# installing dependencies
pip install -r requirements.txt