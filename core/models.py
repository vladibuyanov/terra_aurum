from django.db import models
from django.utils.text import slugify
from terra_aurum.settings import FILES_DIR, EVENTS_FOTO_DIR


class Event(models.Model):
    photo = models.ImageField(
        upload_to=EVENTS_FOTO_DIR,
        blank=True, null=True,
        default=f'{EVENTS_FOTO_DIR}/default.jpg'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    time = models.DateTimeField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.title} {self.time.date()}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class FileModel(models.Model):
    file_name = models.CharField(max_length=200)
    file = models.FileField(upload_to=FILES_DIR)
    description = models.TextField()

    def __str__(self):
        dir_name = self.file.name.split('.')[0]
        name = dir_name.split('/')[-1]
        return name
