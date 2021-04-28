# -*- coding: utf-8 -*-
# Script Name   : create_dir_if_not_there.py
# Author        : Caiziyang
# Created       : 2021/4/8 16:16
# Last Modified : 2021/4/8 16:16
# Version       : 1.0.1
# Modifications : 
#
# Description   :

import os


MESSAGE = 'The directory already exists.'
TESTDIR = 'testdir'

try:
    home = os.path.expanduser("~")
    print(home)
    if not os.path.exists(os.path.join(home, TESTDIR)):
        os.mkdir(os.path.join(home, TESTDIR))
    else:
        print(MESSAGE)
except Exception as e:
    print(e)

