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

time.sleep(1) # wait until users collection has updated

USER_ID = client.find_one('users', selector={'username': UNAME}).get('_id')
print("User ID: " + USER_ID)


def main():
    # check_char()
    hp_write()


def hp_write():
    def update_callback(error, data):
        if error:
            print(error)
            return
        print(data)
    char_id = 'Mtx98jb3c3wWcrWPj'
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
