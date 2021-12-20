from django.db import models
from django.contrib.auth import get_user_model
import datetime


User = get_user_model()


class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_text_content = models.TextField()
    author = models.ForeignKey(User, related_name="post_author", on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='event_icons/', default='prod_default_image.png')
    post_date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return self.post_title

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="likes")

    class Meta:
        unique_together = ('post', 'user',)


    def __str__(self):
        return self.post_title
