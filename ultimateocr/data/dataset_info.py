
from dataclasses import dataclass


@dataclass
class DatasetInfo:

    name: str

    url: str

    filename: str

    task: str

    description: str
