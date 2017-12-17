#!/usr/bin/env python
import os

from crudlfap.manage import main

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mrs.settings')

if __name__ == '__main__':
    main()
