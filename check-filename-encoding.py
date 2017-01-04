import chardet
import os
for root, dirs, names in os.walk('.'):
    for n in names:
        if (chardet.detect(n)['encoding'] not in ['utf-8', 'ascii']):
            print '%s/%s => %s (%s)' % (root, n, chardet.detect(n)['encoding'], chardet.detect(n)['confidence'])
