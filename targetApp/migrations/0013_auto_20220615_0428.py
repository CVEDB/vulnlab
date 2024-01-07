# Generated by Django 3.2.4 on 2022-06-15 04:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("targetApp", "0012_auto_20220614_1738"),
    ]

    operations = [
        migrations.CreateModel(
            name="DomainWhoisStatus",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin_address",
            field=models.ManyToManyField(
                blank=True, related_name="admin_address", to="targetApp.DomainAddress"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin_city",
            field=models.ManyToManyField(
                blank=True, related_name="admin_city", to="targetApp.DomainCity"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin_country",
            field=models.ManyToManyField(
                blank=True, related_name="admin_country", to="targetApp.DomainCountry"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin_email",
            field=models.ManyToManyField(
                blank=True, related_name="admin_email", to="targetApp.DomainEmail"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin_fax",
            field=models.ManyToManyField(
                blank=True, related_name="admin_fax", to="targetApp.DomainFax"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin_name",
            field=models.ManyToManyField(
                blank=True, related_name="admin_name", to="targetApp.DomainRegisterName"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin_organization",
            field=models.ManyToManyField(
                blank=True,
                related_name="admin_organization",
                to="targetApp.DomainRegisterOrganization",
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin_phone",
            field=models.ManyToManyField(
                blank=True, related_name="admin_phone", to="targetApp.DomainPhone"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin_state",
            field=models.ManyToManyField(
                blank=True, related_name="admin_state", to="targetApp.DomainState"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="admin_zip_code",
            field=models.ManyToManyField(
                blank=True, related_name="admin_zip_code", to="targetApp.DomainZipCode"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech_address",
            field=models.ManyToManyField(
                blank=True, related_name="tech_address", to="targetApp.DomainAddress"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech_city",
            field=models.ManyToManyField(
                blank=True, related_name="tech_city", to="targetApp.DomainCity"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech_country",
            field=models.ManyToManyField(
                blank=True, related_name="tech_country", to="targetApp.DomainCountry"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech_email",
            field=models.ManyToManyField(
                blank=True, related_name="tech_email", to="targetApp.DomainEmail"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech_fax",
            field=models.ManyToManyField(
                blank=True, related_name="tech_fax", to="targetApp.DomainFax"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech_name",
            field=models.ManyToManyField(
                blank=True, related_name="tech_name", to="targetApp.DomainRegisterName"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech_organization",
            field=models.ManyToManyField(
                blank=True,
                related_name="tech_organization",
                to="targetApp.DomainRegisterOrganization",
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech_phone",
            field=models.ManyToManyField(
                blank=True, related_name="tech_phone", to="targetApp.DomainPhone"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech_state",
            field=models.ManyToManyField(
                blank=True, related_name="tech_state", to="targetApp.DomainState"
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="tech_zip_code",
            field=models.ManyToManyField(
                blank=True, related_name="tech_zip_code", to="targetApp.DomainZipCode"
            ),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="registrant_address",
            field=models.ManyToManyField(
                blank=True,
                related_name="registrant_address",
                to="targetApp.DomainAddress",
            ),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="registrant_city",
            field=models.ManyToManyField(
                blank=True, related_name="registrant_city", to="targetApp.DomainCity"
            ),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="registrant_country",
            field=models.ManyToManyField(
                blank=True,
                related_name="registrant_country",
                to="targetApp.DomainCountry",
            ),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="registrant_email",
            field=models.ManyToManyField(
                blank=True, related_name="registrant_email", to="targetApp.DomainEmail"
            ),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="registrant_fax",
            field=models.ManyToManyField(
                blank=True, related_name="registrant_fax", to="targetApp.DomainFax"
            ),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="registrant_name",
            field=models.ManyToManyField(
                blank=True,
                related_name="registrant_name",
                to="targetApp.DomainRegisterName",
            ),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="registrant_organization",
            field=models.ManyToManyField(
                blank=True,
                related_name="registrant_organization",
                to="targetApp.DomainRegisterOrganization",
            ),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="registrant_phone",
            field=models.ManyToManyField(
                blank=True, related_name="registrant_phone", to="targetApp.DomainPhone"
            ),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="registrant_state",
            field=models.ManyToManyField(
                blank=True, related_name="registrant_state", to="targetApp.DomainState"
            ),
        ),
        migrations.AlterField(
            model_name="domaininfo",
            name="registrant_zip_code",
            field=models.ManyToManyField(
                blank=True,
                related_name="registrant_zip_code",
                to="targetApp.DomainZipCode",
            ),
        ),
        migrations.AddField(
            model_name="domaininfo",
            name="status",
            field=models.ManyToManyField(blank=True, to="targetApp.DomainWhoisStatus"),
        ),
    ]
