# Generated by Django 3.1.2 on 2020-11-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='status',
            field=models.IntegerField(choices=[(0, 'Check-in'), (1, 'Check-out')], db_index=True, default=0),
        ),
    ]