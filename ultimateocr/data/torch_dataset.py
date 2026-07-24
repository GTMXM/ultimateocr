
from torch.utils.data import Dataset


class OCRTorchDataset(Dataset):

    def __init__(self, samples, transform=None):
        self.samples = samples
        self.transform = transform

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):

        sample = self.samples[idx]

        if self.transform is not None:
            sample = self.transform(sample)

        return sample
