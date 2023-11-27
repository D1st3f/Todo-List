from django.test import TestCase
from django.utils import timezone
from .models import Tag, Task


class TagModelTest(TestCase):

    def test_tag_str_method(self):
        tag = Tag.objects.create(name='TestTag')
        self.assertEqual(str(tag), 'TestTag')


class TaskModelTest(TestCase):

    def test_task_ordering(self):
        task1 = Task.objects.create(content='Task1', datetime_field=timezone.now(), task_done=True)
        task2 = Task.objects.create(content='Task2', datetime_field=timezone.now() - timezone.timedelta(days=1),
                                    task_done=False)
        task3 = Task.objects.create(content='Task3', datetime_field=timezone.now() + timezone.timedelta(days=1),
                                    task_done=False)
        self.assertEqual(list(Task.objects.all()), [task2, task3, task1])
