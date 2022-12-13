# Generated by Django 4.1.4 on 2022-12-11 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatback', '0006_remove_member_chats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='chatmember',
            field=models.ManyToManyField(blank=True, default='creator', related_name='chatroom', through='chatback.MemberChatroom', to='chatback.member'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='memberchatroom',
            name='chatroomid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatback.chatroom'),
        ),
        migrations.AlterField(
            model_name='memberchatroom',
            name='memberid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatback.member'),
        ),
        migrations.AlterField(
            model_name='message',
            name='inchatroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='chatback.chatroom'),
        ),
    ]
