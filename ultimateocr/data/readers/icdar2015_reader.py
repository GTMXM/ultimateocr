
from pathlib import Path
from typing import List

import cv2

from ultimateocr.data.converters import ICDAR2015Converter
from ultimateocr.data.schema import OCRSample


class ICDAR2015Reader:

    def __init__(self):
        self.converter = ICDAR2015Converter()

    def load(
        self,
        image_dir: Path,
        gt_dir: Path,
    ) -> List[OCRSample]:

        samples = []

        image_files = sorted(image_dir.glob("*"))

        for image_path in image_files:

            if image_path.suffix.lower() not in [
                ".jpg",
                ".jpeg",
                ".png",
                ".bmp",
            ]:
                continue

            gt_path = gt_dir / f"gt_{image_path.stem}.txt"

            if not gt_path.exists():
                continue

            image = cv2.imread(str(image_path))

            if image is None:
                continue

            h, w = image.shape[:2]

            sample = self.converter.convert(
                image_path=image_path,
                gt_path=gt_path,
                width=w,
                height=h,
            )

            samples.append(sample)

        return samples
