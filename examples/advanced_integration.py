"""Advanced integration example."""

import pandas as pd
import numpy as np
from datetime import datetime

from kbko_core.logging import setup_logging
from kbko_core.auth.jwt_handler import create_access_token, verify_token
from blackbird.analytics.engine import AnalyticsEngine
from smokey.automation.workflow import Workflow
from seymour_shadows.simulations.simulator import Simulator

logger = setup_logging("advanced_example")


def advanced_business_intelligence():
    """Advanced BI workflow combining multiple modules."""
    logger.info("Starting Advanced Business Intelligence Workflow")
    
    # 1. Create sample sales data
    data = pd.DataFrame({
        "quarter": ["Q1", "Q2", "Q3", "Q4"],
        "product_a_sales": [100000, 120000, 135000, 150000],
        "product_b_sales": [80000, 90000, 100000, 110000],
        "marketing_spend": [10000, 12000, 15000, 18000],
        "operating_costs": [50000, 55000, 60000, 65000],
    })
    
    # 2. Analyze the data
    logger.info("\n=== ANALYTICS PHASE ===")
    engine = AnalyticsEngine()
    engine.load_data(data)
    
    stats = engine.get_summary_statistics()
    logger.info(f"Data loaded: {stats['shape'][0]} quarters, {stats['shape'][1]} metrics")
    
    # Calculate correlations
    data_numeric = data.select_dtypes(include=[np.number])
    correlations = data_numeric.corr()
    logger.info(f"Correlation between Product A and B sales:\n{correlations.loc['product_a_sales', 'product_b_sales']:.3f}")
    
    # 3. Automation workflow for data processing
    logger.info("\n=== AUTOMATION PHASE ===")
    
    def validate_data():
        return {"valid_records": data.shape[0], "validation_errors": 0}
    
    def aggregate_metrics():
        total_sales = data["product_a_sales"].sum() + data["product_b_sales"].sum()
        total_costs = data["marketing_spend"].sum() + data["operating_costs"].sum()
        return {
            "total_sales": total_sales,
            "total_costs": total_costs,
            "profit": total_sales - total_costs
        }
    
    def generate_report():
        return {"report_file": "quarterly_report.pdf", "pages": 10}
    
    workflow = Workflow("Business_Report_Pipeline")
    workflow.add_step("validate", validate_data)
    workflow.add_step("aggregate", aggregate_metrics)
    workflow.add_step("report", generate_report)
    
    results = workflow.execute()
    
    for step, result in results.items():
        if result["status"] == "success":
            logger.info(f"✓ {step}: {result['result']}")
    
    # 4. Run scenario simulations
    logger.info("\n=== SIMULATION PHASE ===")
    
    simulator = Simulator()
    
    def forecast_model(params):
        """Forecast model based on growth rates."""
        base_sales = params.get("base_sales", 0)
        growth_rate = params.get("growth_rate", 0.1)
        years = params.get("years", 3)
        
        projections = {}
        current = base_sales
        for year in range(1, years + 1):
            current = current * (1 + growth_rate)
            projections[f"year_{year}"] = current
        
        return projections
    
    scenarios = [
        ("Pessimistic", {"base_sales": 450000, "growth_rate": 0.05, "years": 3}),
        ("Base Case", {"base_sales": 450000, "growth_rate": 0.10, "years": 3}),
        ("Optimistic", {"base_sales": 450000, "growth_rate": 0.15, "years": 3}),
    ]
    
    for scenario_name, params in scenarios:
        simulator.create_scenario(scenario_name, params)
        result = simulator.run_simulation(scenario_name, forecast_model)
        logger.info(f"{scenario_name}: Year 3 Projection = ${result.output.get('year_3', 0):,.0f}")
    
    logger.info("\n=== WORKFLOW COMPLETED ===")


if __name__ == "__main__":
    advanced_business_intelligence()
