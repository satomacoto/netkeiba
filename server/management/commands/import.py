import concurrent
import logging
import os

from datetime import datetime

import pytz
from django.conf import settings
from django.core.management import BaseCommand, CommandError

from netkeiba.settings import TIME_ZONE
from server.models import WebPage

logger = logging.getLogger(__name__)


def import_page(queryset, i):
    page = queryset[i]
    parser = page.get_parser()
    try:
        parser.parse()
        parser.persist()
    except Exception as e:
        raise e
    return page.url


class Command(BaseCommand):
    help = 'Extract, clean and persist scraped netkeiba HTML'

    def add_arguments(self, parser):
        parser.add_argument('--scrapy-job-dirname', help='The name of the scrapy crawl jobdir')

    def _get_queryset(self, scrapy_job_dirname=None):
        if scrapy_job_dirname:
            crawls_dir = os.path.join(settings.TMP_DIR, 'crawls')
            requests_seen = os.path.join(crawls_dir, scrapy_job_dirname, 'requests.seen')

            if not os.path.exists(requests_seen):
                raise CommandError('jobdir/requests.seen does not exist')

            fingerprints = open(requests_seen).read().splitlines()
            queryset = WebPage.objects.filter(fingerprint__in=fingerprints)
        else:
            queryset = WebPage.objects.all()

        return queryset

    def handle(self, *args, **options):
        start_time = datetime.now(pytz.timezone(TIME_ZONE))
        logger.info(f'START')
        queryset = self._get_queryset(options.get('scrapy_job_dirname'))
        page_count = queryset.count()

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            future_to_ix = {executor.submit(import_page, queryset, i): i for i in range(page_count)}
            for future in concurrent.futures.as_completed(future_to_ix):
                row = future_to_ix[future] + 1
                try:
                    url = future.result()
                except Exception as e:
                    logger.exception(e)
                else:
                    logger.info(f'({row}/{page_count}) <{url}>')

        stop_time = datetime.now(pytz.timezone(TIME_ZONE))
        duration = (stop_time - start_time).seconds
        logger.info(f'STOP <{duration} seconds>')
