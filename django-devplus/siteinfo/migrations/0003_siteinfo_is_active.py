# Generated by Django 4.0.4 on 2022-06-15 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0002_siteinfo_buildtext_siteinfo_copyright_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
