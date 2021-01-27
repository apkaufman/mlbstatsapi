import requests
import pprint

isactive = input('Is this player active? Answer yes or no. ')

if str.lower(isactive) == 'yes':
    isactive = 'Y'
else:
    isactive = 'N'

player_last_name = str.lower(input('What is this player\'s last name? '))
player_last_name = player_last_name + "%25"

player_info = requests.get("http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='" + isactive + "'&name_part='" + player_last_name + "'")

pprint.pprint(player_info.json())
