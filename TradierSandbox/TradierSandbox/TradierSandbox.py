
import urllib3

# Request: Market Quotes (https://sandbox.tradier.com/v1/markets/quotes?symbols=spy)

apiurl = 'https://sandbox.tradier.com/v1/markets/quotes'

http = urllib3.PoolManager()
headers = {"Accept":"application/json",
           "Authorization":"Bearer LvQqFbZtPkqtBeeEIzcWHp8LqEtK"}

r = http.request('GET', 'https://sandbox.tradier.com/v1/markets/quotes?symbols=intc', headers)

#connection = httplib.HTTPSConnection('sandbox.tradier.com', 443, timeout = 30)
# Headers



# Send synchronously

connection.request('GET', '/v1/markets/quotes?symbols=spy', None, headers)
try:
  response = connection.getresponse()
  content = response.read()
  # Success
  print('Response status ' + str(response.status))
except httplib.HTTPException as e:
  # Exception
  print('Exception during request')