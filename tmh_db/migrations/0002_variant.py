# Generated by Django 2.2.2 on 2019-06-28 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aa_wt', models.CharField(default='', max_length=1)),
                ('aa_mut', models.CharField(default='', max_length=1)),
                ('disease_status', models.TextField()),
                ('disease_comments', models.TextField()),
                ('variant_source', models.TextField(default='Unknown', null=True)),
                ('variant_source_id', models.TextField(default='No_ID', null=True)),
                ('residue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmh_db.Residue')),
            ],
        ),
    ]