from django.db import models
from django.utils import timezone


class FavPictureModel(models.Model):
    class Meta:
        # Create some indexes
        indexes = [
            models.Index(fields=['fp_caption'], name='fp_caption_idx'),
            models.Index(fields=['fp_published_date'], name='fp_published_date_idx'),
        ]
        get_latest_by = "fp_published_date"  # This specifies the default field(s) to use in your model Manager’s
        # latest() and earliest() methods.

    fp_published_date = models.DateTimeField("Published Date", auto_now=True)
    fp_created_date = models.DateTimeField("Date Created", auto_now_add=True)
    fp_caption = models.TextField("Fav Caption", max_length=500, help_text="Enter something will ya?")

    def __str__(self):
        return self.fp_caption
