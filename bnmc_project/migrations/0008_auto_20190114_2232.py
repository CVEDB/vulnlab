# Generated by Django 2.1.1 on 2019-01-14 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bnmc_project", "0007_auto_20190114_2229"),
    ]

    operations = [
        migrations.AlterField(
            model_name="educationqualification",
            name="cgpa",
            field=models.CharField(max_length=120, null=True, verbose_name="CGPA"),
        ),
    ]
