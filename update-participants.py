#!/usr/bin/python

import render
import os
import sys
import xmlrpclib
import subprocess

from config import *

with open('secret.txt', 'r') as f:
    passwd = f.read().strip()

x = xmlrpclib.ServerProxy(XMLRPC_ENDPOINT)
page = x.wp.getPage(BLOG_ID, PARTICIPANTS_PAGE_ID, USER, passwd)

text = render.render_template('templates/users.tmpl')
page['description'] = text

x.wp.editPage(BLOG_ID, PARTICIPANTS_PAGE_ID, USER, passwd, page, True)
