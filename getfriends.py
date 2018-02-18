# Making a  GET friends/list request with Twitter API.


import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import os

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_input():
    try:
        user = input('Enter Twitter Account: ')
        friends = int(input('Enter number of friends to get (up to 200): '))
        if len(user) < 1 or friends > 200:
            print('Error. Invalid input.')
            get_input()
        return user, str(friends)
    except ValueError:
        print('Error. Invalid input.')
        get_input()


def request_friends(user, friends='100'):
    try:
       assert isinstance(user, str) and len(user) > 1, 'user type:string, len > 1'
       assert isinstance(friends, str) and int(friends) <= 200, 'friends type:string, < 200'
    except ValueError as err:
        print("Invalid args.", err)
        return None

    url = twurl.augment(TWITTER_URL,
                        {'screen_name': user, 'count': friends})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)

    jsn = json.loads(connection.read())
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'friends.json')
    with open(file_path, 'w', encoding='utf-8') as outfile:
        try:
            json.dump(jsn, outfile, ensure_ascii=False)
        except UnicodeEncodeError as err:
            print(err)
    print("Saved as json file: ", file_path)
    return file_path