from django.db import models

class ComputerSession(models.Model):
    """Represents a computer session in the cyber cafe."""
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title