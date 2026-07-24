
import cv2


class LoadImage:

    def __call__(self, sample):

        image = cv2.imread(sample.image_path)

        if image is None:
            raise FileNotFoundError(sample.image_path)

        sample.metadata["image"] = image

        return sample


class Compose:

    def __init__(self, transforms):
        self.transforms = transforms

    def __call__(self, sample):

        for t in self.transforms:
            sample = t(sample)

        return sample
