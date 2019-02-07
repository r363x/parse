#!/usr/bin/env python3

import re
from operator import itemgetter
from itertools import groupby


parsed = list()
regex = re.compile('(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) +\[(?P<dt>.*)\+\d{4}\] +\"(?P<uri>.*?)\" +\
(?P<code>\d{3}) +(?P<bytes>\d+) +\"(?P<ref>.*?)\" +\"(?P<agent>.*?)\".*: (?P<time>\d+)$')

with open('/var/log/apache2/asdf_access.log', 'r') as l:
    while True:
        line = l.readline()
        if line:
            try:
                parsed.append([x for x in regex.match(line).groups()])
            except AttributeError:
                pass
        else:
            break

parsed.sort(key=itemgetter(0))

counted = list()

for item, group in groupby(parsed, key=itemgetter(0)):
    counted.append([item, len(list(group))])

counted.sort(key=itemgetter(1), reverse=True)
for x in counted:
    print('IP: {},\tCOUNT: {}'.format(x[0], x[1]))

