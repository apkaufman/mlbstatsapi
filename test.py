import requests
import pprint

res = requests.get("http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='493316'")

pprint.pprint(res.json())
