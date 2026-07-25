"""
Base interfaces for UltimateOCR.
"""

from .base_component import BaseComponent as BaseComponent
from .base_module import BaseModule as BaseModule
from .base_model import BaseModel as BaseModel

from .base_backbone import BaseBackbone as BaseBackbone
from .base_neck import BaseNeck as BaseNeck
from .base_head import BaseHead as BaseHead
from .base_loss import BaseLoss as BaseLoss
from .base_postprocess import BasePostProcess as BasePostProcess

__all__ = [
    "BaseComponent",
    "BaseModule",
    "BaseModel",
    "BaseBackbone",
    "BaseNeck",
    "BaseHead",
    "BaseLoss",
    "BasePostProcess",
]
