"""
Base component contract.

Every reusable model component in UltimateOCR derives from
BaseComponent.
"""

from __future__ import annotations

from abc import ABC
from typing import Any

import torch.nn as nn


class BaseComponent(nn.Module, ABC):
    """
    Root class for reusable UltimateOCR components.
    """

    COMPONENT_TYPE = "component"

    def __init__(self) -> None:
        super().__init__()

    @property
    def component_type(self) -> str:
        return self.COMPONENT_TYPE

    def get_config(self) -> dict[str, Any]:
        """
        Return a serializable configuration dictionary.
        """
        return {}
