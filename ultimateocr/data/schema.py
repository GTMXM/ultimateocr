
from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class OCRAnnotation:
    id: int
    text: str
    polygon: List[List[float]]
    bbox: List[float]
    language: Optional[str] = None
    ignore: bool = False
    metadata: Dict = field(default_factory=dict)


@dataclass
class OCRSample:
    image_id: str
    image_path: str
    width: int
    height: int
    annotations: List[OCRAnnotation]
    metadata: Dict = field(default_factory=dict)
