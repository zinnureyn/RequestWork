import tkinter as tk

import requests

import ConstantFile as cf

API_KEY = cf.MY_API_KEY#buraya kendi api keyinizi yazınız

window = tk.Tk()
window.title("Hava Durumu")
label = tk.Label(window, text="")
label.pack()
label2 = tk.Label(window, text="")
label2.pack()
label3 = tk.Label(window, text="")
label3.pack()


def get_weather(user_input):
    weather_request = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={user_input}&aqi=no"
    weather_result = requests.get(weather_request)
    weather_result = weather_result.json()
    return weather_result



entry = tk.Entry(window)
entry.pack()


def girdi_al():
    user_input = entry.get()
    get_weather(user_input)
    label.config(text="sıcaklık" + str(get_weather(user_input)["current"]["temp_c"]) + "°C")




window.geometry("400x300")


button = tk.Button(window, text="Şehir Adı Giriniz", command=girdi_al)
button.pack()


window.mainloop()
