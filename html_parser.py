from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


def html_request(url='https://u.gg/lol/champions/aatrox/build/'):#'https://champion.gg/champion/Aatrox/Top?'): #url as our current default parameter just pass the url we want
    request = Request(url,headers={'User-Agent': 'Mozilla/5.0'}) #define a known header or the itll complain with 403 ...
    mybytes = urlopen(request).read()
    html_doc = mybytes.decode("utf8")
    return html_doc

#read html data from url store data in string
html_doc = html_request()

print(type(html_doc)) #make sure html reponse is stored as a string ....
#print(html_doc)
html_data = BeautifulSoup(html_doc,'html.parser')
#print(html_data.prettify())

PERKS       =  html_data.find_all(attrs={"class":"perk perk-active"})
SHARDS      =  html_data.find_all(attrs={"class":"shard shard-active"})
SPELLS      =  html_data.find_all(attrs={"alt":"SummonerSpell"})
SKILLS_KEY  =  html_data.find_all(attrs={"alt":"ChampionSkill"})
SKILLS_NAME =  html_data.find_all(attrs={"class":"skill-name"})

for perks in PERKS:
    for items in perks:
        active_perks = re.findall(r'(\w+)\.png',items['src'])
        print(active_perks) #grab the image URL from dic
print("")
for shards in SHARDS:
    for items in shards:
        active_shards = re.findall(r'(\w+)\.png',items['src'])
        print(active_shards) #grab the image URL from dic
print("")
for spells in SPELLS:
    active_spells = re.findall(r'(\w+)\.png',spells['src'])
    print(active_spells)
print("")
for skills_key in SKILLS_KEY:
    active_skills_key = re.findall(r'(\w+)\.png',skills_key['src'])
    print(active_skills_key)
print("")
for skills_name in SKILLS_NAME:
    for items in skills_name:
        for indv_items in items:
            print(indv_items)
