import torch

one_to_ten = torch.arange(start=10, end=100, step=5)

range_copy_ones = torch.ones_like(one_to_ten)

range_copy_zero = torch.zeros_like(one_to_ten)

print("one_to_ten",one_to_ten)
print("range_copy_ones", range_copy_ones)
print("range_copy_zero", range_copy_zero)
