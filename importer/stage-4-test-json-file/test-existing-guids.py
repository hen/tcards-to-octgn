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

def tcard_to_card_id(card):
    wave=card['fields']['Set'].replace('Wave ', '')
    card_num=card['fields']['Card #'].split('/')[0]
    return f'W{wave}.{card_num}'

for card in bot_cards['records']:
    card_id=tcard_to_card_id(card)
    if(card_id not in card_to_guid):
        print('Did not find card_id ' + card_id + ' in GUID file.')
