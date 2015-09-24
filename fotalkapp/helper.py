import requests

def getIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def getCountryCode(request):
	ip = getIP(request)
	if ip == "127.0.0.1":
		return "US"

	url = 'https://freegeoip.net/json/' + ip

	r = requests.get(url)
	res = r.json()

	if 'country_code' in res:
		return res['country_code']
	else:
		return 'XX'