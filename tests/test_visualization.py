"""Tests for visualization module."""

import pytest
import pandas as pd
from blackbird.visualization.charts import ChartGenerator


@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({
        "x": [1, 2, 3, 4, 5],
        "y": [2, 4, 6, 8, 10],
    })


def test_line_chart(sample_data):
    """Test line chart creation."""
    fig = ChartGenerator.create_line_chart(sample_data, "x", "y", title="Test")
    assert fig is not None


def test_bar_chart(sample_data):
    """Test bar chart creation."""
    fig = ChartGenerator.create_bar_chart(sample_data, "x", "y", title="Test")
    assert fig is not None


def test_scatter_plot(sample_data):
    """Test scatter plot creation."""
    fig = ChartGenerator.create_scatter_plot(sample_data, "x", "y", title="Test")
    assert fig is not None


def test_histogram(sample_data):
    """Test histogram creation."""
    fig = ChartGenerator.create_histogram(sample_data, "x", title="Test")
    assert fig is not None
