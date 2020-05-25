from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class CreatedTimeStamp(models.Model):
    CreatedDate = models.DateTimeField(auto_now_add=True)
    UpdatedDate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AudioFile(CreatedTimeStamp):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    Audio = models.FileField()
    AudioTranscribed = models.TextField()


    class Meta:
        verbose_name_plural = "AudioFiles"
        #managed = False
        app_label = 'hi'
        db_table = 'AudioFile'

class Entry(CreatedTimeStamp):
    UserID= models.ForeignKey(User, on_delete=models.CASCADE)
    Entry = models.CharField(max_length=30, null=True, blank=True)
    Emotion = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Entries"
        #managed=False
        app_label='hi'
        db_table='Entry'

class Journal(CreatedTimeStamp):
    UserID= models.ForeignKey(User, on_delete=models.CASCADE)
    Journal = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.id
    class Meta:
        verbose_name_plural = "Journals"
        #managed=False
        app_label='hi'
        db_table='Journal'
