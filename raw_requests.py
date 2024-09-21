# get time requst
import requests
from bs4 import BeautifulSoup
import datetime
import time
import sys


# headers = {
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9',
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     # 'cookie': 'PHPSESSID=vsevr3kaackqo5uam139nda8i0; isLoggedIn=1; __cf_bm=_rE0jDmjVxqOoyLcj6P8BhvSssjiQEpBGHqLR9zfxr8-1726628430-1.0.1.1-HJPwlCCxLsDSJZ7nGrt7GsF874LsMIL_z4BuyyNe_TXT6OwT78lL3TXWZfpmKzUNZcCR4kUvOvbKb_kTKZxVYw; SessionExpirationTime=1726657327',
#     'dnt': '1',
#     'origin': 'https://ctm.clubautomation.com',
#     'priority': 'u=1, i',
#     'referer': 'https://ctm.clubautomation.com/event/reserve-court-new',
#     'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
#     'sec-ch-ua-mobile': '?1',
#     'sec-ch-ua-platform': '"Android"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest',
# }

# params = {
#     'ajax': 'true',
# }

# data = {
#     'reservation-list-page': '1',
#     'user_id': '96192',
#     'event_member_token_reserve_court': '8efaf03341f9996523cfa8defe2f0357',
#     'current_guest_count': '0',
#     'component': '42',
#     'club': '-1',
#     'host': '96192',
#     'ball_machine': '0',
#     'date': '09/21/2024',
#     'interval': '30',
#     'timeFrom': '8',
#     'timeTo': '0',
#     'time-reserve': '1726949700',
#     'location-reserve': '9',
#     'surface-reserve': '0',
#     'courtsnotavailable': '',
#     'join-waitlist-case': '1',
#     'is_confirmed': '1',
# }

# response = requests.post(
#     'https://ctm.clubautomation.com/event/reserve-court-new-do',
#     params=params,
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )


# print(response.text)
# print('Cookies')
# print(response.cookies)
# print('Headers')
# print(response.headers)


