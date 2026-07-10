"""Tests for kbko_core module."""

import pytest
from kbko_core.config import settings
from kbko_core.logging import setup_logging


def test_settings_load():
    """Test settings are loaded."""
    assert settings is not None
    assert settings.api_host == "0.0.0.0"
    assert settings.api_port == 8000


def test_setup_logging():
    """Test logging setup."""
    logger = setup_logging("test")
    assert logger is not None
    assert logger.name == "test"
