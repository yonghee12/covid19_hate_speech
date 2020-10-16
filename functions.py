from config import *


def get_safe(url, headers=None, cookies=None, error=0, rtype='text'):
    try:
        response = requests.get(url, headers=headers, cookies=cookies)
    except Exception as e:
        if error > 2:
            return ''
        print(str(e), 'RELOADING REQUESTS MODULE')
        reload(requests)
        time.sleep(2)
        return get_safe(url, headers, cookies, error + 1)
    else:
        if response.status_code == 200:
            if rtype == 'text':
                return response.text
            elif rtype == 'content':
                return response.content
        return ''


def get_headers_from_str(header_str, strip=True):
    if strip:
        sss = [ss.split(': ') for ss in header_str.split('\n') if ss.strip()]
    else:
        sss = [ss.split(': ') for ss in header_str.split('\n')]
    dic = {}
    for tup in sss:
        key = tup[0].replace(":", "")
        if len(tup) == 2:
            dic[key] = tup[1]
        elif len(tup) == 1:
            dic[key] = ''
        else:
            raise Exception("Parse Error")
    return dic


def get_cookies_from_str(cookie_str):
    cookies = {}
    for cook in [cc.split("=") for cc in cookie_str.split("; ") if cc.strip()]:
        cookies.update({cook[0]: '='.join(cook[1:])})
    return cookies