cookies = {
    'PHPSESSID': 'vsevr3kaackqo5uam139nda8i0',
    'isLoggedIn': '1',
    '__cf_bm': '_rE0jDmjVxqOoyLcj6P8BhvSssjiQEpBGHqLR9zfxr8-1726628430-1.0.1.1-HJPwlCCxLsDSJZ7nGrt7GsF874LsMIL_z4BuyyNe_TXT6OwT78lL3TXWZfpmKzUNZcCR4kUvOvbKb_kTKZxVYw',
    'SessionExpirationTime': '1726657327',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'content-length': '0',
    # 'cookie': 'PHPSESSID=79f7ck96fjf7t8gvvlopnd0olo; __cf_bm=o51.lhcaAV5wsxdm_MN9e3Q2xMXmTSS2NwFLOpwsIfI-1726535404-1.0.1.1-3ffSIML9u4oafi6xh__NG0fiJHIsyb46cGnzVyzBAN2Gst16eYskvzeFc_Nb7ktTkgV02WtOn.qcyxAjMgMHMg; isLoggedIn=1; SessionExpirationTime=1726564333',
    'dnt': '1',
    'origin': 'https://ctm.clubautomation.com',
    'priority': 'u=1, i',
    'referer': 'https://ctm.clubautomation.com/member',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
    'x-instana-l': '1,correlationType=web;correlationId=a7abd054acd6b41c',
    'x-instana-s': 'a7abd054acd6b41c',
    'x-instana-t': 'a7abd054acd6b41c',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.post('https://ctm.clubautomation.com/index/update-session-expiration', cookies=cookies, headers=headers)

print(response.text)
print('Cookies')
print(response.cookies)
print('Headers')
print(response.headers)


sys.exit()

# Cancel reservation walrustwins

import requests

cookies = {
    'PHPSESSID': 'vsevr3kaackqo5uam139nda8i0',
    'isLoggedIn': '1',
    '__cf_bm': '_rE0jDmjVxqOoyLcj6P8BhvSssjiQEpBGHqLR9zfxr8-1726628430-1.0.1.1-HJPwlCCxLsDSJZ7nGrt7GsF874LsMIL_z4BuyyNe_TXT6OwT78lL3TXWZfpmKzUNZcCR4kUvOvbKb_kTKZxVYw',
    'SessionExpirationTime': '1726657913',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=vsevr3kaackqo5uam139nda8i0; isLoggedIn=1; __cf_bm=_rE0jDmjVxqOoyLcj6P8BhvSssjiQEpBGHqLR9zfxr8-1726628430-1.0.1.1-HJPwlCCxLsDSJZ7nGrt7GsF874LsMIL_z4BuyyNe_TXT6OwT78lL3TXWZfpmKzUNZcCR4kUvOvbKb_kTKZxVYw; SessionExpirationTime=1726657913',
    'dnt': '1',
    'origin': 'https://ctm.clubautomation.com',
    'priority': 'u=1, i',
    'referer': 'https://ctm.clubautomation.com/event/reserve-court-new',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'ajax': 'true',
}

data = {
    'id': '2285872',
    'confirm': '1',
}

response = requests.post(
    'https://ctm.clubautomation.com/event/cancel-court-time-do',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

print(response.text)
print('Cookies')
print(response.cookies)
print('Headers')
print(response.headers)


















cookies = {
    'PHPSESSID': '79f7ck96fjf7t8gvvlopnd0olo',
    '__cf_bm': 'o51.lhcaAV5wsxdm_MN9e3Q2xMXmTSS2NwFLOpwsIfI-1726535404-1.0.1.1-3ffSIML9u4oafi6xh__NG0fiJHIsyb46cGnzVyzBAN2Gst16eYskvzeFc_Nb7ktTkgV02WtOn.qcyxAjMgMHMg',
    'isLoggedIn': '1',
    'SessionExpirationTime': '1726570333',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    # 'content-length': '0',
    # 'cookie': 'PHPSESSID=79f7ck96fjf7t8gvvlopnd0olo; __cf_bm=o51.lhcaAV5wsxdm_MN9e3Q2xMXmTSS2NwFLOpwsIfI-1726535404-1.0.1.1-3ffSIML9u4oafi6xh__NG0fiJHIsyb46cGnzVyzBAN2Gst16eYskvzeFc_Nb7ktTkgV02WtOn.qcyxAjMgMHMg; isLoggedIn=1; SessionExpirationTime=1726564333',
    'dnt': '1',
    'origin': 'https://ctm.clubautomation.com',
    'priority': 'u=1, i',
    'referer': 'https://ctm.clubautomation.com/member',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
    'x-instana-l': '1,correlationType=web;correlationId=a7abd054acd6b41c',
    'x-instana-s': 'a7abd054acd6b41c',
    'x-instana-t': 'a7abd054acd6b41c',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.post('https://ctm.clubautomation.com/index/update-session-expiration', cookies=cookies, headers=headers)

print(response.text)
print("Cookies")
print(response.cookies)






















# Get times
cookies = {
    'PHPSESSID': '8kjurbhmglt992j5liejvf5k5k',
    'isLoggedIn': '1',
    'SessionExpirationTime': '1726403249',
    '__cf_bm': 'scuHUAPn8HriF3PaPm4kPvlMemDsqATIKWjsu61tPto-1726374449-1.0.1.1-G0c1ueAda1tNh2afyEtIosiVkLcHi77v7TmWi9F7bu.mC7cK82Lv.CaMlLvUQV8X9uytmyBCfswQ62YM.5G6Cg',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=8kjurbhmglt992j5liejvf5k5k; isLoggedIn=1; SessionExpirationTime=1726403249; __cf_bm=scuHUAPn8HriF3PaPm4kPvlMemDsqATIKWjsu61tPto-1726374449-1.0.1.1-G0c1ueAda1tNh2afyEtIosiVkLcHi77v7TmWi9F7bu.mC7cK82Lv.CaMlLvUQV8X9uytmyBCfswQ62YM.5G6Cg',
    'origin': 'https://ctm.clubautomation.com',
    'priority': 'u=1, i',
    'referer': 'https://ctm.clubautomation.com/event/reserve-court-new',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'ajax': 'true',
}

data = {
    'reservation-list-page': '1',
    'user_id': '94299',
    'event_member_token_reserve_court': 'ee4a79e3bece4a506eda309bcf184f75',
    'current_guest_count': '0',
    'component': '42',
    'club': '-1',
    'host': '94299',
    'ball_machine': '0',
    'date': '09/18/2024',
    'interval': '60',
    'timeFrom': '6',
    'timeTo': '0',
    'time-reserve': '',
    'location-reserve': '',
    'surface-reserve': '',
    'courtsnotavailable': '',
    'join-waitlist-case': '0',
}

response = requests.post(
    'https://ctm.clubautomation.com/event/reserve-court-new',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

soup = BeautifulSoup(response.text, 'html.parser')

# Find the table with id 'times-to-reserve'
times_table = soup.find('table', id='times-to-reserve')

# Extract times from the <a> tags within the table
times = []
if times_table:
    for a_tag in times_table.find_all('a'):
        time_text = a_tag.get_text(strip=True)
        times.append(time_text)

print(times)



# Choosing time

cookies = {
    'PHPSESSID': '8kjurbhmglt992j5liejvf5k5k',
    'isLoggedIn': '1',
    '__cf_bm': 'scuHUAPn8HriF3PaPm4kPvlMemDsqATIKWjsu61tPto-1726374449-1.0.1.1-G0c1ueAda1tNh2afyEtIosiVkLcHi77v7TmWi9F7bu.mC7cK82Lv.CaMlLvUQV8X9uytmyBCfswQ62YM.5G6Cg',
    'SessionExpirationTime': '1726403863',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=8kjurbhmglt992j5liejvf5k5k; isLoggedIn=1; __cf_bm=scuHUAPn8HriF3PaPm4kPvlMemDsqATIKWjsu61tPto-1726374449-1.0.1.1-G0c1ueAda1tNh2afyEtIosiVkLcHi77v7TmWi9F7bu.mC7cK82Lv.CaMlLvUQV8X9uytmyBCfswQ62YM.5G6Cg; SessionExpirationTime=1726403863',
    'origin': 'https://ctm.clubautomation.com',
    'priority': 'u=1, i',
    'referer': 'https://ctm.clubautomation.com/event/reserve-court-new',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'ajax': 'true',
}

data = {
    'reservation-list-page': '1',
    'user_id': '94299',
    'event_member_token_reserve_court': 'ee4a79e3bece4a506eda309bcf184f75',
    'current_guest_count': '0',
    'component': '42',
    'club': '-1',
    'host': '94299',
    'ball_machine': '0',
    'date': '09/16/2024',
    'interval': '60',
    'timeFrom': '6',
    'timeTo': '0',
    'time-reserve': '1726492500',
    'location-reserve': '9',
    'surface-reserve': '0',
    'courtsnotavailable': '',
    'join-waitlist-case': '1',
}

# response = requests.post(
#     'https://ctm.clubautomation.com/event/reserve-court-new-do',
#     params=params,
#     cookies=cookies,
#     headers=headers,
#     data=data,
# )

# print(response.text)

# confirm request

def reserve_time(local_time):
    cookies = {
        'PHPSESSID': '8kjurbhmglt992j5liejvf5k5k',
        'isLoggedIn': '1',
        '__cf_bm': 'u443C7xxLf0GVQ82Jc_z_qaFExB0f9sjM.Bkww1j9ww-1726375866-1.0.1.1-6vyT3CRjEwtwEP6etwSyQ6SSXdM7chVB0_YdX66En5NsNWoRnYNrdq.ofRc4I8Gyu3gGyY6staTUPUcA0TH.1A',
        'SessionExpirationTime': '1726405425',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=8kjurbhmglt992j5liejvf5k5k; isLoggedIn=1; __cf_bm=u443C7xxLf0GVQ82Jc_z_qaFExB0f9sjM.Bkww1j9ww-1726375866-1.0.1.1-6vyT3CRjEwtwEP6etwSyQ6SSXdM7chVB0_YdX66En5NsNWoRnYNrdq.ofRc4I8Gyu3gGyY6staTUPUcA0TH.1A; SessionExpirationTime=1726405425',
        'origin': 'https://ctm.clubautomation.com',
        'priority': 'u=1, i',
        'referer': 'https://ctm.clubautomation.com/event/reserve-court-new',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'ajax': 'true',
    }

    data = {
        'reservation-list-page': '1',
        'user_id': '94299',
        'event_member_token_reserve_court': 'ee4a79e3bece4a506eda309bcf184f75',
        'current_guest_count': '0',
        'component': '42',
        'club': '-1',
        'host': '94299',
        'ball_machine': '0',
        'date': '09/19/2024',
        'interval': '60',
        'timeFrom': '6',
        'timeTo': '0',
        'time-reserve': '1726751700',
        'location-reserve': '9',
        'surface-reserve': '0',
        'courtsnotavailable': '',
        'join-waitlist-case': '1',
        'is_confirmed': '1',
    }

    response = requests.post(
        'https://ctm.clubautomation.com/event/reserve-court-new-do',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )

    print(response.text)