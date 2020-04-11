# Generated by Django 3.0.4 on 2020-04-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200411_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(default='UNK', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='UNK', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='hostel_name',
            field=models.CharField(max_length=20),
        ),
    ]
