# Generated by Django 3.0.4 on 2020-04-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_remove_post_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="contact",
            field=models.CharField(default="UNK", max_length=10),
        ),
    ]
