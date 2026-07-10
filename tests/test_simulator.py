"""Tests for simulation engine."""

import pytest
from seymour_shadows.simulations.simulator import Simulator, Scenario


@pytest.fixture
def simulator():
    """Create simulator instance."""
    return Simulator()


def test_create_scenario(simulator):
    """Test scenario creation."""
    params = {"x": 10, "y": 20}
    scenario = simulator.create_scenario("Scenario 1", params, "Test scenario")
    
    assert scenario.name == "Scenario 1"
    assert scenario.parameters == params
    assert "Scenario 1" in simulator.scenarios


def test_run_simulation(simulator):
    """Test running simulation."""
    def simple_model(params):
        return {"result": params["x"] + params["y"]}
    
    simulator.create_scenario("Sim 1", {"x": 5, "y": 10})
    result = simulator.run_simulation("Sim 1", simple_model)
    
    assert result.success is True
    assert result.scenario_name == "Sim 1"
    assert result.output["result"] == 15


def test_simulation_with_kwargs(simulator):
    """Test simulation with additional kwargs."""
    def model_with_params(params):
        return {"result": params.get("x", 0) + params.get("y", 0) + params.get("z", 0)}
    
    simulator.create_scenario("Sim 2", {"x": 5, "y": 10})
    result = simulator.run_simulation("Sim 2", model_with_params, z=15)
    
    assert result.success is True
    assert result.output["result"] == 30


def test_simulation_failure(simulator):
    """Test handling simulation failure."""
    def failing_model(params):
        raise RuntimeError("Model error")
    
    simulator.create_scenario("Sim 3", {"x": 1})
    result = simulator.run_simulation("Sim 3", failing_model)
    
    assert result.success is False
    assert "error" in result.output


def test_get_results(simulator):
    """Test getting results."""
    def model(params):
        return {"result": params["x"]}
    
    simulator.create_scenario("Sim 4", {"x": 100})
    simulator.run_simulation("Sim 4", model)
    
    results = simulator.get_results()
    assert len(results) == 1
    assert results[0].scenario_name == "Sim 4"


def test_compare_scenarios(simulator):
    """Test scenario comparison."""
    def model(params):
        return {"result": params["x"] * 2}
    
    simulator.create_scenario("Compare 1", {"x": 10})
    simulator.create_scenario("Compare 2", {"x": 20})
    
    simulator.run_simulation("Compare 1", model)
    simulator.run_simulation("Compare 2", model)
    
    comparison = simulator.compare_scenarios(["Compare 1", "Compare 2"])
    assert len(comparison) == 2
    assert "Compare 1" in comparison
    assert "Compare 2" in comparison


def test_scenario_not_found(simulator):
    """Test error when scenario not found."""
    def model(params):
        return {}
    
    with pytest.raises(ValueError):
        simulator.run_simulation("Non-existent", model)
