import os

import requests

session = requests.Session()
session.headers['X-Apikey'] = os.getenv('VIRUSTOTAL_API_KEY')


def subdomains(domain):
    resp = session.get(f'https://www.virustotal.com/api/v3/domains/{domain}/subdomains?limit=1000')
    if not resp.ok:
        raise Exception(resp.status_code, resp.text)
    return [x['id'] for x in resp.json()['data'] if 'attributes' in x and any(
        r['type'][0] == 'A' for r in x['attributes']['last_dns_records'])]


def sub(domain):
    return '\n'.join(f'0.0.0.0 {x}' for x in subdomains(domain))


hosts = f'''127.0.0.1       localhost
::1             ip6-localhost

# 扩展 APP 广告拦截规则，对某些影视/动漫 APP 有加速奇效

{sub('sigmob.cn')}

{sub('ugdtimg.com')}

0.0.0.0 open.e.kuaishou.com

0.0.0.0 open.e.kuaishou.cn

{sub('adkwai.com')}

{sub('adukwai.com')}

{sub('e.qq.com')}

{sub('gdt.qq.com')}

0.0.0.0 gray.i.gdt.qq.com
0.0.0.0 q.i.gdt.qq.com

0.0.0.0 gray.v.gdt.qq.com

{sub('pangolin-sdk-toutiao.com')}

{sub('pangolin-sdk-toutiao-b.com')}

0.0.0.0 api-access.pangolin-sdk-toutiao1.com

{sub('pglstatp-toutiao.com')}

{sub('ctobsnssdk.com')}

0.0.0.0 api.hzsanjiaomao.com

0.0.0.0 api.juliangcili.com

{sub('anythinktech.com')}
'''

with open('hosts', 'w') as f:
    f.write(hosts)
