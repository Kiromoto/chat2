from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='ava/avadefault.png', upload_to='ava/', verbose_name='Avatar', blank=True)
    adress = models.CharField(max_length=256, blank=True, verbose_name='Adress')
    phoneNumber = PhoneNumberField(unique=True, blank=True)
    online = models.BooleanField(default=False)


# class Chatroom(models.Model):
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)
#     chatname = models.CharField(max_length=32)
#     chatmember = models.ManyToManyField(Member, through='MemberChatroom', related_name='chatroom', blank=True, default='creator')
#
#
# class Message(models.Model):
#     sender = models.ForeignKey(Member, on_delete=models.CASCADE)
#     text = models.CharField(max_length=1024)
#     datetimecreate = models.DateTimeField(auto_now_add=True)
#     read = models.BooleanField(default=False)
#     inchatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name='message')
