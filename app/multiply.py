import torch

tensor_16 = torch.ones((1,2), dtype= torch.int16)
tensor_32 = torch.ones((1,2), dtype= torch.float16, device="cuda")
long_tensor = torch.tensor([1,2,3,4], dtype=torch.long)


print(tensor_32.dtype)
print(tensor_32.shape)
print(tensor_32.device)