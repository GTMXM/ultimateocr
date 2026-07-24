
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional


@dataclass(slots=True)
class DatasetEntry:
    name: str
    homepage: str
    license: str
    download_url: Optional[str]
    local_path: Path
    description: str = ""


class DatasetHub:
    def __init__(self, root: Path):
        self.root = Path(root)
        self.datasets: Dict[str, DatasetEntry] = {}

    def register(self, entry: DatasetEntry):
        self.datasets[entry.name.lower()] = entry

    def get(self, name: str) -> DatasetEntry:
        return self.datasets[name.lower()]

    def exists(self, name: str) -> bool:
        return name.lower() in self.datasets

    def list(self) -> List[str]:
        return sorted(self.datasets.keys())

    def __len__(self):
        return len(self.datasets)
