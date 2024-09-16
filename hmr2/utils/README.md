# Report for vitpose-h.pth

## Overview

This `.pth` file contains 2 keys:

- **meta**: type = <class 'dict'>
  - Dictionary with 5 keys
    - **env_info**: type = <class 'str'>
      - Value: sys.platform: linux
Python: 3.8.10 | packaged by conda-forge | (default, May 11 2021, 07:01:05) [GCC 9.3.0]
CUDA available: True
GPU 0,1,2,3,4,5,6,7: A100-SXM4-40GB
CUDA_HOME: /usr/local/cuda
NVCC: Build cuda_11.3.r11.3/compiler.29920130_0
GCC: gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
PyTorch: 1.9.0a0+c3d40fd
PyTorch compiling details: PyTorch built with:
  - GCC 9.3
  - C++ Version: 201402
  - Intel(R) Math Kernel Library Version 2019.0.5 Product Build 20190808 for Intel(R) 64 architecture applications
  - Intel(R) MKL-DNN v2.1.2 (Git Hash N/A)
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - NNPACK is enabled
  - CPU capability usage: AVX2
  - CUDA Runtime 11.3
  - NVCC architecture flags: -gencode;arch=compute_52,code=sm_52;-gencode;arch=compute_60,code=sm_60;-gencode;arch=compute_61,code=sm_61;-gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_80,code=sm_80;-gencode;arch=compute_86,code=sm_86;-gencode;arch=compute_86,code=compute_86
  - CuDNN 8.2.1
  - Magma 2.5.2
  - Build settings: BLAS_INFO=mkl, BUILD_TYPE=Release, CUDA_VERSION=11.3, CUDNN_VERSION=8.2.1, CXX_COMPILER=/usr/bin/c++, CXX_FLAGS= -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -fopenmp -DNDEBUG -DUSE_KINETO -DUSE_FBGEMM -DUSE_QNNPACK -DUSE_PYTORCH_QNNPACK -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -Wno-narrowing -Wall -Wextra -Werror=return-type -Wno-missing-field-initializers -Wno-type-limits -Wno-array-bounds -Wno-unknown-pragmas -Wno-sign-compare -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function -Wno-unused-result -Wno-unused-local-typedefs -Wno-strict-overflow -Wno-strict-aliasing -Wno-error=deprecated-declarations -Wno-stringop-overflow -Wno-psabi -Wno-error=pedantic -Wno-error=redundant-decls -Wno-error=old-style-cast -fdiagnostics-color=always -faligned-new -Wno-unused-but-set-variable -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Werror=cast-function-type -Wno-stringop-overflow, LAPACK_INFO=mkl, PERF_WITH_AVX=1, PERF_WITH_AVX2=1, PERF_WITH_AVX512=1, TORCH_VERSION=1.9.0, USE_CUDA=ON, USE_CUDNN=ON, USE_EXCEPTION_PTR=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_MKL=ON, USE_MKLDNN=ON, USE_MPI=ON, USE_NCCL=ON, USE_NNPACK=ON, USE_OPENMP=ON, 

TorchVision: 0.10.0a0
OpenCV: 4.5.5
MMCV: 1.3.9
MMCV Compiler: GCC 9.3
MMCV CUDA Compiler: 11.3
MMPose: 0.24.0+1041e5c
    - **seed**: type = <class 'int'>
      - Value: 0
    - **epoch**: type = <class 'int'>
      - Value: 180
    - **mmcv_version**: type = <class 'str'>
      - Value: 1.3.9
    - **time**: type = <class 'str'>
      - Value: Mon Apr 18 16:38:01 2022

- **state_dict**: type = <class 'collections.OrderedDict'>
  - Dictionary with 403 keys
    - **backbone.pos_embed**: type = <class 'torch.Tensor'>
      - Tensor shape: torch.Size([1, 193, 1280]), dtype = torch.float32
      - First 5 values: [0.0006491369567811489, 0.00040386331966146827, 1.546663224871736e-05, -0.00016539501666557044, -0.0005236031720414758]
    - **backbone.patch_embed.proj.weight**: type = <class 'torch.Tensor'>
      - Tensor shape: torch.Size([1280, 3, 16, 16]), dtype = torch.float32
      - First 5 values: [-2.3768940081936307e-05, -6.476656562881544e-05, -3.148649193462916e-05, -3.0773029720876366e-05, -2.8439346351660788e-05]
    - **backbone.patch_embed.proj.bias**: type = <class 'torch.Tensor'>
      - Tensor shape: torch.Size([1280]), dtype = torch.float32
      - First 5 values: [0.5955566167831421, 0.4470837414264679, 0.7077800631523132, 0.41051119565963745, 0.5218484401702881]
    - **backbone.blocks.0.norm1.weight**: type = <class 'torch.Tensor'>
      - Tensor shape: torch.Size([1280]), dtype = torch.float32
      - First 5 values: [0.04105346277356148, -0.0005369296995922923, -0.0001310460502281785, 0.05795266106724739, -0.0012485551415011287]
    - **backbone.blocks.0.norm1.bias**: type = <class 'torch.Tensor'>
      - Tensor shape: torch.Size([1280]), dtype = torch.float32
      - First 5 values: [-0.0007582535617984831, 0.0001669410994509235, -0.00014944651047699153, 0.00742484163492918, 0.00021594029385596514]

