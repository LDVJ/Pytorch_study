import torch

float_tensor = torch.tensor([1,2.0,3.1230],
                            dtype=torch.int16,
                            device=None,
                            requires_grad=False)

# NOTE tensors datatypes is one of the big three problems with pytorch or deep learning

print(float_tensor)