"""Helpers for surfacing tasks that need attention soon."""

from datetime import datetime, timedelta

_SOON = timedelta(days=2)


def due_soon(task):
    """Return True if task.remind_at falls within the next two days."""
    if not task.remind_at:
        return False
    remind = datetime.fromisoformat(task.remind_at)
    delta = remind - datetime.now()
    return timedelta(0) <= delta < _SOON
