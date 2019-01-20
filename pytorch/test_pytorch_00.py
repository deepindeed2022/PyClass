#!/bin/python
# -*- encoding=utf-8 -*-

# include header
from __future__ import print_function
import torch

# create a tensor
x = torch.rand(5, 3)
print(x)

# test the cuda or not
print("cuda is avaliable? {}".format(torch.cuda.is_available()))
