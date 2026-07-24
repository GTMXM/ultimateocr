
from pathlib import Path
from typing import List

from ultimateocr.data.schema import OCRAnnotation, OCRSample


class ICDAR2015Converter:

    def parse_gt_file(self, gt_path: Path) -> List[OCRAnnotation]:

        annotations = []

        with open(gt_path, "r", encoding="utf-8-sig") as f:

            for idx, line in enumerate(f):

                parts = line.strip().split(",")

                if len(parts) < 9:
                    continue

                coords = list(map(float, parts[:8]))
                text = ",".join(parts[8:]).strip()

                polygon = [
                    [coords[0], coords[1]],
                    [coords[2], coords[3]],
                    [coords[4], coords[5]],
                    [coords[6], coords[7]],
                ]

                xs = coords[0::2]
                ys = coords[1::2]

                bbox = [
                    min(xs),
                    min(ys),
                    max(xs),
                    max(ys),
                ]

                annotations.append(
                    OCRAnnotation(
                        id=idx,
                        text=text,
                        polygon=polygon,
                        bbox=bbox,
                        ignore=(text == "###"),
                    )
                )

        return annotations

    def convert(
        self,
        image_path: Path,
        gt_path: Path,
        width: int,
        height: int,
    ) -> OCRSample:

        anns = self.parse_gt_file(gt_path)

        return OCRSample(
            image_id=image_path.stem,
            image_path=str(image_path),
            width=width,
            height=height,
            annotations=anns,
        )
