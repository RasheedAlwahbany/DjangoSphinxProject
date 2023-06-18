from django.db import models

# Create your models here.
class App(models.Model):
    """Model definition for App."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for App."""

        verbose_name = 'App'
        verbose_name_plural = 'Apps'

    def __str__(self):
        """Unicode representation of App."""
        pass
