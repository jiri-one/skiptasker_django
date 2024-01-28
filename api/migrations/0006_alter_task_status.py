# Generated by Django 5.0.1 on 2024-01-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_task_completion_time_alter_task_creation_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[
                    ("CREATED", "created"),
                    ("INPROGRESS", "inprogress"),
                    ("COMPLETED", "completed"),
                ],
                default="CREATED",
                max_length=50,
            ),
        ),
    ]