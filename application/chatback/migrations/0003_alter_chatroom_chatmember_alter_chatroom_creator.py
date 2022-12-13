# Generated by Django 4.1.4 on 2022-12-11 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatback', '0002_alter_chatroom_chatmember_alter_chatroom_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='chatmember',
            field=models.ManyToManyField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatrooms', to=settings.AUTH_USER_MODEL), related_name='member', to='chatback.member'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatrooms', to=settings.AUTH_USER_MODEL),
        ),
    ]