"""Chart and visualization generator."""

import pandas as pd
from typing import Optional, Dict, Any
import plotly.express as px
import plotly.graph_objects as go


class ChartGenerator:
    """Generate interactive charts and visualizations."""

    @staticmethod
    def create_line_chart(
        data: pd.DataFrame,
        x: str,
        y: str,
        title: Optional[str] = None,
        **kwargs
    ) -> go.Figure:
        """Create line chart.

        Args:
            data: DataFrame with data
            x: X-axis column
            y: Y-axis column
            title: Chart title
            **kwargs: Additional plotly arguments

        Returns:
            Plotly figure
        """
        return px.line(data, x=x, y=y, title=title, **kwargs)

    @staticmethod
    def create_bar_chart(
        data: pd.DataFrame,
        x: str,
        y: str,
        title: Optional[str] = None,
        **kwargs
    ) -> go.Figure:
        """Create bar chart.

        Args:
            data: DataFrame with data
            x: X-axis column
            y: Y-axis column
            title: Chart title
            **kwargs: Additional plotly arguments

        Returns:
            Plotly figure
        """
        return px.bar(data, x=x, y=y, title=title, **kwargs)

    @staticmethod
    def create_scatter_plot(
        data: pd.DataFrame,
        x: str,
        y: str,
        title: Optional[str] = None,
        color: Optional[str] = None,
        size: Optional[str] = None,
        **kwargs
    ) -> go.Figure:
        """Create scatter plot.

        Args:
            data: DataFrame with data
            x: X-axis column
            y: Y-axis column
            title: Chart title
            color: Color column
            size: Size column
            **kwargs: Additional plotly arguments

        Returns:
            Plotly figure
        """
        return px.scatter(data, x=x, y=y, title=title, color=color, size=size, **kwargs)

    @staticmethod
    def create_histogram(
        data: pd.DataFrame,
        x: str,
        title: Optional[str] = None,
        nbins: int = 30,
        **kwargs
    ) -> go.Figure:
        """Create histogram.

        Args:
            data: DataFrame with data
            x: Column to plot
            title: Chart title
            nbins: Number of bins
            **kwargs: Additional plotly arguments

        Returns:
            Plotly figure
        """
        return px.histogram(data, x=x, title=title, nbins=nbins, **kwargs)
