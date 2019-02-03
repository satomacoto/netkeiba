from django.db import models

from server.models import BaseModel


class RaceContender(BaseModel):
    UNKNOWN = 'UNKNOWN'

    OK = 'OK'
    DISQUALIFIED = 'DISQUALIFIED'  # 失
    CANCELLED = 'CANCELLED'  # 取|除
    REMOUNT = 'REMOUNT'  # 再
    NO_FINISH = 'NO_FINISH'  # 中
    POSITION_LOWERED = 'POSITION_LOWERED'  # 降
    POSITION_STATE_CHOICES = (
        (OK, 'OK'),
        (DISQUALIFIED, 'Disqualified'),
        (CANCELLED, 'Cancelled'),
        (REMOUNT, 'Remount'),
        (NO_FINISH, 'Did not finish'),
        (POSITION_LOWERED, 'Position lowered'),
        (UNKNOWN, 'Unknown')
    )

    NOSE = 'NOSE'
    HEAD = 'HEAD'
    NECK = 'NECK'
    OTHER = 'OTHER'
    MARGIN_CHOICES = (
        (NOSE, 'Nose'),
        (HEAD, 'Head'),
        (NECK, 'Neck'),
        (OTHER, 'Other')
    )

    race = models.ForeignKey('server.Race', on_delete=models.CASCADE)
    horse = models.ForeignKey('server.Horse', on_delete=models.CASCADE)
    jockey = models.ForeignKey('server.Jockey', on_delete=models.CASCADE)
    trainer = models.ForeignKey('server.Trainer', on_delete=models.CASCADE)
    owner = models.ForeignKey('server.Owner', on_delete=models.CASCADE)
    order_of_finish = models.PositiveSmallIntegerField()
    position_state = models.CharField(max_length=255, choices=POSITION_STATE_CHOICES)
    post_position = models.PositiveSmallIntegerField()
    horse_number = models.PositiveIntegerField()
    weight_carried = models.FloatField()
    finish_time = models.FloatField()
    # TODO: How about numeric values?
    margin = models.CharField(max_length=255, choices=MARGIN_CHOICES)
    final_stage_time = models.FloatField()
    first_place_odds = models.FloatField()
    popularity = models.PositiveSmallIntegerField()
    horse_weight = models.FloatField(null=True)
    horse_weight_diff = models.FloatField(null=True)
    purse = models.FloatField(default=0.)

    class Meta:
        db_table = 'race_contenders'
        unique_together = ('race', 'horse', 'jockey', 'trainer')
