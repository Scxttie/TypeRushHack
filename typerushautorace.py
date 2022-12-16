import requests, time
from colorama import Fore

i = 1

while(i <= 5):


  s = requests.Session()

  user_req_login = "https://www.typerush.com/api/login"
  logindetails = {"email":"f39083f2@gmail.com","password":"g3QUJrvm.aKpR9a"}

  x = s.post(user_req_login, json = logindetails)

  print(x.text)
  if x.status_code == 200:
    print("Successfully Logged in!")
  else:
    print("Login Failed")

  playerdata = s.get("https://www.typerush.com/api/user")

  if playerdata.status_code == 200:
    print(Fore.GREEN+"""Player Data has loaded. Your Login Session is working!"""+Fore.WHITE)
  else:
    print(Fore.RED+"""Failed To Load Player Data."""+Fore.WHITE)

  racecreateurl = "https://www.typerush.com/api/game/create"
  racecreatedata = {"gameId":"game","token":"thisgeneratesonitsown","gameMode":"car","useApi":"true",   "leagueId":"6b2e01a8fdce89d973cc21f8a3544a48"}

  x1 = s.post(racecreateurl, json = racecreatedata)

  if x1.status_code == 200:
    print(Fore.GREEN+"""Race successfully Created!"""+Fore.WHITE)

  racestarturl = "https://www.typerush.com/api/games/start"
  racestartdata = {"gameId":"game","token":x1.json()["token"],"timestamp":1671213518025,"type":"StartGameRequest","gameData":{"gameStatus":"starting","clientVersion":"5.78","gameMode":"race","gameType":"1"}}

  x2 = s.post(racestarturl, json = racestartdata)

  print(Fore.GREEN+"""Race Has Started! Wait 1 Second Before It Loads Stats."""+Fore.WHITE)

  racestopurl = "https://www.typerush.com/api/games/stop"
  racestopdata = {"gameId":"game","token":x1.json()  ["token"],"timestamp":1671212711663,"type":"StopGameRequest","raceRecord":  {"hits":"999999999999","errorHits":"0"},"gameData":  {"status":"stopping","type":"1","time":0,"wpm":"9999999999","hits":99999999999999,"errorHits":0  ,"accuracy":"99999","typed":"Easter is one of the loveliest holidays. Just like other big   holidays, it is an important commercial event. Enough for experts to say that on Easter,   Americans spend more than fourteen billion dollars","allTyped":"Easter is one of the loveliest   holiodays. Just lioke other big holnidays, it is an important commcercial event. Enough fore   xperxpecrrst s to say that on Easter, Aemericans spend more then an fourtenen mbiullion   daollars","headStart":0}}

  x3 = s.post(racestopurl, json = racestopdata)

  if x3.status_code == 200:
    print(Fore.GREEN+"""Stats Have Been Modded!"""+Fore.WHITE)
  else:
    print(Fore.RED+"""Stats Failed to Mod."""+Fore.WHITE)
