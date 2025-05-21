from django.db import models

# Example
user = models.ForeignKey(User, on_delete=models.CASCADE)
