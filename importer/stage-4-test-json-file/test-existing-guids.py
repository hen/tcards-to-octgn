import json
import re

guid_file='target/card_to_guid.json'
bot_cards_file='target/tmp/bot-cards.json'
battle_cards_file='target/tmp/battle-cards.json'
combiner_forms_file='target/tmp/combiner-forms.json'

# Load JSON files
bot_cards = json.load(open(bot_cards_file))
battle_cards = json.load(open(battle_cards_file))
combiner_cards = json.load(open(combiner_forms_file))

# Load GUID file  (#TODO: This needs to contain the Wave GUID too)
card_to_guid = json.load(open(guid_file))

# TODO: Move this to a library so the xml generation can use it
def tcard_to_card_id(card):
    if('Set' in card['fields']):
        wave=card['fields']['Set'].replace('Wave ', '')
        card_num=card['fields']['Card #'].split('/')[0]
        return f'W{wave}.{card_num}'
    else:   # Combiners for example
        name=card['fields']['Name']
        subtitle=card['fields']['Subtitle']
        return f'@{name} - {subtitle}'

for card in bot_cards['records']:
    card_id=tcard_to_card_id(card)
    if(card_id not in card_to_guid):
        print('Did not find bot card_id ' + card_id + ' in GUID file.')

for card in battle_cards['records']:
    card_id=tcard_to_card_id(card)
    if(card_id not in card_to_guid):
        print('Did not find battle card_id ' + card_id + ' in GUID file.')

for card in combiner_cards['records']:
    card_id=tcard_to_card_id(card)
    if(card_id not in card_to_guid):
        print('Did not find combiner card_id ' + card_id + ' in GUID file.')
