
import json
from pathlib import Path

from .experiment import Experiment


class ExperimentManager:

    def __init__(self, root):

        self.root = Path(root)

        self.root.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(self, experiment: Experiment):

        path = self.root / f"{experiment.id}.json"

        with open(path, "w", encoding="utf-8") as f:

            json.dump(
                experiment.__dict__,
                f,
                indent=4,
                ensure_ascii=False
            )

        return path
