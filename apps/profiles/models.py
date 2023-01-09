from django.db import models

# Create your models here.


def path_to_profile_avatar(instance, filename):
    return 'profiles/{0}/{1}'.format(instance.account.username, filename)


class Profile(models.Model):
    ROLE = (
        (0, 'Stuff'),
        (1, 'Teacher'),
        (2, 'Student'),
    )
    account = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=path_to_profile_avatar)
    role = models.IntegerField(choices=ROLE, default=2)
    bio = models.TextField()

    @property
    def full_name(self):
        result = self.account.username
        if self.account.first_name and self.account.last_name:
            result = f'{self.account.first_name} {self.account.last_name}'
        return result

    def __str__(self):
        return f'{self.account.username}s profile'
