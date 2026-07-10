"""Task scheduling engine using APScheduler."""

from typing import Callable, Optional, Dict, Any
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


class TaskScheduler:
    """Task scheduler for scheduling recurring jobs."""

    def __init__(self):
        """Initialize task scheduler."""
        self.scheduler = BackgroundScheduler()
        self.jobs: Dict[str, Any] = {}

    def start(self) -> None:
        """Start the scheduler."""
        if not self.scheduler.running:
            self.scheduler.start()
            logger.info("Task scheduler started")

    def stop(self) -> None:
        """Stop the scheduler."""
        if self.scheduler.running:
            self.scheduler.shutdown()
            logger.info("Task scheduler stopped")

    def add_interval_job(
        self,
        func: Callable,
        seconds: int = 0,
        minutes: int = 0,
        hours: int = 0,
        days: int = 0,
        job_id: Optional[str] = None,
        **kwargs
    ) -> str:
        """Add interval-based job.

        Args:
            func: Function to schedule
            seconds: Interval in seconds
            minutes: Interval in minutes
            hours: Interval in hours
            days: Interval in days
            job_id: Job ID
            **kwargs: Additional arguments

        Returns:
            Job ID
        """
        job_id = job_id or f"job_{len(self.jobs)}"
        job = self.scheduler.add_job(
            func,
            "interval",
            seconds=seconds,
            minutes=minutes,
            hours=hours,
            days=days,
            id=job_id,
            **kwargs
        )
        self.jobs[job_id] = job
        logger.info(f"Added interval job: {job_id}")
        return job_id

    def add_cron_job(
        self,
        func: Callable,
        job_id: Optional[str] = None,
        **kwargs
    ) -> str:
        """Add cron-based job.

        Args:
            func: Function to schedule
            job_id: Job ID
            **kwargs: Cron expression arguments

        Returns:
            Job ID
        """
        job_id = job_id or f"job_{len(self.jobs)}"
        job = self.scheduler.add_job(func, "cron", id=job_id, **kwargs)
        self.jobs[job_id] = job
        logger.info(f"Added cron job: {job_id}")
        return job_id

    def remove_job(self, job_id: str) -> None:
        """Remove a job.

        Args:
            job_id: Job ID to remove
        """
        if job_id in self.jobs:
            self.scheduler.remove_job(job_id)
            del self.jobs[job_id]
            logger.info(f"Removed job: {job_id}")

    def get_jobs(self) -> Dict[str, Any]:
        """Get all jobs.

        Returns:
            Dictionary of jobs
        """
        return self.jobs
