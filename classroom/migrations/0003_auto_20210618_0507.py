# Generated by Django 3.2.3 on 2021-06-18 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classroom", "0002_alter_user_first_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="description",
            new_name="comment",
        ),
        migrations.RenameField(
            model_name="customer",
            old_name="chases_number",
            new_name="phone_number",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="b_break",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="battery",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="c_gear",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="car_category",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="contact_number",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="customer_name",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="f_indicator_left",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="f_indicator_right",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="f_wiper_left",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="f_wiper_right",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="h_lamps_left",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="h_lamps_right",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="id_number",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="id_type",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="key",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="p_tank",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="r_mirror",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="s_mirror_left",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="s_mirror_right",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="spear_tyre",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="starter",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="t_indicator",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="vehicle_number",
        ),
        migrations.RemoveField(
            model_name="customer",
            name="wiper_back",
        ),
        migrations.AddField(
            model_name="customer",
            name="device",
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name="customer",
            name="price",
            field=models.TextField(blank=True, max_length=5000),
        ),
    ]
