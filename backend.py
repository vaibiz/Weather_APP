import requests
API_KEY="dedc5e1e6d87f6c0d47d8c7184917c8f"

def get_data(place="Vilnius", forecast_days=None):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_val=8*forecast_days
    filtered_data=filtered_data[:nr_val]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Vilnius", forecast_days=3))

