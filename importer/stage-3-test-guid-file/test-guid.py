import json
import re

# TODO: Consider a test framework
input_file='target/card_to_guid.json'
guid_re = re.compile(r"^........-....-....-....-............$")
card_id_re = re.compile(r"^W[0-9][CP]?\.T?0?[0-9][0-9]?$")
card_id_re2 = re.compile(r"^@")

def good_card_id(card_id):
    if(not card_id_re.match(card_id) and not card_id_re2.match(card_id)):
        return "ERROR: Card ID has incorrect format: {}".format(card_id)
    else:
        return None

def good_guid(guid):
    if(not guid_re.match(guid)):
        return "ERROR: GUID has incorrect format: {}".format(guid)
    else:
        return None

def test(error):
    if(error):
        print(error)

with open(input_file) as json_file:
    data = json.load(json_file)

    for key, value in data.items():
        test(good_card_id(key))
        test(good_guid(value))
