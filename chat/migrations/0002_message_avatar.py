# Generated by Django 3.2.4 on 2023-07-15 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='avatar',
            field=models.ImageField(default='avatar.png', upload_to='avatars/'),
        ),
    ]