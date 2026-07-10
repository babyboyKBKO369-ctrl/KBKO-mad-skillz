"""Strategic planning engine."""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


@dataclass
class Objective:
    """Planning objective."""

    name: str
    description: str
    priority: int = 1  # 1=high, 2=medium, 3=low
    deadline: Optional[datetime] = None
    status: str = "pending"  # pending, in_progress, completed


@dataclass
class Plan:
    """Strategic plan."""

    name: str
    description: str
    objectives: List[Objective] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)


class Planner:
    """Strategic planning engine."""

    def __init__(self):
        """Initialize planner."""
        self.plans: Dict[str, Plan] = {}

    def create_plan(self, name: str, description: str) -> Plan:
        """Create a new plan.

        Args:
            name: Plan name
            description: Plan description

        Returns:
            Created plan
        """
        plan = Plan(name=name, description=description)
        self.plans[name] = plan
        logger.info(f"Created plan: {name}")
        return plan

    def add_objective(
        self,
        plan_name: str,
        objective_name: str,
        description: str,
        priority: int = 1,
        deadline_days: Optional[int] = None,
    ) -> Objective:
        """Add objective to plan.

        Args:
            plan_name: Plan name
            objective_name: Objective name
            description: Objective description
            priority: Priority (1=high, 2=medium, 3=low)
            deadline_days: Deadline in days from now

        Returns:
            Created objective
        """
        if plan_name not in self.plans:
            raise ValueError(f"Plan not found: {plan_name}")

        deadline = None
        if deadline_days:
            deadline = datetime.utcnow() + timedelta(days=deadline_days)

        objective = Objective(
            name=objective_name,
            description=description,
            priority=priority,
            deadline=deadline,
        )
        self.plans[plan_name].objectives.append(objective)
        logger.info(f"Added objective to plan {plan_name}: {objective_name}")
        return objective

    def update_objective_status(
        self, plan_name: str, objective_name: str, status: str
    ) -> None:
        """Update objective status.

        Args:
            plan_name: Plan name
            objective_name: Objective name
            status: New status
        """
        if plan_name not in self.plans:
            raise ValueError(f"Plan not found: {plan_name}")

        for obj in self.plans[plan_name].objectives:
            if obj.name == objective_name:
                obj.status = status
                self.plans[plan_name].updated_at = datetime.utcnow()
                logger.info(f"Updated objective status: {objective_name} -> {status}")
                return

        raise ValueError(f"Objective not found: {objective_name}")

    def get_plan(self, plan_name: str) -> Plan:
        """Get plan.

        Args:
            plan_name: Plan name

        Returns:
            Plan object
        """
        if plan_name not in self.plans:
            raise ValueError(f"Plan not found: {plan_name}")
        return self.plans[plan_name]

    def get_all_plans(self) -> Dict[str, Plan]:
        """Get all plans.

        Returns:
            Dictionary of plans
        """
        return self.plans
