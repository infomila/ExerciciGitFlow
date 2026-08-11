import unittest

from taskflow.tasks import Task


class TaskTests(unittest.TestCase):
    def test_defaults(self):
        task = Task("Write tests")
        self.assertFalse(task.done)
        self.assertIsNotNone(task.id)

    def test_ids_are_unique(self):
        first = Task("First")
        second = Task("Second")
        self.assertNotEqual(first.id, second.id)


if __name__ == "__main__":
    unittest.main()
