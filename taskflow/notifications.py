from datetime import datetime, timedelta

_SOON = timedelta(days=2)


def due_soon(task):
    if not task.remind_at:
        return False
    remind = datetime.fromisoformat(task.remind_at)
    return remind - datetime.now() < _SOON
