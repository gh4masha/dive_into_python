import requests
import datetime
from operator import itemgetter


def calc_age(uid):
    ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
    # – Для; получения; id; пользователя; по; username; или; user_id:
    #
    # https: // api.vk.com / method / users.get?v = 5.71 & access_token = [token] & user_ids = [user_id]

    # – Для; получения; списка; друзей:

    # https: // api.vk.com / method / friends.get?v = 5.71 & access_token = [token] & user_id = [user_id] & fields = bdate

    result = requests.get(
        'https://api.vk.com/method/users.get?v=5.71&access_token=' + ACCESS_TOKEN + '&user_ids=' + uid)
    print('result: ', result)

    print('text: ', result.text)
    print('json: ', result.json())
    user_json = result.json()['response']
    user_id = user_json[0]['id']

    friends_result = requests.get(
        'https://api.vk.com/method/friends.get?v=5.71&access_token=' + ACCESS_TOKEN + '&user_id=' + str(
            user_id) + '&fields=bdate')
    print('json: ', friends_result.json()['response'])
    stat = dict()
    current_year = datetime.date.today().year
    for person in friends_result.json()['response']['items']:
        try:
            bdate = person['bdate']

            d = bdate.split('.')
            if len(d) == 3:
                d1 = datetime.date(int(d[2]), int(d[1]), int(d[0]))
                f_age = stat.get(current_year - d1.year)
                if f_age == None:
                    stat[current_year - d1.year] = 1
                else:
                    stat.update({current_year - d1.year: f_age + 1})
        except:
            pass
    s = sorted(stat.items(), key=lambda item: item[0])
    return sorted(s, key=itemgetter(1), reverse=True)


if __name__ == '__main__':
    res = calc_age('6492')
    print(res)
