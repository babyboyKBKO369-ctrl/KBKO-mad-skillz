"""Example usage of KBKO Mad Skillz modules."""

import pandas as pd
import numpy as np
from datetime import datetime

# Import modules
from kbko_core.logging import setup_logging
from blackbird.analytics.engine import AnalyticsEngine
from blackbird.visualization.charts import ChartGenerator
from smokey.automation.workflow import Workflow
from smokey.scheduler.task_scheduler import TaskScheduler
from seymour_shadows.planner.planner import Planner
from seymour_shadows.simulations.simulator import Simulator

# Setup logging
logger = setup_logging("examples")


def example_analytics():
    """Example: Analytics Engine Usage."""
    logger.info("=" * 50)
    logger.info("EXAMPLE: Analytics Engine")
    logger.info("=" * 50)
    
    # Create sample data
    data = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=30),
        "sales": np.random.randint(100, 1000, 30),
        "visitors": np.random.randint(500, 5000, 30),
        "region": np.random.choice(["North", "South", "East", "West"], 30),
    })
    
    # Initialize analytics engine
    engine = AnalyticsEngine()
    engine.load_data(data)
    
    # Get summary statistics
    stats = engine.get_summary_statistics()
    logger.info(f"Data shape: {stats['shape']}")
    logger.info(f"Columns: {stats['columns']}")
    
    # Perform correlation analysis
    corr = engine.correlation_analysis()
    logger.info(f"Correlation matrix:\n{corr}")
    
    # Aggregate by region
    agg = engine.aggregate_data("region", "sum")
    logger.info(f"Aggregated by region:\n{agg}")


def example_visualization():
    """Example: Visualization Usage."""
    logger.info("\n" + "=" * 50)
    logger.info("EXAMPLE: Visualization")
    logger.info("=" * 50)
    
    data = pd.DataFrame({
        "month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "revenue": [10000, 15000, 12000, 18000, 22000],
        "expenses": [5000, 6000, 5500, 7000, 8000],
    })
    
    # Create visualizations
    line_chart = ChartGenerator.create_line_chart(
        data, "month", "revenue", title="Monthly Revenue"
    )
    logger.info(f"Created line chart: {type(line_chart)}")
    
    bar_chart = ChartGenerator.create_bar_chart(
        data, "month", "expenses", title="Monthly Expenses"
    )
    logger.info(f"Created bar chart: {type(bar_chart)}")


def example_workflow():
    """Example: Workflow Automation Usage."""
    logger.info("\n" + "=" * 50)
    logger.info("EXAMPLE: Workflow Automation")
    logger.info("=" * 50)
    
    def fetch_data():
        return {"records": 5000}
    
    def process_data():
        return {"processed": 4950}
    
    def validate_data():
        return {"valid": 4900}
    
    def upload_data():
        return {"uploaded": 4900}
    
    # Create workflow
    workflow = Workflow("Data Pipeline")
    workflow.add_step("fetch", fetch_data)
    workflow.add_step("process", process_data)
    workflow.add_step("validate", validate_data)
    workflow.add_step("upload", upload_data)
    
    # Execute workflow
    results = workflow.execute()
    
    for step, result in results.items():
        logger.info(f"{step}: {result['status']} - {result.get('result', result.get('error'))}")


def example_planning():
    """Example: Planning Engine Usage."""
    logger.info("\n" + "=" * 50)
    logger.info("EXAMPLE: Planning Engine")
    logger.info("=" * 50)
    
    planner = Planner()
    
    # Create plan
    plan = planner.create_plan("Q1 2024 Goals", "First quarter objectives")
    logger.info(f"Created plan: {plan.name}")
    
    # Add objectives
    planner.add_objective(
        "Q1 2024 Goals",
        "Launch new product",
        "Release version 2.0 of our product",
        priority=1,
        deadline_days=90
    )
    planner.add_objective(
        "Q1 2024 Goals",
        "Increase user base",
        "Grow user base by 50%",
        priority=1,
        deadline_days=90
    )
    planner.add_objective(
        "Q1 2024 Goals",
        "Optimize performance",
        "Reduce response time by 40%",
        priority=2,
        deadline_days=60
    )
    
    # Get plan details
    plan = planner.get_plan("Q1 2024 Goals")
    logger.info(f"Plan has {len(plan.objectives)} objectives")
    for obj in plan.objectives:
        logger.info(f"  - {obj.name} (Priority: {obj.priority})")


def example_simulation():
    """Example: Simulation Engine Usage."""
    logger.info("\n" + "=" * 50)
    logger.info("EXAMPLE: Simulation Engine")
    logger.info("=" * 50)
    
    simulator = Simulator()
    
    def revenue_model(params):
        """Financial model."""
        units_sold = params.get("units_sold", 0)
        price_per_unit = params.get("price_per_unit", 0)
        fixed_costs = params.get("fixed_costs", 0)
        
        revenue = units_sold * price_per_unit
        profit = revenue - fixed_costs
        
        return {
            "revenue": revenue,
            "profit": profit,
            "profit_margin": (profit / revenue * 100) if revenue > 0 else 0
        }
    
    # Create scenarios
    scenarios = [
        ("Conservative", {"units_sold": 1000, "price_per_unit": 100, "fixed_costs": 50000}),
        ("Normal", {"units_sold": 2000, "price_per_unit": 100, "fixed_costs": 50000}),
        ("Optimistic", {"units_sold": 3000, "price_per_unit": 100, "fixed_costs": 50000}),
    ]
    
    for name, params in scenarios:
        simulator.create_scenario(name, params)
        result = simulator.run_simulation(name, revenue_model)
        logger.info(f"{name}: Revenue=${result.output['revenue']:,.0f}, Profit=${result.output['profit']:,.0f}")


if __name__ == "__main__":
    logger.info("\n" + "*" * 50)
    logger.info("KBKO Mad Skillz - Examples")
    logger.info("*" * 50)
    
    example_analytics()
    example_visualization()
    example_workflow()
    example_planning()
    example_simulation()
    
    logger.info("\n" + "*" * 50)
    logger.info("All examples completed!")
    logger.info("*" * 50)
