#encoding ucf-8
import requests
url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
params = {'theRegionCode':3113}

#get请求
#response = requests.get(url=url,params=params)

#post请求
#response = requests.post(url=url,data=params,headers={'Content-type':'application/x-www-form-urlencoded'})

#SOAP请求
datas = '''
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <getSupportCityString xmlns="http://WebXml.com.cn/">
      <theRegionCode>3113</theRegionCode>
    </getSupportCityString>
  </soap12:Body>
</soap12:Envelope>
'''
soapUrl='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx'
#response = requests.post(url=soapUrl,data=datas,headers={'Content-type':'text/xml'})



#json参数
jsonUrl='http://ws.webxml.com.cn/event/weather/getWeather/'
dataJson='{"theCityCode":1}'
response = requests.post(url=jsonUrl,json=dataJson,headers={'Content-type':'application/json'})


print(response.text)
#print(type(response.text))