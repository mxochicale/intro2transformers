# Setting up conda env 

## Conda
Install [mamba](https://github.com/mxochicale/code/tree/main/mamba) and create [...VE](ve.yml).

```
#mamba env create -f *ve.yml  
  Summary:
  Install: 177 packages
  Total download: 1GB
```


## Dependencies

* Python package versions
```
$ mamba activate *VE
$ python package_versions.py 


2023-07-16 08:13:06.596249: I tensorflow/core/util/util.cc:169] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
python: 3.10.8 | packaged by conda-forge | (main, Nov 22 2022, 08:23:14) [GCC 10.4.0]
torch: 1.11.0.post202
torch cuda_is_available: True
torch cuda version: 11.2
torch cuda.device_count  1
PIL version: 10.0.0
transformers version: 4.30.2
tensorflow version: 2.9.1

```

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
