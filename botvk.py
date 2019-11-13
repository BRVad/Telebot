# -*- coding: utf-8 -*-
import json
import requests
import vk
global token_vk


token_vk = '69fdbd8b69fdbd8b69fdbd8b946990530e669fd69fdbd8b3434849b35dade86d1822671'
session = vk.Session(access_token=token_vk)
api = vk.API(session)


def take_posts():
    version = 5.103
    domain = 'ProTestingPro'
    count = 10
    offset = 0
    token_vk = '69fdbd8b69fdbd8b69fdbd8b946990530e669fd69fdbd8b3434849b35dade86d1822671'


    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token_vk,
                                'v': version,
                                'domain': domain,
                                'count': count,
                                'offset': offset
                            }
                            )
    data = response.json()['response']['items']
    return data


def look_in_json():
    d = take_posts()
    with open('dates.json', 'w') as f:
        json.dump(d, f, indent=2)


# print(take_posts())
# def get_msg():
#     global get_from
#     if messages['count'] >= 1:
#             id = messages['items'][0]['last_message']['from_id']
#             body = messages['items'][0]['last_message']['text']
#             get_from = {'chat_id': str(id), 'text': str(body)}
#             return get_from
#
#
# def send_msg():
#     try:
#         vk.method('messages.send', {'peer_id': get_from['chat_id'], 'message': 'hi', 'random_id': random.randint(1, 21565465313)})
#     except:
#         pass
# def file_writer(data):
#     with open('my_wall.csv', 'w') as file:
#         pen = csv.writer(file)
#         pen.writerow(('likes', 'body', 'url'))
#         for post in data:
#             try:
#                 if post['attachments'][0]['type'] == 'photo':
#                     img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
#                 else:
#                     img_url = 'pass'
#             except:
#                 pass
#             pen.writerow((post['likes']['count'], post['text'], img_url))