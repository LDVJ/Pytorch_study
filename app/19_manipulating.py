import torch

# some_tensor = torch.randint(high=10, size=[2,3])
some_tensor = torch.tensor([[1,2,3],[4,5,6]])

# print(some_tensor)

# print("Addition: ",some_tensor + 10)
# print("Subtraction: ",some_tensor - 10)
# print("Multiplication: ",some_tensor * 10)
# print("Division: ",some_tensor / 10)


# print(torch.add(some_tensor, 10))
# # print(torch.add(some_tensor, 10))
# print(torch.sub(some_tensor, 10))
# print(torch.subtract(some_tensor, 10))
# print(torch.mul(some_tensor, 10))
# print(torch.multiply(some_tensor, 10))
# print(torch.div(some_tensor, 10))
# print(torch.divide(some_tensor, 10))

# some_tensor.add_(10)
print(some_tensor.add_(10))
# print(some_tensor.div(10))

print(some_tensor)
