import datetime
import sys

import re

text = """
<td width="307" valign="top" height="113" class="greyText">
                <span class="redText"><strong>
                Resale                </strong></span><br>





                 Price: <strong><span onclick="showAlbum('detailedInfo207', 'ping.php?propertyID=207', '400');" style="cursor:pointer" class="tealText">
                 75,000 </span></strong><br>

                  PropertyID: <strong>207</strong><br>
                  Type: <strong>Apartment</strong><br>

                  Bedrooms: <strong>1</strong><br>
                  Bathrooms: <strong>1</strong><br>
                  WC: <strong>0</strong><br>
                  Pool:
                  <strong>Communal Pool                  </strong><br>
                  Building Area: <strong>63.30sqm</strong><br>
                  District:<strong> Pafos </strong><br>
                  Suburb:<strong> Geroskipou </strong><br>
                  Title Deeds: <strong>No</strong><br>                   </td>
"""


def main(argv):
    global text
    ret = {}
    for item in text.split('<br>'):
        item = re.sub('\s+', ' ', item)
        p = re.compile('(?P<key>.*(?:\s.*)):\s?<strong>(?P<value>.*)</strong>', re.DOTALL)
        item = item.replace("\n", "")
        m = p.match(item)
        if m:
            key, value = m.groups()
            ret[key.strip()] = value.strip()

    import pprint
    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(ret)


if __name__ == '__main__':
    start_time = datetime.datetime.now()

    main(sys.argv[1:])

    end_time = datetime.datetime.now()
    c = end_time - start_time

    print '%d seconds %d microseconds' % (c.seconds, c.microseconds)
