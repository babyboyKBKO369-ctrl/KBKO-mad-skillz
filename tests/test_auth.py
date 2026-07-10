"""Tests for authentication module."""

import pytest
from kbko_core.auth.jwt_handler import create_access_token, verify_token
from kbko_core.auth.password import hash_password, verify_password


def test_create_access_token():
    """Test JWT token creation."""
    token = create_access_token({"sub": "test_user"})
    assert isinstance(token, str)
    assert len(token) > 0


def test_verify_token():
    """Test JWT token verification."""
    data = {"sub": "test_user", "email": "test@example.com"}
    token = create_access_token(data)
    payload = verify_token(token)
    assert payload["sub"] == "test_user"
    assert payload["email"] == "test@example.com"


def test_verify_invalid_token():
    """Test verification of invalid token."""
    with pytest.raises(ValueError):
        verify_token("invalid_token")


def test_hash_password():
    """Test password hashing."""
    password = "test_password_123"
    hashed = hash_password(password)
    assert hashed != password
    assert len(hashed) > 0


def test_verify_password():
    """Test password verification."""
    password = "test_password_123"
    hashed = hash_password(password)
    assert verify_password(password, hashed) is True
    assert verify_password("wrong_password", hashed) is False
