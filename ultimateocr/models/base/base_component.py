"""
Base component contract.
"""

from __future__ import annotations

from abc import ABC
from typing import Any

import torch.nn as nn

from ultimateocr.models.common import ComponentInfo, ComponentType


class BaseComponent(nn.Module, ABC):
    """
    Root class for every reusable UltimateOCR component.
    """

    COMPONENT_TYPE = ComponentType.MODULE

    PROVIDER = "ultimateocr"

    VERSION = "0.1.0"

    EXPERIMENTAL = False

    def __init__(self) -> None:
        super().__init__()

    @property
    def component_type(self) -> ComponentType:
        return self.COMPONENT_TYPE

    @property
    def component_info(self) -> ComponentInfo:
        return ComponentInfo(
            name=self.__class__.__name__,
            component_type=self.COMPONENT_TYPE,
            provider=self.PROVIDER,
            version=self.VERSION,
            experimental=self.EXPERIMENTAL,
        )

    def get_config(self) -> dict[str, Any]:
        return {}
