# Generated by Django 3.2.4 on 2023-04-11 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("targetApp", "0025_domain_request_headers"),
    ]

    operations = [
        migrations.CreateModel(
            name="DomainRegistration",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "organization",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("address", models.CharField(blank=True, max_length=500, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                ("zip_code", models.CharField(blank=True, max_length=100, null=True)),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.CharField(blank=True, max_length=500, null=True)),
                ("phone", models.CharField(blank=True, max_length=100, null=True)),
                ("fax", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_address",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_city",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_country",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_email",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_fax",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_id",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_name",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_organization",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_phone",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_state",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="admin_zip_code",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="ip_address",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="raw_text",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="registrant_address",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="registrant_city",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="registrant_country",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="registrant_email",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="registrant_fax",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="registrant_name",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="registrant_organization",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="registrant_phone",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="registrant_state",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="registrant_zip_code",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="related_tlds",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_address",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_city",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_country",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_email",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_fax",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_id",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_name",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_organization",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_phone",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_state",
        ),
        migrations.RemoveField(
            model_name="domaininfo",
            name="tech_zip_code",
        ),
        migrations.AddField(
            model_name="domainregistrar",
            name="email",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="domainregistrar",
            name="phone",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name="domainregistrar",
            name="url",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="dnssec",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="domainregistrar",
            name="name",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name="DomainAddress",
        ),
        migrations.DeleteModel(
            name="DomainCity",
        ),
        migrations.DeleteModel(
            name="DomainCountry",
        ),
        migrations.DeleteModel(
            name="DomainEmail",
        ),
        migrations.DeleteModel(
            name="DomainFax",
        ),
        migrations.DeleteModel(
            name="DomainPhone",
        ),
        migrations.DeleteModel(
            name="DomainRegisterName",
        ),
        migrations.DeleteModel(
            name="DomainRegisterOrganization",
        ),
        migrations.DeleteModel(
            name="DomainRegistrarID",
        ),
        migrations.DeleteModel(
            name="DomainState",
        ),
        migrations.DeleteModel(
            name="DomainZipCode",
        ),
        migrations.DeleteModel(
            name="RelatedTLD",
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="admin",
                to="targetApp.domainregistration",
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="registrant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="registrant",
                to="targetApp.domainregistration",
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tech",
                to="targetApp.domainregistration",
            ),
        ),
    ]
