# Generated by Django 3.2.3 on 2021-06-19 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20210618_0507'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Truck',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_register',
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
