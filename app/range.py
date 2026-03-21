import torch

range_tensor = torch.arange(start=10, end=0, step= -2)



copy_range = torch.ones_like(range_tensor)


print(range_tensor)

print(copy_range)
