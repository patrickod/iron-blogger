import random
import sys
import yaml

from dateutil.parser import parse

import render

from config import START


def raffle(last_meetup):
    with open('out/report.yml') as r:
        report = yaml.safe_load(r)
    with open('bloggers.yml') as f:
        users = yaml.safe_load(f)

    last_meetup_datetime = parse(last_meetup)

    tickets = []
    for (un, rec) in users.items():
        if rec.get('end'):
            continue
        weeks = report.get(un, [])
        for week in weeks:
            if not week or not week[0]:
                continue
            if week[0]['date'] > last_meetup_datetime:
                tickets.append(un)
    print tickets
    return random.choice(tickets)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        date = sys.argv[1]
        print raffle(date)
    else:
        print "Must pass date %Y-%m-%d"
