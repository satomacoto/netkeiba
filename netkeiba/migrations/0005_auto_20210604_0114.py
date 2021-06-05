# Generated by Django 3.2.4 on 2021-06-04 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netkeiba', '0004_alter_race_race_class_choices'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='race_type',
            field=models.CharField(choices=[('JUST2', 'JUST2'), ('JUST3', 'JUST3'), ('JUST4', 'JUST4'), ('OVER3', 'OVER3'), ('OVER4', 'OVER4'), ('OVER5', 'OVER5'), ('OVER3OBSTACLE', 'OVER3OBSTACLE'), ('OVER4OBSTACLE', 'OVER4OBSTACLE'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=255),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_class',
            field=models.CharField(choices=[('UNRACED_MAIDEN', 'UNRACED_MAIDEN'), ('MAIDEN', 'MAIDEN'), ('UNRACED', 'UNRACED'), ('W1', 'W1'), ('W2', 'W2'), ('W3', 'W3'), ('U500', 'U500'), ('U900', 'U900'), ('U1000', 'U1000'), ('U1600', 'U1600'), ('OPEN', 'OPEN'), ('G3', 'G3'), ('G2', 'G2'), ('G1', 'G1'), ('UNKNOWN', 'Unknown')], default='UNKNOWN', max_length=255),
        ),
    ]
