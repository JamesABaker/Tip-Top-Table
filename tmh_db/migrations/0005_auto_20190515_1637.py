# Generated by Django 2.2 on 2019-05-15 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tmh_db', '0004_auto_20190515_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funfam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funfam_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pfam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pfam_id', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='funfam_residue',
            name='funfam_id',
        ),
        migrations.CreateModel(
            name='Pfam_residue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('e_value', models.FloatField()),
                ('pfam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmh_db.Pfam')),
                ('residue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tmh_db.Residue')),
            ],
        ),
        migrations.AddField(
            model_name='funfam_residue',
            name='funfam',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tmh_db.Funfam'),
            preserve_default=False,
        ),
    ]