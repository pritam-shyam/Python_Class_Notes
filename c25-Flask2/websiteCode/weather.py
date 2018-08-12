import requests


def get_temp(city='Ames'):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Ames&APPID=06e81d1e5ef8943f21e81cc0d314d658')
    wdata=r.json()
    return float(wdata['main']['temp']) * 9/5 - 459.67
