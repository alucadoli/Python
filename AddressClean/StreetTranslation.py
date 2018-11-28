# _*_ coding:utf-8 _*_

import requests

cookies = {
    'MUID': '3C934BF619576FF2342D40FF1D576C30',
    'SRCHD': 'AF=NOFORM',
    'SRCHUID': 'V=2&GUID=E9848B481A05401BA7953FB711BB4186&dmnchg=1',
    'SRCHUSR': 'DOB=20171204',
    'MUIDB': '3C934BF619576FF2342D40FF1D576C30',
    'ENSEARCH': 'BENVER=1',
    '_EDGE_S': 'mkt=zh-cn&SID=1E7A21FC6DE660A13CB32AB26C2661AE',
    'PPLState': '1',
    '_FP': 'hta=off',
    'ULC': 'P=5792|3:3&H=5792|3:3&T=5792|3:3',
    'SRCHHPGUSR': 'CW=1519&CH=894&DPR=1.25&UTC=480&WTS=63655038356',
    'iptac-5C838FE1DDB7-FCZ1949N005': '434f5250464353494e545c636e616c6c69404643535f4144--1521009565--1825--1520859896--ea8cf45850f057cd4aabbbe104e12e0e296618a0aa7a290ee719700fcaf064f1',
    'KievRPSAuth': 'FABiARRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACBfn5UbOJuCqIAFI3kGiob9uOj2OOHuKTlFYvY2CekX2JH/zWGy%2BfIZhTw3CKppvbQiHmOpR0GZGyIvRtbBiJ/znrbSNKwLQ731dKWPEWFJKmlpO/2IEt0MEY5TAAE8OlBALqARjBgHeGMfAfb4HM/PqwyhC9KQEOYblvyVGwRmjdMaGsiuU24dqTlqEcgY4t5IBeHJ3abXew3wbxkPIKjwovUPfZNzTrpoPmyxYvE25G4zB3WGs/s8ZwQg3uB0hGRhcpIhZ9TQJSuHF1xf2t5cIhcOkdDLkV/ZSo/dzTlEo9Fa0xl3cNNMh2V4uele5etiva8oyYzJQ2zDxJu0pRBUxzHu9hppezHC6wFyPqVaFIQ41czKTwQn0Rv/sml%2BuvY1gHEhqxZRQtlIUAIaMujkpMXnCLegM7PgZWMVrY90D',
    'KievRPSSecAuth': 'FABiARRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACKpzyaexmGpiIAHUug4S0C%2Bk2WyGs8mJZqTL%2BiYCEQgyQ83PTpqjiguQFw3%2Bti19pPmTp5Sy/KX1dmn2dH1mDQeVYThSPhbjThf8ilmpPUDg4z3%2BEPFTorOVrIle/lnPGTmb/i87HzTZwTTbBC1uKkZ0/IvdaduVeKYAIRv2G5zA9eiCvoAqqL12uUOD%2B4Zp0/YA/MFfke0CQ79O7CyHG8YjJsX4b3EnF%2Bkb/EI/9WUdQm0CFFrBv2KEA553bjx7Ww7%2BM87ZUIE2idlkHLVSQxuiU7caBEYtNpses6SBf577aQneqUsNo0IGulluzF9AKWL3C/V3AwK%2Bvn483Jea6X15%2Bi/oO8Tpad4zDOWQNGax/7eEWJKmJsZ8kBz3QaVj81OPBwlSMd0jm1wUAFEgAv5X63Urqc1oeIMwlj1MDeL7',
    'ANON': 'A=C799EF28EA43DCA3E2C83AD1FFFFFFFF&E=153d&W=1',
    'NAP': 'V=1.9&E=14e3&C=au2qdGSu8D0Hl_edg567I3NVdyeRNtJ3Bk6cM_qAuCuIntOkZft3dA&W=2',
    '_U': '1X7i4jfcD8qC5A0oPQH6kpunN9k7myOW6AKBBQOmbj9_b4q2RqW27crSZO9Q8k4ojO6wr07YNnWT3ys4fPT74z1MWZpVMTfFbwnzOVMnwrviWhi4zsTMRV6hGQejhvATH',
    'WLID': '+nhjbFxqmRQhP3rkaWBpYIDrJaLv25TBWXQ/6xKMknYVDY3+ETN/z+AV1cNbj1UZ4m14grB79h2735TijeM2JeevK1o2FYoRcue0TcOvvoo=',
    'WLS': 'C=&N=',
    'ipv6': 'hit=1527760291991&t=4',
    'MSCC': '1',
    'btstkn': '%252BcJbsG92jmIy2WG9S%252BtH6m3SoAKtg2jl3Mgk4HBwa8p5loDMTFHfHvhiUM2UVohu',
    '_SS': 'SID=1E7A21FC6DE660A13CB32AB26C2661AE&HV=1527756776&bIm=485&h5comp=0',
}

headers = {
    'Origin': 'https://www.bing.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Referer': 'https://www.bing.com/',
    'Connection': 'keep-alive',
    'DNT': '1',
}

params = (
    ('', ''),
    ('category', ''),
    ('IG', '0229DF117D9A4AD4B850189D212E2AE5'),
    ('IID', 'translator.5035.1'),
)

data = [
  ('', ''),
  # ('text', '\u676D\u5DDE\u5E02\u4E0B\u6C9912\u53F7\u5927\u8857'),
  ('text',r'上海市青浦区拓青路88号'),
  ('from', 'zh-CHS'),
  ('to', 'en'),
]

proxies = {
	"https": "http://10.3.246.5:8500"
}

response = requests.post('https://www.bing.com/ttranslate', headers=headers, params=params, cookies=cookies, proxies = proxies,data=data, verify=False)

print(response.text)