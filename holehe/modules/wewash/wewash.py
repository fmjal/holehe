import random
from holehe.core import *
from holehe.localuseragent import *

async def wewash(email, client, out):
    name = "we-wash"
    domain = "backend.we-wash.com"
    method = "reset-password"
    frequent_rate_limit = False

    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json',
        'WW-App-Version': '2.53.0',
        'WW-Client': 'USERAPP',
        'Origin': 'https://app.we-wash.com',
        'Connection': 'keep-alive',
        'Referer': 'https://app.we-wash.com/',
        'TE': 'trailers'
    }

    data = {
        "email": email
    }

    try:
        response = await client.post('https://backend.we-wash.com/v3/reset-password', headers=headers, json=data)
        if response.status_code == 200:
            out.append({
                "name": name,
                "domain": domain,
                "method": method,
                "frequent_rate_limit": frequent_rate_limit,
                "rateLimit": False,
                "exists": True,
                "emailrecovery": None,
                "phoneNumber": None,
                "others": None
            })
        elif response.status_code == 404:
            out.append({
                "name": name,
                "domain": domain,
                "method": method,
                "frequent_rate_limit": frequent_rate_limit,
                "rateLimit": False,
                "exists": False,
                "emailrecovery": None,
                "phoneNumber": None,
                "others": None
            })
        else:
            out.append({
                "name": name,
                "domain": domain,
                "method": method,
                "frequent_rate_limit": frequent_rate_limit,
                "rateLimit": True,
                "exists": False,
                "emailrecovery": None,
                "phoneNumber": None,
                "others": None
            })
    except Exception:
        out.append({
            "name": name,
            "domain": domain,
            "method": method,
            "frequent_rate_limit": frequent_rate_limit,
            "rateLimit": True,
            "exists": False,
            "emailrecovery": None,
            "phoneNumber": None,
            "others": None
        })

