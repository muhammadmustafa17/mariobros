#!"d:\university of michigan ms ai\advance artificail intellegence\mariobros\mariosupbros\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'nes-py==8.1.8','console_scripts','nes_py'
__requires__ = 'nes-py==8.1.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('nes-py==8.1.8', 'console_scripts', 'nes_py')()
    )
