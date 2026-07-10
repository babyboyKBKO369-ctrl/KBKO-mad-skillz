"""Integration tests for the entire system."""

import pytest
import pandas as pd
import numpy as np
from kbko_core.config import settings
from blackbird.analytics.engine import AnalyticsEngine
from blackbird.visualization.charts import ChartGenerator
from smokey.automation.workflow import Workflow
from smokey.scheduler.task_scheduler import TaskScheduler
from seymour_shadows.planner.planner import Planner
from seymour_shadows.simulations.simulator import Simulator


def test_end_to_end_analytics_workflow():
    """Test complete analytics workflow."""
    # Create sample data
    data = pd.DataFrame({
        "month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "sales": [100, 150, 200, 180, 250],
        "expenses": [50, 70, 80, 90, 100],
    })
    
    # Analyze
    engine = AnalyticsEngine()
    engine.load_data(data)
    stats = engine.get_summary_statistics()
    
    assert stats["shape"] == (5, 3)
    
    # Visualize
    chart = ChartGenerator.create_line_chart(
        data, "month", "sales", title="Sales Trend"
    )
    assert chart is not None


def test_end_to_end_automation_workflow():
    """Test complete automation workflow."""
    results_list = []
    
    def extract_data():
        return {"records": 1000}
    
    def transform_data():
        return {"transformed": 900}
    
    def load_data():
        return {"loaded": 900}
    
    workflow = Workflow("ETL_Pipeline")
    workflow.add_step("extract", extract_data)
    workflow.add_step("transform", transform_data)
    workflow.add_step("load", load_data)
    
    results = workflow.execute()
    
    assert results["extract"]["status"] == "success"
    assert results["transform"]["status"] == "success"
    assert results["load"]["status"] == "success"


def test_end_to_end_planning_workflow():
    """Test complete planning workflow."""
    planner = Planner()
    
    # Create plan
    plan = planner.create_plan("2024 Strategy", "Annual strategic plan")
    
    # Add objectives
    planner.add_objective(
        "2024 Strategy",
        "Increase Revenue",
        "Grow revenue by 20%",
        priority=1,
        deadline_days=365
    )
    planner.add_objective(
        "2024 Strategy",
        "Reduce Costs",
        "Reduce operational costs by 10%",
        priority=2,
        deadline_days=180
    )
    
    # Update status
    planner.update_objective_status("2024 Strategy", "Increase Revenue", "in_progress")
    
    # Verify
    plan = planner.get_plan("2024 Strategy")
    assert len(plan.objectives) == 2
    assert plan.objectives[0].status == "in_progress"


def test_end_to_end_simulation_workflow():
    """Test complete simulation workflow."""
    simulator = Simulator()
    
    def financial_model(params):
        """Simple financial model."""
        revenue = params.get("revenue", 0)
        expenses = params.get("expenses", 0)
        return {
            "profit": revenue - expenses,
            "margin": ((revenue - expenses) / revenue * 100) if revenue > 0 else 0
        }
    
    # Create scenarios
    simulator.create_scenario(
        "Conservative",
        {"revenue": 1000000, "expenses": 700000},
        "Conservative estimates"
    )
    simulator.create_scenario(
        "Optimistic",
        {"revenue": 1500000, "expenses": 700000},
        "Optimistic estimates"
    )
    
    # Run simulations
    conservative = simulator.run_simulation("Conservative", financial_model)
    optimistic = simulator.run_simulation("Optimistic", financial_model)
    
    assert conservative.success is True
    assert optimistic.success is True
    assert optimistic.output["profit"] > conservative.output["profit"]


def test_settings_accessible():
    """Test that settings are accessible across modules."""
    assert settings.api_host == "0.0.0.0"
    assert settings.api_port == 8000
    assert settings.secret_key is not None
