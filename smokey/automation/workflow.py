"""Workflow automation engine."""

from typing import Callable, List, Dict, Any, Optional
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class WorkflowStep:
    """Represents a workflow step."""

    name: str
    func: Callable
    args: tuple = ()
    kwargs: Dict[str, Any] = None

    def __post_init__(self):
        if self.kwargs is None:
            self.kwargs = {}


class Workflow:
    """Workflow automation engine."""

    def __init__(self, name: str):
        """Initialize workflow.

        Args:
            name: Workflow name
        """
        self.name = name
        self.steps: List[WorkflowStep] = []
        self.results: Dict[str, Any] = {}

    def add_step(
        self,
        name: str,
        func: Callable,
        args: tuple = (),
        kwargs: Optional[Dict[str, Any]] = None,
    ) -> "Workflow":
        """Add step to workflow.

        Args:
            name: Step name
            func: Step function
            args: Function arguments
            kwargs: Function keyword arguments

        Returns:
            Self for chaining
        """
        if kwargs is None:
            kwargs = {}
        step = WorkflowStep(name, func, args, kwargs)
        self.steps.append(step)
        logger.info(f"Added step to workflow {self.name}: {name}")
        return self

    def execute(self) -> Dict[str, Any]:
        """Execute workflow.

        Returns:
            Dictionary with step results
        """
        logger.info(f"Starting workflow execution: {self.name}")
        self.results = {}

        for step in self.steps:
            try:
                logger.info(f"Executing step: {step.name}")
                result = step.func(*step.args, **step.kwargs)
                self.results[step.name] = {"status": "success", "result": result}
                logger.info(f"Step completed: {step.name}")
            except Exception as e:
                logger.error(f"Step failed: {step.name} - {str(e)}")
                self.results[step.name] = {"status": "failed", "error": str(e)}

        logger.info(f"Workflow completed: {self.name}")
        return self.results

    def get_results(self) -> Dict[str, Any]:
        """Get workflow results.

        Returns:
            Results dictionary
        """
        return self.results
