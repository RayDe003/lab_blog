# Generated by Django 4.2.8 on 2023-12-12 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mic_blog', '0008_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]