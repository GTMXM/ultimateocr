"""
Component type definitions for UltimateOCR.
"""

from __future__ import annotations

from enum import Enum


class ComponentType(str, Enum):
    MODEL = "model"
    MODULE = "module"

    BACKBONE = "backbone"
    NECK = "neck"
    HEAD = "head"

    LOSS = "loss"
    POSTPROCESS = "postprocess"

    DETECTION = "detection"
    RECOGNITION = "recognition"
    LAYOUT = "layout"
    LANGUAGE = "language"
