import random
import sys
import yaml

from collections import Counter
from dateutil.parser import parse

def shuffle(last_meetup_datetime):
    with open('out/report.yml') as r:
        report = yaml.safe_load(r)
    with open('bloggers.yml') as f:
        users = yaml.safe_load(f)

    tickets = Counter()
    for (username, info) in users.items():
        if info.get('end'):
            continue
        weeks = report.get(username, [])
        for week in weeks:
            if not week or not week[0]:
                continue
            if week[0]['date'] > last_meetup_datetime:
                tickets[username] += 1
    return tickets

def raffle(last_meetup_str):
    last_meetup_datetime = parse(last_meetup_str)
    tickets = shuffle(last_meetup_datetime)
    print "Raffle contains the following tickets:"
    print tickets
    print "And the winner is:"
    return random.choice(list(tickets.elements()))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        date = sys.argv[1]
        print raffle(date)
    else:
        print "Usage: python raffle.py <LAST_MEETUP_DATE as %Y-%m-%d>"
