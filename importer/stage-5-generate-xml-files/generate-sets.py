import json
import pystache

bot_cards_file='target/tmp/bot-cards.json'
battle_cards_file='target/tmp/battle-cards.json'
combiner_forms_file='target/tmp/combiner-forms.json'

guid_file='target/card_to_guid.json'

# TODO: COPY OF function in json tester
def tcard_to_card_id(card):
    if('Set' in card['fields']):
        wave=card['fields']['Set'].replace('Wave ', '')
        card_num=card['fields']['Card #'].split('/')[0]
        return f'W{wave}.{card_num}'
    else:   # Combiners for example
        name=card['fields']['Name']
        subtitle=card['fields']['Subtitle']
        return f'@{name} - {subtitle}'




# Load JSON files
bot_cards = json.load(open(bot_cards_file))
battle_cards = json.load(open(battle_cards_file))
combiner_cards = json.load(open(combiner_forms_file))

# Load GUID file  (#TODO: This needs to contain the Wave GUID too)
card_to_guid = json.load(open(guid_file))

# Read in XML Template
template = open("importer/stage-5-generate-xml-files/set.template","r").read()

output_files_by_set = {}

# For each Card in JSON file:
for card in bot_cards['records']:
    if(card['fields']['Name']=='Bumblebee'):
        wave=card['fields']['Set']    # This will be a problem for Combiner Forms which have no Set
        card_id=tcard_to_card_id(card)
        if(card_id in card_to_guid):
            guid=card_to_guid[card_id]
        else:
            guid="UNKNOWN"
        print(pystache.render(template, {'card' : card['fields'], 'guid' : guid}))
#        output_files_by_set[wave] += pystache.render(template, {'card' : card, 'guid' : guid})

# Output each set to a set.xml file
#print(output_files_by_set['Wave 1'])
