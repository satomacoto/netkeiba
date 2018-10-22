import json
import os
import random
from itertools import chain


class UserAgentMiddleware(object):
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        crawler_list = json.load(open(f'{dir_path}/../resources/crawler-user-agents.json', 'r'))
        self.user_agent_list = list(chain.from_iterable([item['instances'] for item in crawler_list]))

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agent_list)
        if user_agent:
            request.headers['User-Agent'] = user_agent

    def process_exception(self, request, exception, spider):
        user_agent = random.choice(self.user_agent_list)
        request.headers['User-Agent'] = user_agent
