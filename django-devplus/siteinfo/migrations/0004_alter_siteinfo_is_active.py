# Generated by Django 4.0.4 on 2022-06-15 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0003_siteinfo_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='is_active',
            field=models.BooleanField(default=1),
        ),
    ]
