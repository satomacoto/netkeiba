from django.db import models

from netkeiba.models.base import BaseModel


class Race(BaseModel):
    UNKNOWN = 'UNKNOWN'

    SAPPORO = 'SAPPORO'
    HAKODATE = 'HAKODATE'
    FUMA = 'FUMA'
    NIIGATA = 'NIIGATA'
    TOKYO = 'TOKYO'
    NAKAYAMA = 'NAKAYAMA'
    CHUKYO = 'CHUKYO'
    KYOTO = 'KYOTO'
    HANSHIN = 'HANSHIN'
    OGURA = 'OGURA'
    RACETRACK_CHOICES = (
        (SAPPORO, 'Sapporo'),
        (HAKODATE, 'Hakodate'),
        (FUMA, 'Fuma'),
        (NIIGATA, 'Niigata'),
        (TOKYO, 'Tokyo'),
        (NAKAYAMA, 'Nakayama'),
        (CHUKYO, 'Chukyo'),
        (KYOTO, 'Kyoto'),
        (HANSHIN, 'Hanshin'),
        (OGURA, 'Ogura'),
        (UNKNOWN, 'Unknown'),
    )

    HORSE_AGE = 'HORSE_AGE'
    WEIGHT_FOR_AGE = 'WEIGHT_FOR_AGE'
    SET_WEIGHT = 'SET_WEIGHT'
    HANDICAP = 'HANDICAP'
    IMPOST_CATEGORY_CHOICES = (
        # [馬齢] 同一年齢の馬だけのレース
        (HORSE_AGE, 'Horse age'),
        # [定量] 別定のなかでも、馬の年齢と性別を基準に定められているレース
        (WEIGHT_FOR_AGE, 'Weight for age'),
        # [別定] そのレース毎に負担重量を決定する基準が設けられているレース
        (SET_WEIGHT, 'Set weight'),
        # [ハンデ] 出走予定馬の実績や最近の状態などを考慮し
        # 各出走馬に勝つチャンスを与えるよう決められた重量を負担させるレース
        (HANDICAP, 'Handicap'),
        (UNKNOWN, 'Unknown'),
    )

    DIRT = 'DIRT'
    TURF = 'TURF'
    SURFACE_CHOICES = (
        (DIRT, 'Dirt'),
        (TURF, 'Turf'),
        (UNKNOWN, 'Unknown'),
    )

    JUST2 = 'JUST2'
    JUST3 = 'JUST3'
    JUST4 = 'JUST4'
    OVER3 = 'OVER3'
    OVER4 = 'OVER4'
    OVER5 = 'OVER5'
    OVER3OBSTACLE = 'OVER3OBSTACLE'
    OVER4OBSTACLE = 'OVER4OBSTACLE'

    RACE_TYPE_CHOICES = (
        (JUST2, 'JUST2'),
        (JUST3, 'JUST3'),
        (JUST4, 'JUST4'),
        (OVER3, 'OVER3'),
        (OVER4, 'OVER4'),
        (OVER5, 'OVER5'),
        (OVER3OBSTACLE, 'OVER3OBSTACLE'),
        (OVER4OBSTACLE, 'OVER4OBSTACLE'),
        (UNKNOWN, 'Unknown'),
    )

    UNRACED_MAIDEN = 'UNRACED_MAIDEN'
    MAIDEN = 'MAIDEN'
    UNRACED = 'UNRACED'
    W1 = 'W1'
    W2 = 'W2'
    W3 = 'W3'
    U500 = 'U500'
    U900 = 'U900'
    U1000 = 'U1000'
    U1600 = 'U1600'
    OPEN = 'OPEN'
    G3 = 'G3'
    G2 = 'G2'
    G1 = 'G1'

    RACE_CLASS_CHOICES = (
        (UNRACED_MAIDEN, 'UNRACED_MAIDEN'),
        (MAIDEN, 'MAIDEN'),
        (UNRACED, 'UNRACED'),
        (W1, 'W1'),
        (W2, 'W2'),
        (W3, 'W3'),
        (U500, 'U500'),
        (U900, 'U900'),
        (U1000, 'U1000'),
        (U1600, 'U1600'),
        (OPEN, 'OPEN'),
        (G3, 'G3'),
        (G2, 'G2'),
        (G1, 'G1'),
        (UNKNOWN, 'Unknown'),
    )

    CLOUDY = 'CLOUDY'
    RAINY = 'RAINY'
    LIGHT_RAIN = 'LIGHT_RAIN'
    SUNNY = 'SUNNY'
    SNOWY = 'SNOWY'
    WEATHER_CHOICES = (
        (CLOUDY, 'Cloudy'),
        (RAINY, 'Rainy'),
        (LIGHT_RAIN, 'Light rain'),
        (SUNNY, 'Sunny'),
        (SNOWY, 'Snowy'),
        (UNKNOWN, 'Unknown'),
    )

    SLIGHTLY_HEAVY = 'SLIGHTLY_HEAVY'
    HEAVY = 'HEAVY'
    GOOD = 'GOOD'
    BAD = 'BAD'
    TRACK_CONDITION_CHOICES = (
        (SLIGHTLY_HEAVY, 'Slightly heavy'),
        (HEAVY, 'Heavy'),
        (GOOD, 'Good'),
        (BAD, 'Bad'),
        (UNKNOWN, 'Unknown'),
    )

    STRAIGHT = 'STRAIGHT'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    OBSTACLE = 'OBSTACLE'
    COURSE_CHOICES = (
        (LEFT, 'Left'),
        (RIGHT, 'Right'),
        (STRAIGHT, 'Straight'),
        (OBSTACLE, 'Obstacle'),
        (UNKNOWN, 'Unknown'),
    )

    key = models.CharField(max_length=255, unique=True)
    racetrack = models.CharField(max_length=255, choices=RACETRACK_CHOICES, default=UNKNOWN)
    impost_category = models.CharField(max_length=255, choices=IMPOST_CATEGORY_CHOICES, default=UNKNOWN)
    surface = models.CharField(max_length=255, choices=SURFACE_CHOICES, default=UNKNOWN)
    course = models.CharField(max_length=255, choices=COURSE_CHOICES, default=UNKNOWN)
    distance = models.PositiveSmallIntegerField()
    number = models.PositiveSmallIntegerField()
    race_type = models.CharField(max_length=255, choices=RACE_TYPE_CHOICES, default=UNKNOWN)
    race_class = models.CharField(max_length=255, choices=RACE_CLASS_CHOICES, default=UNKNOWN)
    datetime = models.DateTimeField()
    weather = models.CharField(max_length=255, choices=WEATHER_CHOICES, default=UNKNOWN)
    track_condition = models.CharField(max_length=255, choices=TRACK_CONDITION_CHOICES, default=UNKNOWN)

    # 外枠か
    is_outside_racetrack = models.BooleanField()

    # (指定) [地]が出走できるレースで、かつ地方競馬所属の騎手が騎乗できる(特指)以外のレース
    is_regional_maiden_race = models.BooleanField()

    # (特指) JRAが認定した地方競馬の競走で第1着となった[地]が出走できるレースで、かつ地方競馬所属の騎手が騎乗できるレース
    is_winner_regional_horse_race = models.BooleanField()

    # [指定] 地方競馬所属の騎手が騎乗できるレース
    is_regional_jockey_race = models.BooleanField()

    # (混) 内国産馬にマル外が混合して出走できるレース
    is_foreign_horse_race = models.BooleanField()

    # (国際) 内国産馬に(外)および[外]が混合して出走できるレース
    is_foreign_trainer_horse_race = models.BooleanField()

    # (見習騎手) 若手騎手が騎乗できるレース
    is_apprentice_jockey_race = models.BooleanField()

    # (牝) 牝馬しか出走できないレース
    is_female_only_race = models.BooleanField()

    class Meta:
        db_table = 'races'
        get_latest_by = '-datetime'
        unique_together = ('racetrack', 'datetime')
