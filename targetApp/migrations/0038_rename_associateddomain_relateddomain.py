# Generated by Django 3.2.4 on 2023-04-16 02:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("targetApp", "0037_auto_20230416_0216"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AssociatedDomain",
            new_name="RelatedDomain",
        ),
    ]
