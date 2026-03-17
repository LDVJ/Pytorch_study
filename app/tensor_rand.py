import torch

# here we are creating random tensor with the numbers

# random tensor are the main building block of the systematic tensor 
random_tensor = torch.rand(3,4) # ranges from 0 -> 1
print(random_tensor)

# create the random tensor for the image type file

random_tensor2 = torch.randn(size=(3,4)) # it ranges from -infiniy to +infiniy

print(random_tensor2)

randome_image_tensor = torch.rand(3, 224,224) # height, weight, colour channel

# print(randome_image_tensor.ndim)
# print(randome_image_tensor.shape)

print(randome_image_tensor)

