import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.absolute()
sys.path = [str(ROOT)] + sys.path
print(sys.path)

from functions import *


def make_google_query(query, site, date_min, date_max, page):
    return {
        'q': f'{query} site:{site}',
        'lr': 'lang_ko',
        'client': 'safari',
        'tbs': f'lr:lang_1ko,cdr:1,cd_min:{date_min},cd_max:{date_max}',
        'start': f"{(page - 1) * 10}",
        'sa': 'N'
    }
