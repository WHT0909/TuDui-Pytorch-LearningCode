from torchvision import transforms
from PIL import Image

img_path = "../data/hymenoptera_data/train/ants/0013035.jpg"
img = Image.open(img_path)

tensor_trans = transforms.ToTensor()
img_tensor = tensor_trans(img)
print(img_tensor)