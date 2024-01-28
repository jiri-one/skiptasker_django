from django.db import models
from django.utils import timezone


class Task(models.Model):
    class Status(models.TextChoices):
        CREATED = "CREATED", ("created")
        INPROGRESS = "INPROGRESS", ("inprogress")
        COMPLETED = "COMPLETED", ("completed")

    def save(self, *args, **kwargs):
        """Override predefined model method and save completion_time if status is set to COMPLETED or delete completion_time if we set another status"""
        if self.status.lower() == "completed":
            self.completion_time = timezone.now()
        elif self.status.lower() != "completed" and self.completion_time is not None:
            self.completion_time = None
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    description = models.CharField(max_length=200)
    creation_time = models.DateTimeField(editable=False, auto_now_add=True)
    completion_time = models.DateTimeField(editable=False, blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=Status,
        default=Status.CREATED,
    )

    class Meta:
        ordering = ["creation_time"]
