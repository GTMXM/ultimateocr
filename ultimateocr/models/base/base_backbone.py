"""
BaseBackbone contract.
"""

from .base_module import BaseModule


class BaseBackbone(BaseModule):
    """
    Base interface for backbone.
    """

    COMPONENT_TYPE = "backbone"
