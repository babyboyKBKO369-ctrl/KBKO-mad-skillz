"""Tests for planning engine."""

import pytest
from datetime import datetime, timedelta
from seymour_shadows.planner.planner import Planner, Objective, Plan


@pytest.fixture
def planner():
    """Create planner instance."""
    return Planner()


def test_create_plan(planner):
    """Test plan creation."""
    plan = planner.create_plan("Q1 Plan", "Q1 planning objectives")
    assert plan is not None
    assert plan.name == "Q1 Plan"
    assert "Q1 Plan" in planner.plans


def test_add_objective(planner):
    """Test adding objective to plan."""
    planner.create_plan("Plan A", "Description A")
    obj = planner.add_objective(
        "Plan A",
        "Objective 1",
        "Description 1",
        priority=1,
        deadline_days=30
    )
    
    assert obj.name == "Objective 1"
    assert obj.priority == 1
    assert len(planner.plans["Plan A"].objectives) == 1


def test_update_objective_status(planner):
    """Test updating objective status."""
    planner.create_plan("Plan B", "Description B")
    planner.add_objective("Plan B", "Obj 1", "Desc 1")
    
    planner.update_objective_status("Plan B", "Obj 1", "in_progress")
    plan = planner.get_plan("Plan B")
    assert plan.objectives[0].status == "in_progress"


def test_get_plan(planner):
    """Test getting plan."""
    planner.create_plan("Plan C", "Description C")
    plan = planner.get_plan("Plan C")
    assert plan.name == "Plan C"


def test_get_all_plans(planner):
    """Test getting all plans."""
    planner.create_plan("Plan 1", "Desc 1")
    planner.create_plan("Plan 2", "Desc 2")
    
    plans = planner.get_all_plans()
    assert len(plans) == 2
    assert "Plan 1" in plans
    assert "Plan 2" in plans


def test_plan_not_found(planner):
    """Test error when plan not found."""
    with pytest.raises(ValueError):
        planner.add_objective("Non-existent", "Obj", "Desc")


def test_objective_not_found(planner):
    """Test error when objective not found."""
    planner.create_plan("Plan", "Desc")
    with pytest.raises(ValueError):
        planner.update_objective_status("Plan", "Non-existent", "completed")
