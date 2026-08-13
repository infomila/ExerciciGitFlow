from taskflow.tasks import Task


class Storage:
    """Keeps tasks in memory for the lifetime of the process."""

    def __init__(self):
        self._tasks = []

    def add(self, title):
        task = Task(title)
        self._tasks.append(task)
        return task

    def all(self):
        return list(self._tasks)

    def remove(self, task_id):
        self._tasks = [t for t in self._tasks if t.id != task_id]
