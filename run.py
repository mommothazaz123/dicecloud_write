import os

import time
from MeteorClient import MeteorClient

UNAME = os.environ.get('DICECLOUD_USER', '')
PWD = os.environ.get('DICECLOUD_PWD', '').encode()

client = MeteorClient('ws://dicecloud.com/websocket', debug=True)
client.connect()
print("Connected")
while not client.connected:
    time.sleep(0.1)
client.login(UNAME, PWD)
print("Logged in")

time.sleep(1)  # wait until users collection has updated

USER_ID = client.find_one('users', selector={'username': UNAME}).get('_id')
print("User ID: " + USER_ID)

char_id = 'Mtx98jb3c3wWcrWPj'


def main():
    # check_char()
    test_id()


def test_id():
    client.insert('characters', {'name': 'DELETABLETESTCHAR', 'owner': USER_ID})


def spell_write():
    spellData = {'name': 'Fireball',
                 'description': "A bright streak flashes from your pointing finger to a point you choose within range then blossoms with a low roar into an explosion of flame. Each creature in a 20-foot radius must make a Dexterity saving throw. A target takes 8d6 fire damage on a failed save, or half as much damage on a successful one.\nThe fire spreads around corners. It ignites flammable objects in the area that aren't being worn or carried.\n**At Higher Levels:** When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 for each slot level above 3rd.",
                 'castingTime': '1 action', 'range': '150 feet', 'duration': 'Instantaneous', 'components.verbal': True,
                 'components.somatic': True, 'components.concentration': False,
                 'components.material': 'a tiny ball of bat guano and sulfur', 'ritual': False, 'level': 3,
                 'school': 'Evocation', 'charId': 'Mtx98jb3c3wWcrWPj',
                 'parent': {'id': 'hF8Q6FN5MFqz7Po76', 'collection': 'SpellLists'}, 'prepared': 'prepared'}

    client.insert('spells', spellData)


def hp_write():
    def update_callback(error, data):
        if error:
            print(error)
            return
        print(data)

    client.update('characters', {'_id': char_id}, {'$set': {"hitPoints.adjustment": -10}}, callback=update_callback)


def debug():
    def insert_callback(error, data):
        if error:
            print(error)
            return
        print(data)

    client.insert('characters', {'name': 'Test Character', 'owner': USER_ID},
                  callback=insert_callback)


if __name__ == '__main__':
    main()
    while True:
        pass
