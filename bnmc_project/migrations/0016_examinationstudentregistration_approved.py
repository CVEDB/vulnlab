# Generated by Django 2.1.1 on 2019-05-22 06:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bnmc_project", "0015_auto_20190407_1901"),
    ]

    operations = [
        migrations.AddField(
            model_name="examinationstudentregistration",
            name="approved",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
