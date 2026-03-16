import torch

scalar = torch.tensor(7)

vector = torch.tensor([1,2])

MATRIX = torch.tensor([[1,2],[3,4]])

TENSOR = torch.tensor([[[1,2,3],[4,5,6],[7,8,9]],[[9,8,7],[6,5,4],[3,2,1]]])

# basic scalr based functions
print(scalar)
print(scalar.item())
print(scalar.ndim)
print(scalar.shape)

# vector basic functions
print(vector)
print(vector.ndim)
print(vector.shape)

# MATRIX basic functions
print(MATRIX)
print(MATRIX.ndim)
print(MATRIX.shape)

#TENSOR basic functions
print(TENSOR)
print(TENSOR.ndim)
print(TENSOR.shape)