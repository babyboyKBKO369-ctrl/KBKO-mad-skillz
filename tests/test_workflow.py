"""Tests for workflow automation."""

import pytest
from smokey.automation.workflow import Workflow


@pytest.fixture
def workflow():
    """Create workflow instance."""
    return Workflow("test_workflow")


def test_workflow_creation(workflow):
    """Test workflow creation."""
    assert workflow.name == "test_workflow"
    assert len(workflow.steps) == 0


def test_add_step(workflow):
    """Test adding step to workflow."""
    def step_func():
        return "step_result"
    
    workflow.add_step("step_1", step_func)
    assert len(workflow.steps) == 1
    assert workflow.steps[0].name == "step_1"


def test_workflow_chaining(workflow):
    """Test method chaining."""
    def step_func():
        return "result"
    
    result = (workflow
        .add_step("step_1", step_func)
        .add_step("step_2", step_func)
        .add_step("step_3", step_func))
    
    assert result is workflow
    assert len(workflow.steps) == 3


def test_workflow_execution(workflow):
    """Test workflow execution."""
    def step1():
        return 10
    
    def step2():
        return 20
    
    workflow.add_step("calc_1", step1)
    workflow.add_step("calc_2", step2)
    
    results = workflow.execute()
    assert "calc_1" in results
    assert "calc_2" in results
    assert results["calc_1"]["status"] == "success"
    assert results["calc_1"]["result"] == 10


def test_workflow_with_args(workflow):
    """Test workflow with arguments."""
    def add_numbers(a, b):
        return a + b
    
    workflow.add_step("add", add_numbers, args=(5, 3))
    results = workflow.execute()
    
    assert results["add"]["status"] == "success"
    assert results["add"]["result"] == 8


def test_workflow_with_kwargs(workflow):
    """Test workflow with keyword arguments."""
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    workflow.add_step("greet", greet, kwargs={"name": "World", "greeting": "Hi"})
    results = workflow.execute()
    
    assert results["greet"]["status"] == "success"
    assert results["greet"]["result"] == "Hi, World!"


def test_workflow_error_handling(workflow):
    """Test workflow error handling."""
    def failing_step():
        raise ValueError("Step failed")
    
    workflow.add_step("fail", failing_step)
    results = workflow.execute()
    
    assert results["fail"]["status"] == "failed"
    assert "error" in results["fail"]
