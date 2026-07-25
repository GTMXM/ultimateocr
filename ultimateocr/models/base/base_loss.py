"""
BaseLoss contract.
"""

from .base_module import BaseModule


class BaseLoss(BaseModule):
    """
    Base interface for loss.
    """

    COMPONENT_TYPE = "loss"
