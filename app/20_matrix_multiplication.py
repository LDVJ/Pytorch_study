import torch

matrix1 = torch.tensor([[1,2,4],[4,5,6]])

matrix2 = torch.tensor([[9,8],[7,6],[5,4]])

# output = torch.matmul(matrix1, matrix2)
# print(output)
value = 0

for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        value += torch.matmul(matrix1[i], matrix2[j])

print(value)
print(len(matrix1), len(matrix2))
# print(matrix1.shape)

# print(matrix2.shape)