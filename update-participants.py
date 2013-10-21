#!/usr/bin/python

import render
import xmlrpclib
import json

from config import *

with open('secret.txt', 'r') as f:
    secret = json.load(f)
    passwd = secret['wordpress']['password']

x = xmlrpclib.ServerProxy(XMLRPC_ENDPOINT)
page = x.wp.getPage(BLOG_ID, PARTICIPANTS_PAGE_ID, USER, passwd)

text = render.render_template('templates/users.tmpl')
page['description'] = text

x.wp.editPage(BLOG_ID, PARTICIPANTS_PAGE_ID, USER, passwd, page, True)
