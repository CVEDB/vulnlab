# Generated by Django 2.0.4 on 2019-07-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bnmc_project", "0028_auto_20190710_1643"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applylicense",
            name="Working_years_as_a_registered",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
