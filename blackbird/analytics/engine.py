"""Analytics processing engine."""

import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional
from sklearn.preprocessing import StandardScaler


class AnalyticsEngine:
    """Main analytics engine for data processing."""

    def __init__(self):
        """Initialize analytics engine."""
        self.scaler = StandardScaler()
        self.data: Optional[pd.DataFrame] = None

    def load_data(self, data: pd.DataFrame) -> None:
        """Load data for analysis.

        Args:
            data: DataFrame to load
        """
        self.data = data.copy()

    def get_summary_statistics(self) -> Dict[str, Any]:
        """Get summary statistics of the data.

        Returns:
            Dictionary with summary statistics
        """
        if self.data is None:
            raise ValueError("No data loaded. Call load_data() first.")

        return {
            "shape": self.data.shape,
            "columns": list(self.data.columns),
            "dtypes": self.data.dtypes.to_dict(),
            "null_counts": self.data.isnull().sum().to_dict(),
            "statistics": self.data.describe().to_dict(),
        }

    def normalize_data(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """Normalize data using StandardScaler.

        Args:
            columns: Columns to normalize. If None, normalize all numeric columns.

        Returns:
            Normalized DataFrame
        """
        if self.data is None:
            raise ValueError("No data loaded. Call load_data() first.")

        data = self.data.copy()
        numeric_cols = columns or data.select_dtypes(include=[np.number]).columns.tolist()

        data[numeric_cols] = self.scaler.fit_transform(data[numeric_cols])
        return data

    def correlation_analysis(self) -> pd.DataFrame:
        """Perform correlation analysis.

        Returns:
            Correlation matrix
        """
        if self.data is None:
            raise ValueError("No data loaded. Call load_data() first.")

        numeric_data = self.data.select_dtypes(include=[np.number])
        return numeric_data.corr()

    def aggregate_data(self, group_by: str, agg_func: str = "sum") -> pd.DataFrame:
        """Aggregate data by grouping.

        Args:
            group_by: Column to group by
            agg_func: Aggregation function (sum, mean, count, etc.)

        Returns:
            Aggregated DataFrame
        """
        if self.data is None:
            raise ValueError("No data loaded. Call load_data() first.")

        return self.data.groupby(group_by).agg(agg_func)
