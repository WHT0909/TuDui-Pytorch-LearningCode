from torch.utils.data import Dataset
from PIL import Image
import os

class MyData(Dataset):
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.data_path = os.path.join(self.root_dir, self.label_dir)
        self.img_list = os.listdir(self.data_path)

    def __getitem__(self, idx):
        img_name = self.img_list[idx]
        img_path = os.path.join(self.data_path, img_name)
        img = Image.open(img_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_list)

img_dataset = MyData(root_dir="../data/hymenoptera_data/train", label_dir="ants")
img, label = img_dataset[0]
# print(img, label)
img.show()