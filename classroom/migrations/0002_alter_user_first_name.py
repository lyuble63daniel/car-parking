# Generated by Django 3.2.3 on 2021-06-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classroom", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
    ]
