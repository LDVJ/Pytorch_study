import torch


float_tensor = torch.randn(size=(2,3,4), dtype=torch.float32)

like = torch.rand_like(float_tensor)

print(float_tensor)

print(like)