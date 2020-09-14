import os
import sys

from discord.ext.commands import Bot

from consts import *

def parse_status(statuses = DEFAULT_STATUSES):
    return [s.strip() for s in statuses.split(',')] 

class BufatronBot(Bot):
    status = parse_status(os.getenv('BUFATRON_BOT_STATUSES'))
    token  = os.getenv('BUFATRON_BOT_OAUTH_TOKEN')

    def __init__(self, **options):
        super().__init__(command_prefix=COMMAND_PREFIX, description=BOT_DESCRIPTION, **options)
