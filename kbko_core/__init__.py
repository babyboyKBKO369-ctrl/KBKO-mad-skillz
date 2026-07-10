"""KBKO Core - Core infrastructure and utilities."""

__version__ = "0.1.0"
__author__ = "KBKO Team"

from kbko_core.config import settings
from kbko_core.logging import setup_logging

__all__ = ["settings", "setup_logging"]
