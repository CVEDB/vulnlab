# Generated by Django 2.0.4 on 2019-10-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bnmc_project", "0042_examination_result_add"),
    ]

    operations = [
        migrations.AlterField(
            model_name="examination_result_add",
            name="create",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
