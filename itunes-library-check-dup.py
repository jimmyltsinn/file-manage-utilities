import sys
import plistlib
from urllib.parse import urlparse
import urllib.request

libA = plistlib.load(open(sys.argv[1], 'rb'))['Tracks']

def sameSong(a, b):
    if a['Track ID'] == b['Track ID']:
        return False
    if 'Found' in a and a['Found']:
        return False
    if 'Found' in b and b['Found']:
        return False
    if a['Name'] != b['Name']:
        return False
    if 'Artist' in a and 'Artist' in b and a['Artist'] != b['Artist']:
        return False
    if 'Album' in a and 'Album' in b and a['Album'] != b['Album']:
        return False
    if 'Track Number' in a and 'Track Number' in b and a['Track Number'] != b['Track Number']:
        return False
    return True

for i in libA:
    for j in libA:
        trackA = libA[i]
        trackB = libA[j]
        if sameSong(trackA, trackB):
            if 'Found' not in trackA:
                trackA['Found'] = []
            if 'Found' not in trackB:
                trackB['Found'] = []
            trackA['Found'].append(trackB)
            trackB['Found'].append(trackA)

aOnly = sorted([libA[a] for a in libA if 'Found' in libA[a]], key=lambda a: a['Name'])

print('-- Duplicated --')
for track in aOnly:
    print(track)
    print('%s (%s) @ %s [%s]'%(track['Name'], track['Artist'] if 'Artist' in track else '??', track['Album'] if 'Album' in track else '??', urllib.request.unquote(urlparse(track['Location']).path) if 'Location' in track else 'DL?'))
    for t in track['Found']:
        print('\t%s (%s) @ %s [%s]'%(t['Name'], t['Artist'] if 'Artist' in t else '??', t['Album'] if 'Album' in t else '??', urllib.request.unquote(urlparse(t['Location']).path) if 'Location' in t else 'DL?'))
