import requests


def get_temp(city):
    url = f"http://api.weather.com/{city}/temperature"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['temperature']
    else:
        return None


def is_hot(city, threshold):
    temp = get_temp(city)
    if temp is None:
        return False
    return temp > threshold


if __name__ == "__main__":
    city = "Lahore"
    threshold = 45
    print(f"Is it hot in {city}? {'Yes' if is_hot(city,
                                                  threshold) else 'No'}")
