# Generated by Django 3.2.4 on 2023-04-12 05:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("targetApp", "0030_domaininfo_geolocation_iso"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DomainRegistrar",
            new_name="Registrar",
        ),
        migrations.RenameModel(
            old_name="DomainWhoisStatus",
            new_name="WhoisStatus",
        ),
    ]
