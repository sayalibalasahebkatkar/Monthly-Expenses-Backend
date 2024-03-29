# Generated by Django 4.1.13 on 2024-03-11 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomates', '0004_alter_transaction_description_alter_transaction_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='user_id',
            field=models.ManyToManyField(related_name='teams', to='roomates.roomate'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='roomates.team'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='roomates.roomate'),
        ),
    ]
