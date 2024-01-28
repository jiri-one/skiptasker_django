# Generated by Django 5.0.1 on 2024-01-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_task_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="completion_time",
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="creation_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
