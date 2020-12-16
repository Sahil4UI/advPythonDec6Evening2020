import json
import urllib.request as url
import cgi

formdata = cgi.FieldStorage()

player_name = formdata.getvalue('name')
player_name=player_name.replace(" ","%20")
path=f"https://cricapi.com/api/playerFinder?apikey=RiPTCn1FNCUNmr3QzfBy03EMIJG2&name={player_name}"
res=url.urlopen(path)
data = json.load(res)
pid=data['data'][0]['pid']

path=f"https://cricapi.com/api/playerStats?apikey=RiPTCn1FNCUNmr3QzfBy03EMIJG2&pid={pid}"
res= url.urlopen(path)
data = json.load(res)
name =data['fullName']
bat_style = data['battingStyle']
bowl_style = data['bowlingStyle']
profile = data['profile']
age = data['currentAge']
role = data['playingRole']
img = data['imageURL']


print("Content-type:text/html\r\n\r\n")
print(f"""<!DOCTYPE html>
<!--html5 declaration-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
     <h2>Data for {name}</h2>
      <p><b>Profile : </b>{profile}</p>
      <img src={img}>
</body>
</html>""")