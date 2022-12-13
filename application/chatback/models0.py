from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Member(models.Model):
    user = models.OneToOneField(User, related_name='member', on_delete=models.CASCADE)
    avatar = models.ImageField(default='ava/avadefault.png', upload_to='ava/', verbose_name='Загрузите аватарку')
    address = models.TextField(blank=False)
    phone = models.CharField(max_length=16, blank=False)
    online = models.BooleanField(default=False)

    def get_chats(self):
        chats = set()
        for chat in Chatroom.objects.all():
            if self.user in chat.chatmember.all():
                chats.add(chat)
        return chats

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)
        if img.height > 315 or img.width > 315:
            img_newsize = (315, 315)
            img.thumbnail(img_newsize)
            img.save(self.avatar.path)


class Chatroom(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    chatname = models.CharField(max_length=32)
    chatmember = models.ManyToManyField(Member, through='MemberChatroom', related_name='chatroom', blank=True, default='creator')

    def __str__(self):
        return f'{self.chatname}_{self.pk}'

    class Meta:
        ordering = ('pk', 'creator',)


class MemberChatroom(models.Model):
    memberid = models.ForeignKey(Member, blank=True, null=True, on_delete=models.CASCADE)
    chatroomid = models.ForeignKey(Chatroom, blank=True, null=True, on_delete=models.CASCADE)


class Message(models.Model):
    sender = models.ForeignKey(Member, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    datetimecreate = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    inchatroom = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name='message')

    def __str__(self):
        return f'{self.sender.username} {self.text}'

    class Meta:
        ordering = ('datetimecreate',)
