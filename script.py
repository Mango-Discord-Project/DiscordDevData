import json

string = """da	Danish	Dansk
de	German	Deutsch
en-GB	English, UK	English, UK
en-US	English, US	English, US
es-ES	Spanish	Español
fr	French	Français
hr	Croatian	Hrvatski
it	Italian	Italiano
lt	Lithuanian	Lietuviškai
hu	Hungarian	Magyar
nl	Dutch	Nederlands
no	Norwegian	Norsk
pl	Polish	Polski
pt-BR	Portuguese, Brazilian	Português do Brasil
ro	Romanian, Romania	Română
fi	Finnish	Suomi
sv-SE	Swedish	Svenska
vi	Vietnamese	Tiếng Việt
tr	Turkish	Türkçe
cs	Czech	Čeština
el	Greek	Ελληνικά
bg	Bulgarian	български
ru	Russian	Pусский
uk	Ukrainian	Українська
hi	Hindi	हिन्दी
th	Thai	ไทย
zh-CN	Chinese, China	中文
ja	Japanese	日本語
zh-TW	Chinese, Taiwan	繁體中文
ko	Korean	한국어"""

data = {}
for line in string.split('\n'):
    key, *value = line.split('\t')
    data[key] = [value[0], value[1].replace(' ', '').split(',')]

print(json.dumps(data, indent=4, ensure_ascii=False))