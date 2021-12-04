from django.shortcuts import render
import urllib.request,json

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        API=urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=f6d1137aa492f15ecfebda9cf0c0e787')
        jsondata=json.load(API)
        data={
            "countrycode":str(jsondata['sys']['country']),
            "coordinate":str(jsondata['coord']['lon'])+","+
            str(jsondata['coord']['lat']),
            "temp":str(jsondata['main']['temp']),
            "pressure":str(jsondata['main']['pressure']),
            "humidity":str(jsondata['main']['humidity']),
            }  
          
    else:
        city=''
        data={}

    return render(request,'index.html',{'city':city,'data':data} )