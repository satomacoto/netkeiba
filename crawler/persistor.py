import logging
from typing import Dict, List

from django.apps import apps
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.forms import model_to_dict

logger = logging.getLogger(__name__)


class Persistor:
    def get(self, model_key: str, **kwargs) -> Dict:
        raise NotImplementedError

    def get_or_create(self, model_key: str, defaults=None, **kwargs):
        raise NotImplementedError

    def update_or_create(self, model_key: str, defaults=None, **kwargs) -> Dict:
        raise NotImplementedError

    def all(self, model_key: str) -> List[Dict]:
        raise NotImplementedError


class DjangoPersistor(Persistor):
    _model_lookup_map = {
        'apprentice_jockey_race': 'ApprenticeJockeyRace',
        'course_type': 'CourseType',
        'female_only_race': 'FemaleOnlyRace',
        'foreign_horse_race': 'ForeignHorseRace',
        'foreign_horse_and_trainer_race': 'ForeignTrainerHorseRace',
        'horse': 'Horse',
        'horse_sex': 'HorseSex',
        'impost_category': 'ImpostCategory',
        'jockey': 'Jockey',
        'non_winner_regional_horse_race': 'NonWinnerRegionalHorseRace',
        'race': 'Race',
        'race_contender': 'RaceContender',
        'racetrack': 'Racetrack',
        'regional_jockey_race': 'RegionalJockeyRace',
        'trainer': 'Trainer',
        'turf_condition_category': 'TurfConditionCategory',
        'dirt_condition_category': 'DirtConditionCategory',
        'weather_category': 'WeatherCategory',
        'winner_regional_horse_race': 'WinnerRegionalHorseRace',
    }

    def get(self, model_key: str, **kwargs) -> Dict:
        model_name = self._model_lookup_map.get(model_key)
        try:
            record = apps.get_model('server', model_name).objects.get(**kwargs)
        except (LookupError, MultipleObjectsReturned, ObjectDoesNotExist) as e:
            logger.error(f'Error occurred during model lookup: {e}')
            raise e
        else:
            return model_to_dict(record)

    def get_or_create(self, model_key: str, defaults=None, **kwargs):
        model_name = self._model_lookup_map.get(model_key)
        record, _ = apps.get_model('server', model_name).objects.get_or_create(defaults=None, **kwargs)
        return model_to_dict(record)

    def update_or_create(self, model_key: str, defaults=None, **kwargs) -> Dict:
        model_name = self._model_lookup_map.get(model_key)
        record, _ = apps.get_model('server', model_name).objects.update_or_create(defaults=defaults, **kwargs)
        return model_to_dict(record)

    def all(self, model_key: str) -> List[Dict]:
        model_name = self._model_lookup_map.get(model_key)
        query_set = apps.get_model('server', model_name).objects.all()
        return [model_to_dict(record) for record in query_set]
