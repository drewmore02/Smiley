# Generated by Django 5.1.6 on 2025-02-21 06:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HousingArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('num_bathrooms', models.PositiveIntegerField()),
                ('num_showers', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cabin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('has_heating', models.BooleanField(default=False)),
                ('housing_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cabins', to='housing.housingarea')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.PositiveIntegerField()),
                ('cabin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='housing.cabin')),
            ],
        ),
    ]
