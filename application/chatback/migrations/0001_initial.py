# Generated by Django 4.1.4 on 2022-12-10 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatname', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('pk', 'creator'),
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='ava/avadefault.png', upload_to='ava/', verbose_name='Загрузите аватарку')),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=16)),
                ('online', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('datetimecreate', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
                ('inchatroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatroom', to='chatback.chatroom')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatback.member')),
            ],
            options={
                'ordering': ('datetimecreate',),
            },
        ),
        migrations.AddField(
            model_name='chatroom',
            name='chatmember',
            field=models.ManyToManyField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatback.member'), related_name='member', to='chatback.member'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatback.member'),
        ),
    ]
