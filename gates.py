import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import datetime
import time
import sys
import schedule
import csv
import cookies

gate_test = "Hello World"

# with open('dates.csv', mode='r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     next(csv_reader)
#     for row in csv_reader:
#         print(row)
#         datetime_str = f"{row[0]} {row[1]}"
#         datetime_obj = datetime.datetime.strptime(datetime_str, "%m/%d/%Y %H:%M")
#         epoch_time = int(time.mktime(datetime_obj.timetuple()))
#         print(epoch_time)

# Time is stored in seconds since epoch / 1000
def get_local_time(seconds):
    local_time = datetime.datetime.fromtimestamp(seconds)
    return local_time

def get_unix_seconds(local_time):
    unix_seconds = int(time.mktime(local_time.timetuple()))
    return unix_seconds

def format_date(local_time):
    return local_time.strftime("%m/%d/%Y")


expire_time = 1726657327

def check_expiration(cookies, expire_time):
    current_time = int(time.time())

    if(current_time > expire_time):
        print("Session expired")
        print("Please manually start a new session")
        sys.exit()
    # Check if session expires in 2 hours
    elif(current_time > expire_time + 7200):
        print("Session expires in 2 hours")
        print("Refreshing session")
        refresh_session(cookies)
        sys.exit()

def server():
    schedule.every().hour.do(check_expiration, expire_time)
    schedule.run_pending()
    time.sleep(1)

def main():

    #reserve_time(get_local_time(1726670700), cookies)
    # reserve_time(date='09/23/2024', cookies=default_cookies, time='1727106300')
    # refresh_session(cookies)
    reserve_dates()

def refresh_session(cookies):
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


def reserve_time(local_time=None, cookies=None, date=None, time=None, length=60):
    if(cookies is None):
        cookies = {
            'PHPSESSID': 'vsevr3kaackqo5uam139nda8i0',
            'isLoggedIn': '1',
            '__cf_bm': '_rE0jDmjVxqOoyLcj6P8BhvSssjiQEpBGHqLR9zfxr8-1726628430-1.0.1.1-HJPwlCCxLsDSJZ7nGrt7GsF874LsMIL_z4BuyyNe_TXT6OwT78lL3TXWZfpmKzUNZcCR4kUvOvbKb_kTKZxVYw',
            'SessionExpirationTime': '1726657327',
        }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=76gukkufq424qrp1r4fhttonoe; isLoggedIn=1; __cf_bm=yfADEpTqAEd3SjLoLVvh85KF8IdOIUiN2uTFKqjW8ho-1726719914-1.0.1.1-6Chh6GckHWl5ckjocspVjkS_WaSOvlZ09p5VtucMda.0.zbsb69rF6WcD6t_Em0gVVOjqQxkoXAincrZPG2VYw; SessionExpirationTime=1726748733',
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

    if date is None:
        date = format_date(local_time)

    if(time is None):
        time = str(get_unix_seconds(local_time))

    data = {
        'reservation-list-page': '1',
        'user_id': '96192',
        'event_member_token_reserve_court': 'b40bf887821973f33641859653aef6d9',
        'current_guest_count': '0',
        'component': '42',
        'club': '-1',
        'host': '96192',
        'ball_machine': '0',
        'date': date,
        'interval': str(length),
        'timeFrom': '9',
        'timeTo': '0',
        'time-reserve': time,
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

    # print(response.text)
    return response

def reserve_dates():
    with open('dates.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            print(row)
            datetime_str = f"{row[0]} {row[1]}"
            datetime_obj = datetime.datetime.strptime(datetime_str, "%m/%d/%Y %H:%M")
            epoch_time = int(time.mktime(datetime_obj.timetuple()))
            print("Attempting to reserve: " + datetime_str)
            response = reserve_time(date=row[0], cookies=cookies.default_cookies, time=str(epoch_time), length=row[2])
            if "Reservation Completed" in response.text:
                print("Successfully reserved: " + datetime_str)
                return
        print("No dates available")
        # Maybe print available dates
if __name__ == "__main__":
    main()