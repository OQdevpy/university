from django.db import models
from django.db.models.signals import pre_save


class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey('blog.Blog', on_delete=models.CASCADE)
    message = models.TextField()
    is_reply = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.author.username}s comment'


def comment_pre_save(instance, sender, *args, **kwargs):
    if instance.parent is not None:
        instance.is_reply = True
        instance.post_id = instance.parent.post_id


pre_save.connect(comment_pre_save, sender=Comment)




