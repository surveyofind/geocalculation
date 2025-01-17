# Generated by Django 5.0.4 on 2024-04-16 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GridData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude_start', models.FloatField()),
                ('latitude_end', models.FloatField()),
                ('longitude_start', models.FloatField()),
                ('longitude_end', models.FloatField()),
                ('height_start', models.FloatField()),
                ('height_end', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GridPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('value', models.FloatField()),
                ('grid_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geocalculation_app.griddata')),
            ],
        ),
    ]
