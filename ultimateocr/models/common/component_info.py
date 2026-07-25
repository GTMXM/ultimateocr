"""
Component metadata definitions.
"""

from __future__ import annotations

from dataclasses import dataclass

from .component_type import ComponentType


@dataclass(frozen=True, slots=True)
class ComponentInfo:
    """
    Immutable metadata describing an UltimateOCR component.
    """

    name: str
    component_type: ComponentType

    provider: str = "ultimateocr"
    version: str = "0.1.0"

    experimental: bool = False
