import datetime
import sys

import re

text = """
<td class="greyText" width="307" valign="top" height="113">
<span class="redText">
<br>
Price:
<strong>
<br>
PropertyID:
<strong>207</strong>
<br>
Type:
<strong>Apartment</strong>
<br>
Bedrooms:
<strong>1</strong>
<br>
Bathrooms:
<strong>1</strong>
<br>
WC:
<strong>0</strong>
<br>
Pool:
<strong>Communal Pool </strong>
<br>
Building Area:
<strong>63.30sqm</strong>
<br>
District:
<strong> Pafos </strong>
<br>
Suburb:
<strong> Geroskipou </strong>
<br>
Title Deeds:
<strong>No</strong>
<br>
</td>
"""


def main(argv):
    global text
    ret = {}
    for item in text.split('<br>'):
        # print item
        p = re.compile('(?P<key>.*):<strong>(?P<value>.*)</strong>', re.DOTALL)
        m = p.match(item.replace("\n", ""))
        if m:
            key, value = m.groups()
            ret[key] = value

    print ret

if __name__ == '__main__':
    start_time = datetime.datetime.now()

    main(sys.argv[1:])

    end_time = datetime.datetime.now()
    c = end_time - start_time

    print '%d seconds %d microseconds' % (c.seconds, c.microseconds)
