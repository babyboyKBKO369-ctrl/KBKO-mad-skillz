"""Tests for task scheduler."""

import pytest
import time
from smokey.scheduler.task_scheduler import TaskScheduler


@pytest.fixture
def scheduler():
    """Create scheduler instance."""
    return TaskScheduler()


def test_scheduler_start_stop(scheduler):
    """Test scheduler start and stop."""
    scheduler.start()
    assert scheduler.scheduler.running
    scheduler.stop()
    assert not scheduler.scheduler.running


def test_add_interval_job(scheduler):
    """Test adding interval job."""
    scheduler.start()
    
    def test_func():
        pass
    
    job_id = scheduler.add_interval_job(test_func, seconds=10)
    assert job_id in scheduler.jobs
    
    scheduler.stop()


def test_add_cron_job(scheduler):
    """Test adding cron job."""
    scheduler.start()
    
    def test_func():
        pass
    
    job_id = scheduler.add_cron_job(test_func, hour=12, minute=0)
    assert job_id in scheduler.jobs
    
    scheduler.stop()


def test_remove_job(scheduler):
    """Test removing job."""
    scheduler.start()
    
    def test_func():
        pass
    
    job_id = scheduler.add_interval_job(test_func, seconds=10)
    assert job_id in scheduler.jobs
    
    scheduler.remove_job(job_id)
    assert job_id not in scheduler.jobs
    
    scheduler.stop()


def test_get_jobs(scheduler):
    """Test getting jobs."""
    scheduler.start()
    
    def test_func():
        pass
    
    scheduler.add_interval_job(test_func, seconds=10, job_id="test_1")
    scheduler.add_interval_job(test_func, seconds=20, job_id="test_2")
    
    jobs = scheduler.get_jobs()
    assert len(jobs) == 2
    assert "test_1" in jobs
    assert "test_2" in jobs
    
    scheduler.stop()
