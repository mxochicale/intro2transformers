# 🎓 Intro to transformers
> "A transformer is a deep learning model that adopts the mechanism of self-attention, differentially weighting the significance of each part of the input data." 
[~wiki](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)). 

_‘What I cannot create. I do not understand.’ ~ Richard Feynman (1918 – 1988)_ [:tv:](https://youtu.be/GHOGAomJJjM?t=496) [:link:](https://www.quora.com/What-did-Richard-Feynman-mean-when-he-said-What-I-cannot-create-I-do-not-understand)

## Getting started!

[![Open in Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new?repo=mxochicale/intro-to-transformers)

1. Open this repo in a Codespace (click the button above!)
2. Open one of the notebooks
3. Click the `Select kernel` button in the upper-right and select `Python X`
4. Have fun! 🚀

## Table of content
1.  :wrench: [Tutorials](tutorials)
2. :school_satchel: [References](references)

## :nut_and_bolt: Installation

### Dev installation
```
curl -LsSf https://astral.sh/uv/install.sh | sh # install uv
uv venv --python 3.12 # Create a virtual environment at .venv.
source .venv/bin/activate #To activate the virtual environment
uv pip install -e ".[test,learning]" # Install the package in editable mode
uv pip list --verbose #check versions
pre-commit run -a #pre-commit hooks
```
See further details [here](docs/dependencies).


## Clone repository
The github repository link is 
https://github.com/mxochicale/intro-to-transformers

To clone this repo, you might need to generate your SSH keys as suggested [here](https://github.com/mxochicale/tools/blob/main/github/SSH.md).
You can then clone the repository by typing (or copying) the following line in a terminal at your selected path in your machine:
```
cd && mkdir -p repositories/mxochicale && cd repositories/mxochicale
git clone git@github.com:mxochicale/intro2transformers.git
```

## Issues 
If you have questions or have experiment any problems, please [open an issue](https://github.com/mxochicale/transformers-tutorials/issues). 
