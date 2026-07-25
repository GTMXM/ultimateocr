"""
Base component contract.
"""

from __future__ import annotations

from abc import ABC
from typing import Any

import torch.nn as nn

from ultimateocr.models.common import ComponentType


class BaseComponent(nn.Module, ABC):
    """
    Root class for every reusable UltimateOCR component.
    """

    COMPONENT_TYPE = ComponentType.MODULE

    def __init__(self) -> None:
        super().__init__()

    @property
    def component_type(self) -> ComponentType:
        return self.COMPONENT_TYPE

    def get_config(self) -> dict[str, Any]:
        return {}
