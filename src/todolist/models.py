from django.db import models
from django.utils.text import slugify
# Create your models here.

class NoteModel(models.Model):
    titre = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    date = models.DateTimeField()

    class Meta:
        verbose_name = "Note"

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.titre)

        super().save(*args, **kwargs)
