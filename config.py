#!/usr/bin/env python
## -*- coding: utf-8 -*-

import os.path
import datetime
import subprocess

HERE  = os.path.dirname(__file__)
START = datetime.datetime(2015, 3, 2, 6)

XMLRPC_ENDPOINT = 'http://iron-blogger.noisebridge.systems/xmlrpc.php'
USER            = 'patrickod'
BLOG_ID         = 1
PARTICIPANTS_PAGE_ID = 5

MAILING_LIST_EMAIL = 'iron-blogger@lists.noisebridge.net'

FINE_SIZE = 5
CURRENCY = "$"

# check the version of ledger to find out which commands to use
if subprocess.check_output(['ledger', '--version'])[7] == "3":
    BALANCE_CMD = ['ledger', '-f', os.path.join(HERE,'ledger'),
                   '--no-color', '-n', 'balance']

    DEBTS_CMD = ['ledger', '-f', os.path.join(HERE, 'ledger'),
                 '--flat', '--no-total', '--no-color',
                 'balance', 'Pool:Owed:']

else:
    BALANCE_CMD = ['ledger', '-f', os.path.join(HERE, 'ledger'),
                   '-n', 'balance']
    DEBTS_CMD = ['ledger', '-f', os.path.join(HERE, 'ledger'),
                 '-n', 'balance', 'Pool:Owed:']

PUNT_TEXT = """\
%(date)s Punt
  Pool:Owed:%(user)s  -%(debt)s
  User:%(user)s"""
