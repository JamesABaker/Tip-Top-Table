# Generated by Django 2.2.5 on 2020-02-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0019_tmh_meta_tmh'),
    ]

    operations = [
        migrations.AddField(
            model_name='variant',
            name='variant_map',
            field=models.TextField(null=True),
        ),
    ]
