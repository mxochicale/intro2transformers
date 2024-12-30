# Setting up python env 

## uv env
```
curl -LsSf https://astral.sh/uv/install.sh | sh # install uv
uv venv --python 3.12 # Create a virtual environment at .venv.
source .venv/bin/activate #To activate the virtual environment
```

## Hardware

* OS
```
$ hostnamectl

 Static hostname: --
       Icon name: computer-laptop
         Chassis: laptop
      Machine ID: --
         Boot ID: --
Operating System: Ubuntu 22.04.1 LTS              
          Kernel: Linux 5.15.0-56-generic
    Architecture: x86-64
 Hardware Vendor: --

```

* GPU
```
$ nvidia-smi -q

==============NVSMI LOG==============

Timestamp                                 : Sat Dec 17 13:27:52 2022
Driver Version                            : 520.61.05
CUDA Version                              : 11.8

Attached GPUs                             : 1
GPU 00000000:01:00.0
    Product Name                          : NVIDIA RTX A2000 8GB Laptop GPU
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere

```


## Codespaces 

* Create conda env in the terminal 
``` 
#cd ../../
#source ~/.bashrc
#conda create -n eVE -c conda-forge # environment location: /opt/conda/envs/eVE
#conda init
## Using base env
pip install --upgrade pip
pip install tensorflow matplotlib scikit-learn pydot
# adding VE to jupyter notebook
# https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=eVE
##others
# conda create --name env_name python==3.7.5 package_name1 package_name2
``` 


* Useful commands in the terminal
``` 
cat /etc/os-release
free -m
```

References
* https://www.youtube.com/watch?v=E2sRPvvvGPE  
* https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/setting-up-your-python-project-for-codespaces


* Configuring NVIDIA CUDA for your codespace
https://docs.github.com/en/codespaces/developing-in-codespaces/getting-started-with-github-codespaces-for-machine-learning

https://github.com/devcontainers/features/tree/main/src/nvidia-cuda


* Data science and machine learning with Codespaces - Universe 2022
https://www.youtube.com/watch?v=QbbYj56s7HU
https://github.com/tanmayeekamath/intro-to-ml


* 023/02/28/10-things-you-didnt-know-you-could-do-with-github-codespaces/
https://noise.getoto.net/2023/02/28/10-things-you-didnt-know-you-could-do-with-github-codespaces/