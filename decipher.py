# Module for deciphering data from json files
# received with Twitter API GET friends/list request


import json
from decipherparams import userdict_params, relationdict_params


def friendslist(data):
    """
    Returns list of tuples of (username, screen name, id) for every user.
    """
    return [(u['name'], u['screen_name'], u['id']) for u in data['users']]


def usernameslist(data):
    """
    Returns list of usernames of all users.
    """
    return [u['name'] for u in data['users']]


def idslist(data):
    """
    Returns list of user id's of all users.
    """
    return [u['id'] for u in data['users']]


def userdict(data, param='name'):
    """
    Returns a dictionary user_id :  param for all users in data.
    Params display info about user's profile.
    -----------------------------------------------------------
    possible params:
    "id_str"                       - user id as a string
    "name"                         - username
    "screen_name"                  - users's screen name
    "location"                     - user's location
    "description"                  - description of users's profile
    "url"                          - user's URL stated in description
    "protected"                    - bool whether account is protected or not
    "followers_count"              - number of user's followers
    "friends_count"                - number of people followed by user
    "listed_count"                 - number of people in user's lists
    "created_at"                   - date and time when account was created
    "favourites_count"             - number of tweets liked by user
    "utc_offset":                  - the offset from GMT/UTC in seconds
    "time_zone"                    - user's set time zone
    "geo_enabled"                  - bool whether geolocation is enabled or not
    "verified"                     - bool whether profile is verified or not
    "statuses_count"               - number of user's tweets
    "lang"                         - user's profile language
    "contributors_enabled"         - indicates that the user has account with 
    “contributor mode” enabled, allowing for Tweets issued by the user to be 
    co-authored by another account.
    "is_translator"                - bool whether translator is enabled or not
    "is_translation_enabled"       - bool whether translation is enabled or not
    "profile_background_color"     - code of profile background color
    "profile_background_image_url" - http link to profile background image
    "profile_background_image_url_https" - https link to profile background img
    "profile_background_tile"      - bool whether translation is enabled or not
    "profile_image_url"            - http link to profile image
    "profile_image_url_https"      - https link to profile image
    "profile_link_color"           - code of profile link color
    "profile_sidebar_border_color" - code of profile sidebar border
    "profile_sidebar_fill_color"   - code of profile sidebar fill
    "profile_text_color"           - code of profile text color
    "profile_use_background_image" - bool whether profile uses background img
    "has_extended_profile"         - bool whether profile has extended profile
    "default_profile"              - bool whether it is a default profile
    "default_profile_image"        - bool info whether profile image is default
    -----------------------------------------------------------------
    "all"                          - includes all the possible params
    """
    try:
        if param in userdict_params:
            d = {u['id']: u[param] for u in data['users']}
        elif param == "all":
            d = {u['id']: {p: u[p] for p in userdict_params} 
            for u in data['users']}
        else:
            print("Invalid param argument")
            return None
        return d
    except KeyError as err:
        print("Can't find info for every user on key:", err)


def relationdict(data, param='following'):
    """
    Returns a dictionary user_id: param or user_id: dict[params] if param="all"
    Params display info about relations between authorized
    and specified user's profiles for every specified user in data.
    --------------------------------------------------------------------
    Possible params:
    "muting"              - bool whether authorized user had muted specified
    "following"           - bool whether authorized user is following specified
    "live_following"      - bool whether user is live following specified
    "follow_request_sent" - bool whether user sent followrequest to specified
    "notifications"       - bool if user enabled notifications from specified
    "blocking"            - bool whether authorized user had blocked specified
    "blocked_by"          - bool whether authorized user isblocked by specified
    "translator_type"     - info about translator type set for specified user
    ---------------------------------------------------------------------
    "all"                 - includes all the possible params
    """
    try:
        if param in relationdict_params:
            d = {u['id']: u[param] for u in data['users']}
        elif param == "all":
            d = {u['id']: {p: u[p] for p in relationdict_params}
            for u in data['users']}
        else:
            print("Invalid param argument")
            return None
        return d
    except KeyError as err:
        print("Can't find info for every user on key:", err)


def userstatus(data):
    """
    Returns a dictionary id : status with info
    about latest status of every user in data.
    status - dict
    """
    return {u['id']: u["status"] for u in data['users']}


def userentities(data):
    """
    Returns a dictionary id : entities with info
    about user entities with links for every user in data.
    entities - dict
    """
    return {u['id']: u["entities"] for u in data['users']}


# filename = "json/friends200ippvch.json"
# data = json.load(open(filename, encoding='utf-8'))
# print(idslist(data)[:10])
# print(userdict(data))
# print(relationdict(data, param='following'))
