# Generated by Django 4.2.14 on 2024-09-19 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_rename_booking_reservation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="phone",
            field=models.CharField(max_length=10),
        ),
    ]
