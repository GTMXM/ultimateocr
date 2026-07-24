
from pathlib import Path
from typing import List


class DatasetValidator:

    def __init__(self):
        self.errors = []

    def validate_image_exists(self, image_path):

        image_path = Path(image_path)

        if not image_path.exists():

            self.errors.append(
                f"Missing image: {image_path}"
            )

    def validate_bbox(self, bbox, width, height):

        if len(bbox) != 4:

            self.errors.append(
                f"Invalid bbox length: {bbox}"
            )

            return

        x1, y1, x2, y2 = bbox

        if x1 < 0 or y1 < 0:

            self.errors.append(
                f"Negative bbox: {bbox}"
            )

        if x2 > width or y2 > height:

            self.errors.append(
                f"BBox outside image: {bbox}"
            )

        if x2 <= x1 or y2 <= y1:

            self.errors.append(
                f"Invalid bbox geometry: {bbox}"
            )

    def validate_text(self, text):

        if text is None:

            self.errors.append(
                "Text is None"
            )

            return

        if len(text.strip()) == 0:

            self.errors.append(
                "Empty text"
            )

    def has_errors(self):

        return len(self.errors) > 0

    def report(self) -> List[str]:

        return self.errors
