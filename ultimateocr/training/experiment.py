
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict


@dataclass
class Experiment:

    id: str

    name: str

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    config: Dict = field(default_factory=dict)

    metrics: Dict = field(default_factory=dict)

    notes: str = ""
