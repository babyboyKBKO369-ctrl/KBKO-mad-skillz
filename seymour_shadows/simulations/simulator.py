"""Scenario simulation engine."""

from typing import Dict, List, Any, Callable, Optional
from dataclasses import dataclass
import logging
import numpy as np

logger = logging.getLogger(__name__)


@dataclass
class Scenario:
    """Represents a scenario."""

    name: str
    parameters: Dict[str, Any]
    description: Optional[str] = None


@dataclass
class SimulationResult:
    """Simulation result."""

    scenario_name: str
    success: bool
    output: Dict[str, Any]
    metrics: Dict[str, float]


class Simulator:
    """Scenario simulation engine."""

    def __init__(self):
        """Initialize simulator."""
        self.scenarios: Dict[str, Scenario] = {}
        self.results: List[SimulationResult] = []

    def create_scenario(
        self,
        name: str,
        parameters: Dict[str, Any],
        description: Optional[str] = None,
    ) -> Scenario:
        """Create a scenario.

        Args:
            name: Scenario name
            parameters: Scenario parameters
            description: Scenario description

        Returns:
            Created scenario
        """
        scenario = Scenario(name=name, parameters=parameters, description=description)
        self.scenarios[name] = scenario
        logger.info(f"Created scenario: {name}")
        return scenario

    def run_simulation(
        self,
        scenario_name: str,
        model_func: Callable,
        **kwargs
    ) -> SimulationResult:
        """Run simulation for a scenario.

        Args:
            scenario_name: Scenario name
            model_func: Model function to run
            **kwargs: Additional arguments

        Returns:
            Simulation result
        """
        if scenario_name not in self.scenarios:
            raise ValueError(f"Scenario not found: {scenario_name}")

        scenario = self.scenarios[scenario_name]
        logger.info(f"Running simulation for scenario: {scenario_name}")

        try:
            # Merge scenario parameters with kwargs
            params = {**scenario.parameters, **kwargs}
            output = model_func(params)

            # Calculate metrics
            metrics = self._calculate_metrics(output)

            result = SimulationResult(
                scenario_name=scenario_name,
                success=True,
                output=output,
                metrics=metrics,
            )
        except Exception as e:
            logger.error(f"Simulation failed for scenario {scenario_name}: {str(e)}")
            result = SimulationResult(
                scenario_name=scenario_name,
                success=False,
                output={"error": str(e)},
                metrics={},
            )

        self.results.append(result)
        return result

    def _calculate_metrics(self, output: Dict[str, Any]) -> Dict[str, float]:
        """Calculate metrics from simulation output.

        Args:
            output: Simulation output

        Returns:
            Metrics dictionary
        """
        metrics = {}
        for key, value in output.items():
            if isinstance(value, (int, float)):
                metrics[f"{key}_avg"] = float(value)
        return metrics

    def get_results(self) -> List[SimulationResult]:
        """Get all simulation results.

        Returns:
            List of results
        """
        return self.results

    def compare_scenarios(
        self, scenario_names: List[str]
    ) -> Dict[str, SimulationResult]:
        """Compare results across scenarios.

        Args:
            scenario_names: List of scenario names

        Returns:
            Dictionary of results for each scenario
        """
        comparison = {}
        for result in self.results:
            if result.scenario_name in scenario_names:
                comparison[result.scenario_name] = result
        return comparison
