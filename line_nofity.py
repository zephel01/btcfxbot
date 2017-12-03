#coding:UTF-8
import requests

line_notify_token = 'Your Token'
line_notify_api = 'https://notify-api.line.me/api/notify'
message = 'test massage'


payload = {'message': message}
headers = {'Authorization': 'Bearer ' + line_notify_token} 
line_notify = requests.post(line_notify_api, data=payload, headers=headers)

