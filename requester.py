# -*- coding: utf-8 -*-
api_token='' # Enter your instagram auth token 
aurl='https://api.instagram.com/v1/media/popular?access_token'+api_token
import json,requests,sched,time
s = sched.scheduler(time.time, time.sleep)
def online_call(sc):
	session = requests.session()
  headers = {
		"User-Agent":"User-Agent": "Mozilla\/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko\/20100101 Firefox\/57.0"
        } 
	r = requests.post(url = aurl,data='',headers=headers)
	data_rec = r.text
	print(data_rec)
	s.enter(60, 1, online_call, (sc,))
s.enter(60, 1, online_call, (s,))
s.run()
sleep(1)
