import torch

# how to create zero and ones tensor 

zero_tensor = torch.zeros(size=(1,3,3))

print(zero_tensor)

one_tensor = torch.ones(size=(2,2,2), dtype=torch.int32)

print(one_tensor)

print(one_tensor.dtype)