from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):

    user=models.OneToOneField(User , on_delete=models.CASCADE)
    bio=models.TextField()
    age=models.PositiveSmallIntegerField()
    phone=models.PositiveIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username

#signal
def save_profile(sender, **kwargs):
    if kwargs['created']:
        p1=Profile(user=kwargs['instance'])
        p1.save()

post_save.connect(save_profile, sender=User)



class Relation(models.Model):
    from_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    to_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-created',)


    def __str__(self) -> str:
        return f'{self.from_user} is following {self.to_user}'



