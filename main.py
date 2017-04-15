import os
from mastodon import Mastodon
from getpass import getpass

client_cred_name = '.donburi_client.cred'
user_cred_name = '.donburi_user.cred'

def register(instance_url):
    Mastodon.create_app(
        'DonburiTairiku',
        to_file = client_cred_name,
        api_base_url = instance_url
    )

def login(instance_url, email, password):
    mastodon = Mastodon(
        client_id = client_cred_name,
        api_base_url = instance_url
    )
    mastodon.log_in(
        email,
        password,
        to_file = user_cred_name
    )

def toot(instance_url):
    mastodon = Mastodon(
        client_id = client_cred_name, 
        access_token = user_cred_name,
        api_base_url = instance_url
    )
    mastodon.toot(input('Toot: '))

instance_url = os.environ.get('MASTODON_INSTANCE_URL')
if instance_url == None:
    print('environment variable MASTODON_INSTANCE_URL was not set.')
    instance_url = input('Instance URL: ')
if not os.access(client_cred_name, os.F_OK):
    register(instance_url)
if not os.access(user_cred_name, os.F_OK):
    email = input('email: ')
    password = getpass('your password: ')
    login(instance_url, email, password)
toot(instance_url)
