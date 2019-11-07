import os
import xml.etree.ElementTree as ET
from collections import OrderedDict
import json
import re

# Need to clone the OCTGN_TF repository. 
# TODO: Make this less hardcoded
data_location='../OCTGN_TF/f44befce-4d6d-4fb9-a286-9585f36aece9/sets/'
output_file='target/card_to_guid.json'

card_to_guid = OrderedDict()

for set_directory in os.listdir(data_location):
    for filename in os.listdir(os.path.join(data_location, set_directory)):
        if(filename == 'set.xml'):
            root = ET.parse( os.path.join(data_location, set_directory, filename) ).getroot()
            octgn_wave = root.attrib['name'].replace('Wave ', '')
            for card_tag in root.findall('cards/card'):
                octgn_id = card_tag.attrib['id']
                octgn_name = card_tag.attrib['name']
                octgn_cardnum = card_tag.find('./property[@name="Card Number"]').attrib['value']
                # Fix the OCTGN data not being consistent
                octgn_cardnum = re.sub(r"^[^ ]* ", '', octgn_cardnum)
                octgn_cardnum = re.sub(r"^[UCR]", '', octgn_cardnum)
                if(octgn_cardnum == ""):
                    print('Warning: No Card ID for ' + octgn_name + ', using the name')
                    card_to_guid[octgn_name] = octgn_id
                    continue

                octgn_cardtype = card_tag.find('./property[@name="Type"]').attrib['value']
                if(octgn_cardtype == 'Character' and not octgn_cardnum.startswith('T')):
                    bot='T'
                else:
                    bot=''

                card_id='W{}.{}{}'.format(octgn_wave, bot, octgn_cardnum)
                card_to_guid[card_id] = octgn_id

output = json.dumps(card_to_guid, indent=4)
with open(output_file, 'w') as fout:
    print(output, file=fout)
fout.close()
