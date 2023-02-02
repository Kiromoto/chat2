from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user')
    avatar = models.ImageField(default='ava/avadefault.png', upload_to='ava/', verbose_name='Avatar', blank=True)
    online = models.BooleanField(default=False, verbose_name='Online/offline')

    @receiver(post_save, sender=User)
    def create_user_member(sender, instance, created, **kwargs):
        if created:
            Member.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_member(sender, instance, **kwargs):
        instance.member.save()

    def __str__(self):
        return self.user.username


class Chatroom(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Chat name')
    dtcreate = models.DateTimeField(auto_now_add=True, verbose_name='Datetime chat')
    owner = models.ForeignKey(Member, related_name='memberowner', on_delete=models.CASCADE, verbose_name='User-creater')
    guests = models.ManyToManyField(Member, related_name='memberguest', blank=True, verbose_name='Members of chat')

    def get_absolute_url(self):
        return reverse('chat', args=[str(self.id)])

    def __str__(self):
        return self.name



