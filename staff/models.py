from django.db import models

class Role(models.TextChoices):
    engineer = ("Engineer", "engineer")
    worker = ("Worker", "worker")
    accountant = ("Accountant", "accountant")
    manager = ("Manager", "manager")
    guard = ("Guard", "guard")


class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/staff/")
    position = models.CharField(max_length=50, choices=Role.choices, default=Role.worker)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


