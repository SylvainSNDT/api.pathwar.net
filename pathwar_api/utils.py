# -*- coding: utf-8 -*-

import random
import urllib

from flask import current_app


def request_get_user(request):
    auth = request.authorization
    if auth.get('username'):
        if auth.get('password'):  # user:pass
            username = auth.get('username')
            try:
                username = urllib.unquote(username)
            except:
                pass
            return current_app.data.driver.db['raw-users'].find_one({
                '$or': [
                    {'login': username},
                    {'email': username},
                ]
                # 'active': True,  # FIXME: Reenable later
            })
        else:  # token
            user_token = current_app \
                .data \
                .driver \
                .db['raw-user-tokens'] \
                .find_one({
                    'token': auth.get('username')
                })
            if user_token:
                return current_app \
                    .data \
                    .driver \
                    .db['raw-users'] \
                    .find_one({'_id': user_token['user']})
    return None


def is_restricted_word(input_):
    input_ = input_.lower()

    restricted_words = (
        'supportdetails',
        'support-details',
        'stacks',
        'imulus',
        'github',
        'twitter',
        'facebook',
        'google',
        'apple',
        'about',
        'account',
        'activate',
        'add',
        'admin',
        'administrator',
        'api',
        'app',
        'apps',
        'archive',
        'archives',
        'auth',
        'blog',
        'cache',
        'cancel',
        'careers',
        'cart',
        'changelog',
        'checkout',
        'codereview',
        'compare',
        'config',
        'configuration',
        'connect',
        'contact',
        'create',
        'delete',
        'direct_messages',
        'documentation',
        'download',
        'downloads',
        'edit',
        'email',
        'employment',
        'enterprise',
        'faq',
        'favorites',
        'feed',
        'feedback',
        'feeds',
        'fleet',
        'fleets',
        'follow',
        'followers',
        'following',
        'friend',
        'friends',
        'gist',
        'group',
        'groups',
        'help',
        'home',
        'hosting',
        'hostmaster',
        'idea',
        'ideas',
        'index',
        'info',
        'invitations',
        'invite',
        'is',
        'it',
        'job',
        'jobs',
        'json',
        'language',
        'languages',
        'lists',
        'login',
        'logout',
        'logs',
        'mail',
        'map',
        'maps',
        'mine',
        'mis',
        'news',
        'oauth',
        'oauth_clients',
        'offers',
        'openid',
        'order',
        'orders',
        'organizations',
        'plans',
        'popular',
        'post',
        'postmaster',
        'privacy',
        'projects',
        'put',
        'recruitment',
        'register',
        'remove',
        'replies',
        'root',
        'rss',
        'sales',
        'save',
        'search',
        'security',
        'sessions',
        'settings',
        'shop',
        'signup',
        'sitemap',
        'ssl',
        'ssladmin',
        'ssladministrator',
        'sslwebmaster',
        'status',
        'stories',
        'styleguide',
        'subscribe',
        'subscriptions',
        'support',
        'sysadmin',
        'sysadministrator',
        'terms',
        'tour',
        'translations',
        'trends',
        'unfollow',
        'unsubscribe',
        'update',
        'url',
        'user',
        'weather',
        'webmaster',
        'widget',
        'widgets',
        'wiki',
        'ww',
        'www',
        'wwww',
        'xfn',
        'xml',
        'xmpp',
        'yaml',
        'yml',
        'chinese',
        'mandarin',
        'spanish',
        'english',
        'bengali',
        'hindi',
        'portuguese',
        'russian',
        'japanese',
        'german',
        'wu',
        'javanese',
        'korean',
        'french',
        'vietnamese',
        'telugu',
        'chinese',
        'marathi',
        'tamil',
        'turkish',
        'urdu',
        'min-nan',
        'jinyu',
        'gujarati',
        'polish',
        'arabic',
        'ukrainian',
        'italian',
        'xiang',
        'malayalam',
        'hakka',
        'kannada',
        'oriya',
        'panjabi',
        'sunda',
        'panjabi',
        'romanian',
        'bhojpuri',
        'azerbaijani',
        'farsi',
        'maithili',
        'hausa',
        'arabic',
        'burmese',
        'serbo-croatian',
        'gan',
        'awadhi',
        'thai',
        'dutch',
        'yoruba',
        'sindhi',
    )
    return input_ in restricted_words


def generate_name(sep='-'):
    """ Python port of github.com/docker/docker names-generator.go
    """
    left = [
        "admiring",
        "adoring",
        "agitated",
        "angry",
        "backstabbing",
        "berserk",
        "boring",
        "clever",
        "cocky",
        "compassionate",
        "condescending",
        "cranky",
        "desperate",
        "determined",
        "distracted",
        "dreamy",
        "drunk",
        "ecstatic",
        "elated",
        "elegant",
        "evil",
        "fervent",
        "focused",
        "furious",
        "gloomy",
        "goofy",
        "grave",
        "happy",
        "high",
        "hopeful",
        "hungry",
        "insane",
        "jolly",
        "jovial",
        "kickass",
        "lonely",
        "loving",
        "mad",
        "modest",
        "naughty",
        "nostalgic",
        "pensive",
        "prickly",
        "reverent",
        "romantic",
        "sad",
        "serene",
        "sharp",
        "sick",
        "silly",
        "sleepy",
        "stoic",
        "stupefied",
        "suspicious",
        "tender",
        "thirsty",
        "trusting",
    ]
    right = [
        "albattani",
        "almeida",
        "archimedes",
        "ardinghelli",
        "babbage",
        "banach",
        "bardeen",
        "brattain",
        "shockley",
        "bartik",
        "bell",
        "blackwell",
        "bohr",
        "brown",
        "carson",
        "colden",
        "cori",
        "cray",
        "curie",
        "darwin",
        "davinci",
        "einstein",
        "elion",
        "engelbart",
        "euclid",
        "fermat",
        "fermi",
        "feynman",
        "franklin",
        "galileo",
        "goldstine",
        "goodall",
        "hawking",
        "heisenberg",
        "hodgkin",
        "hoover",
        "hopper",
        "hypatia",
        "jang",
        "jones",
        "kilby",
        "noyce",
        "kirch",
        "kowalevski",
        "lalande",
        "leakey",
        "lovelace",
        "lumiere",
        "mayer",
        "mccarthy",
        "mcclintock",
        "mclean",
        "meitner",
        "mestorf",
        "morse",
        "newton",
        "nobel",
        "payne",
        "pare",
        "pasteur",
        "perlman",
        "pike",
        "poincare",
        "poitras",
        "ptolemy",
        "ritchie",
        "thompson",
        "rosalind",
        "sammet",
        "sinoussi",
        "stallman",
        "swartz",
        "tesla",
        "torvalds",
        "turing",
        "wilson",
        "wozniak",
        "wright",
        "yalow",
        "yonath",
    ]
    return random.choice(left) + sep + random.choice(right)
