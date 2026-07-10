"""Tests for analytics engine."""

import pytest
import pandas as pd
import numpy as np
from blackbird.analytics.engine import AnalyticsEngine


@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=10),
        "value1": np.random.rand(10),
        "value2": np.random.rand(10),
        "category": ["A", "B"] * 5,
    })


@pytest.fixture
def analytics_engine():
    """Create analytics engine instance."""
    return AnalyticsEngine()


def test_load_data(analytics_engine, sample_data):
    """Test loading data."""
    analytics_engine.load_data(sample_data)
    assert analytics_engine.data is not None
    assert len(analytics_engine.data) == 10


def test_summary_statistics(analytics_engine, sample_data):
    """Test summary statistics."""
    analytics_engine.load_data(sample_data)
    stats = analytics_engine.get_summary_statistics()
    assert "shape" in stats
    assert "columns" in stats
    assert stats["shape"] == (10, 4)


def test_normalize_data(analytics_engine, sample_data):
    """Test data normalization."""
    analytics_engine.load_data(sample_data)
    normalized = analytics_engine.normalize_data()
    assert normalized is not None
    assert len(normalized) == 10


def test_correlation_analysis(analytics_engine, sample_data):
    """Test correlation analysis."""
    analytics_engine.load_data(sample_data)
    corr = analytics_engine.correlation_analysis()
    assert corr is not None
    assert corr.shape[0] >= 1


def test_aggregate_data(analytics_engine, sample_data):
    """Test data aggregation."""
    analytics_engine.load_data(sample_data)
    agg = analytics_engine.aggregate_data("category", "sum")
    assert agg is not None
    assert len(agg) == 2  # Two categories


def test_no_data_loaded(analytics_engine):
    """Test error when no data loaded."""
    with pytest.raises(ValueError):
        analytics_engine.get_summary_statistics()
