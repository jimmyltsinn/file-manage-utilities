import sys
import plistlib
import os
from urllib.parse import urlparse
import urllib.request

root = plistlib.load(open(sys.argv[1], 'rb'))
tracks = root['Tracks']

err = []
notexist = []
purchased = []

for i in tracks:
    try:
        track = tracks[i]
        if ('Purchased' in track and track['Purchased']):
            purchased.append(track)
            continue
        loc = urllib.request.unquote(urlparse(track['Location']).path)
        exist = os.path.isfile(loc)
        if (not exist):
            notexist.append(loc)
    except:
        err.append(track)

print('-- Purchased --')
purchased = sorted(purchased, key=lambda e: e['Name'])
for entry in purchased:
    print('%s (%s)'%(entry['Name'], entry['Artist']))

print()
print('-- Not Exist --')
notexist = sorted(notexist)
for entry in notexist:
    print(entry)

print()
print('-- Error --')
for entry in err:
    print(entry['Name'], entry)
