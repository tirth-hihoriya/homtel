# Generated by Django 3.0.4 on 2020-04-15 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0014_auto_20200415_1241"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomcategory",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
