# Generated by Django 3.0.4 on 2020-04-12 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='contact',
        ),
    ]