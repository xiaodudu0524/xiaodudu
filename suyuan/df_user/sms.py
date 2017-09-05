import json
import requests

headers = {
    "X-LC-Id": "uMXfsfIqzEKqcginnfoKAEYF-gzGzoHsz",
    "X-LC-Key": "E6gcREswLaR9aQovpc5aph1Q",
    "Content-Type": "application/json",

}

REQUEST_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/requestSmsCode'

VERIFY_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/verifySmsCode/'


def send_message(phone):
    data = {
        "mobilePhoneNumber": phone,
    }
    r = requests.post(REQUEST_SMS_CODE_URL, data=json.dumps(data), headers=headers)
    print r.status_code
    if r.status_code == 200:

        return True
    else:
        return False


def verify(phone, code):
    target_url = VERIFY_SMS_CODE_URL + "%s?mobilePhoneNumber=%s" % (code, phone)
    r = requests.post(target_url, headers=headers)
    if r.status_code == 200:
        return True
    else:
        return False
