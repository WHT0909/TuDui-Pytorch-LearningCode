import torchvision

train_set = torchvision.datasets.CIFAR10(root="../data", train=True, download=False)
test_set = torchvision.datasets.CIFAR10(root="../data", train=False, download=False)

print(train_set[0])