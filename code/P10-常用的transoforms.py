from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from  torchvision import transforms

img = Image.open("../data/hymenoptera_data/train/ants/0013035.jpg")
trans_to_tensor = transforms.ToTensor()
img_tensor = trans_to_tensor(img)
writer = SummaryWriter(log_dir="./logs/P10_logs")
writer.add_image(tag="img_tensor", img_tensor=img_tensor)
trans_normalize = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
img_norm_tensor = trans_normalize(img_tensor)
writer.add_image(tag="img_normalize_tensor", img_tensor=img_norm_tensor)
trans_resize = transforms.Resize((512, 512))
img_resize = trans_resize(img_tensor)
writer.add_image(tag="img_resize_tensor", img_tensor=img_resize)
writer.close()