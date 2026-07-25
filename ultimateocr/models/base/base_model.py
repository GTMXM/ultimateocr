"""
Base model contract.

All trainable OCR models derive from BaseModel.
"""

from __future__ import annotations

from abc import abstractmethod

from .base_component import BaseComponent


class BaseModel(BaseComponent):
    """
    Root class for complete OCR models.
    """

    COMPONENT_TYPE = "model"

    @abstractmethod
    def forward(self, *args, **kwargs):
        """
        Execute a forward pass.
        """
        raise NotImplementedError
