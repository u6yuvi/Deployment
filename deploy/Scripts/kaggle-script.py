#!c:\users\u6yuv\documents\courses\deployment\deploy\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'kaggle==1.5.1.1','console_scripts','kaggle'
__requires__ = 'kaggle==1.5.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('kaggle==1.5.1.1', 'console_scripts', 'kaggle')()
    )
