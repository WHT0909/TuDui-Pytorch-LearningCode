from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

writer = SummaryWriter("./logs/P7_logs")

img_path = "../data/hymenoptera_data/train/ants/0013035.jpg"
img_data = Image.open(img_path)
img_array = np.array(img_data)

writer.add_image("test_image", img_array, dataformats='HWC')

for i in range(100):
    writer.add_scalar("y=x", i, i)

writer.close()