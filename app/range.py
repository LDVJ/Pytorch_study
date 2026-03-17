import torch

# range_tensor = torch.arange(start=10, end=0, step= -2)

normal_tensor = torch.rand(size=(3,4), dtype=torch.int32)

# copy_range = torch.ones_like(range_tensor)

new_tensor = torch.rand_like(normal_tensor, dtype=torch.int32)

# print(range_tensor)

# print(copy_range)

print(normal_tensor)

print(new_tensor)