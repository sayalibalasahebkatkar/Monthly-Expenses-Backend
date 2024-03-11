# Generated by Django 4.1.13 on 2024-03-11 17:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomates', '0002_alter_roomate_user_id_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('description', models.TextField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('team', models.ForeignKey(db_column='team_id', on_delete=django.db.models.deletion.CASCADE, to='roomates.team')),
                ('user', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='roomates.roomate')),
            ],
        ),
    ]
