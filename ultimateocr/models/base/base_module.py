"""
Base reusable module contract.
"""

from __future__ import annotations

from abc import abstractmethod

from .base_component import BaseComponent


class BaseModule(BaseComponent):
    """
    Root contract for reusable model modules.

    Examples:
        - Backbone
        - Neck
        - Head
        - Loss
        - PostProcess
    """

    COMPONENT_TYPE = "module"

    @abstractmethod
    def forward(self, *args, **kwargs):
        raise NotImplementedError
