# Generated by Django 2.1.4 on 2018-12-18 23:57

from django.db import migrations


def load_horse_sexes(apps, schema_editor):
    HorseSex = apps.get_model('server', 'HorseSex')

    HorseSex.objects.bulk_create([
        HorseSex(name='male'),
        HorseSex(name='female'),
        HorseSex(name='castrated'),
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('server', '0005_racetracks'),
    ]

    operations = [
        migrations.RunPython(load_horse_sexes, migrations.RunPython.noop)
    ]
