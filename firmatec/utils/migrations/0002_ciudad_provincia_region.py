# Generated by Django 3.2.3 on 2021-08-04 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utils.region')),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utils.provincia')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='utils.region')),
            ],
        ),
    ]
