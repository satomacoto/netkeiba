# Generated by Django 2.1.4 on 2019-01-24 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApprenticeJockeyRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'apprentice_jockey_races',
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'course_types',
            },
        ),
        migrations.CreateModel(
            name='DirtConditionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'dirt_condition_categories',
            },
        ),
        migrations.CreateModel(
            name='FemaleOnlyRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'female_only_races',
            },
        ),
        migrations.CreateModel(
            name='ForeignHorseRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'foreign_horse_races',
            },
        ),
        migrations.CreateModel(
            name='ForeignTrainerHorseRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'foreign_trainer_horse_races',
            },
        ),
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
                ('total_races', models.PositiveSmallIntegerField(null=True)),
                ('total_wins', models.PositiveSmallIntegerField(null=True)),
                ('birthday', models.DateField(null=True)),
                ('user_rating', models.FloatField(blank=True, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'horses',
            },
        ),
        migrations.CreateModel(
            name='HorseSex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'horse_sexes',
            },
        ),
        migrations.CreateModel(
            name='ImpostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'impost_categories',
            },
        ),
        migrations.CreateModel(
            name='Jockey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'jockeys',
            },
        ),
        migrations.CreateModel(
            name='NonWinnerRegionalHorseRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'non_winner_regional_horse_races',
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255, unique=True)),
                ('distance', models.PositiveSmallIntegerField()),
                ('datetime', models.DateTimeField(null=True)),
                ('course_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.CourseType')),
                ('dirt_condition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.DirtConditionCategory')),
                ('impost_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.ImpostCategory')),
            ],
            options={
                'db_table': 'races',
                'get_latest_by': '-date',
            },
        ),
        migrations.CreateModel(
            name='RaceContender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_of_finish', models.PositiveSmallIntegerField()),
                ('order_of_finish_lowered', models.BooleanField()),
                ('did_remount', models.BooleanField()),
                ('post_position', models.PositiveSmallIntegerField()),
                ('weight_carried', models.FloatField()),
                ('finish_time', models.FloatField()),
                ('first_place_odds', models.FloatField()),
                ('popularity', models.PositiveSmallIntegerField()),
                ('horse_weight', models.FloatField(null=True)),
                ('horse_weight_diff', models.FloatField(null=True)),
                ('horse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Horse')),
                ('jockey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Jockey')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Race')),
            ],
            options={
                'db_table': 'race_contenders',
            },
        ),
        migrations.CreateModel(
            name='RaceTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'racetracks',
            },
        ),
        migrations.CreateModel(
            name='RegionalJockeyRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Race')),
            ],
            options={
                'db_table': 'regional_jockey_races',
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'trainers',
            },
        ),
        migrations.CreateModel(
            name='TurfConditionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'turf_condition_categories',
            },
        ),
        migrations.CreateModel(
            name='WeatherCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'weather_categories',
            },
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(unique=True)),
                ('html', models.TextField()),
                ('fingerprint', models.CharField(max_length=255)),
                ('crawled_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'webpages',
            },
        ),
        migrations.CreateModel(
            name='WinnerRegionalHorseRace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Race')),
            ],
            options={
                'db_table': 'winner_regional_horse_races',
            },
        ),
        migrations.AddField(
            model_name='racecontender',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Trainer'),
        ),
        migrations.AddField(
            model_name='race',
            name='racetrack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.RaceTrack'),
        ),
        migrations.AddField(
            model_name='race',
            name='turf_condition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.TurfConditionCategory'),
        ),
        migrations.AddField(
            model_name='race',
            name='weather',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.WeatherCategory'),
        ),
        migrations.AddField(
            model_name='nonwinnerregionalhorserace',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Race'),
        ),
        migrations.AddField(
            model_name='horse',
            name='sex',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.HorseSex'),
        ),
        migrations.AddField(
            model_name='foreigntrainerhorserace',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Race'),
        ),
        migrations.AddField(
            model_name='foreignhorserace',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Race'),
        ),
        migrations.AddField(
            model_name='femaleonlyrace',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Race'),
        ),
        migrations.AddField(
            model_name='apprenticejockeyrace',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Race'),
        ),
        migrations.AlterUniqueTogether(
            name='racecontender',
            unique_together={('race', 'horse', 'jockey', 'trainer')},
        ),
    ]
