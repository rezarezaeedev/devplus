# Generated by Django 4.0.4 on 2022-06-15 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinfo',
            name='buildtext',
            field=models.CharField(max_length=50, null=1),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='copyright',
            field=models.CharField(max_length=50, null=1),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='fortext',
            field=models.CharField(max_length=50, null=1),
            preserve_default=1,
        ),
    ]
