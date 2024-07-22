from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from todo.models import Task

class TaskViewsTestCase(TestCase):
    # pass
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            complete=False,
            user=self.user
        )
    
    def test_task_list_view(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_list.html')
        self.assertContains(response, self.task.title)
    
    def test_task_detail_view(self):
        response = self.client.get(reverse('task-detail', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_detail.html')
        self.assertContains(response, self.task.title)
    
    def test_task_create_view(self):
        response = self.client.get(reverse('task-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_create.html')
        response = self.client.post(reverse('task-create'), {
            'title': 'New Task',
            'description': 'New Description',
            'complete': False
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 2)
    
    def test_task_update_view(self):
        response = self.client.get(reverse('task-update', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_create.html')
        response = self.client.post(reverse('task-update', kwargs={'pk': self.task.pk}), {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'complete': True
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
    
    def test_task_delete_view(self):
        response = self.client.get(reverse('task-delete', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_delete.html')
        response = self.client.post(reverse('task-delete', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
