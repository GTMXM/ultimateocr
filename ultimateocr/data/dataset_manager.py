
from pathlib import Path


class DatasetManager:

    def __init__(self, root):

        self.root = Path(root)

        self.raw = self.root / "raw"

        self.processed = self.root / "processed"

        self.synthetic = self.root / "synthetic"

        self.benchmarks = self.root / "benchmarks"

    def info(self):

        return {

            "raw": self.raw,

            "processed": self.processed,

            "synthetic": self.synthetic,

            "benchmarks": self.benchmarks

        }
