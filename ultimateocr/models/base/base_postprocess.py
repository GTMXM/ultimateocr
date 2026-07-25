"""
BasePostProcess contract.
"""

from .base_module import BaseModule


class BasePostProcess(BaseModule):
    """
    Base interface for postprocess.
    """

    COMPONENT_TYPE = "postprocess"
