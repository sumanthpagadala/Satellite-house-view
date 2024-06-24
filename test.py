import torch

if torch.backends.mps.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

# Example tensor operation
x = torch.tensor([1.0, 2.0, 3.0], device=device)
print(x)