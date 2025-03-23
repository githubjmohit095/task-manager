from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task

def aws_lambda_mock(task):
    print(f"AWS Lambda triggered for task: {task.title}")

@receiver(post_save, sender=Task)
def task_status_change(sender, instance, **kwargs):
    if instance.status == 'completed':
        aws_lambda_mock(instance)
