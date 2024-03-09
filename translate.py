import requests

url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"

payload = {
	"from": "en",
	"to": "hu",
	"q": "Hello ! Rapid Translate Multi Traduction"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "7b4d07df1cmsh77019569982fc6ap13e9acjsn8d76474b4a78",
	"X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())