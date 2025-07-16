import tkinter as tk
from tkinter import messagebox
import requests

# Function to update Entry appearance on hover
def on_enter(event):
    city_entry.config(highlightbackground="blue", highlightthickness=2) 

def on_leave(event):
    city_entry.config(highlightbackground="gray", highlightthickness=1) 

# Function to fetch weather data
def get_weather():
    city = city_entry.get().strip()  # Remove whitespace
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    api_key = "21b65cff8ba23a5aedf049d3473eb793"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != 200:
            messagebox.showerror("Error", f"City not found: {data['message']}")
            return

        city_name = data["name"]
   
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_desc = data["weather"][0]["description"]

        # Update result label
        result_label.config(
            text=f"Weather in {city_name}:\n"
               
                 f"Temperature: {temperature}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Condition: {weather_desc.capitalize()}"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Unable to fetch data: {e}")



root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg='#ffc55a')


title_label = tk.Label(root, text="Weather App", bg='#ffc55a', font=("Arial", 16, "bold"))
title_label.pack(pady=5)


city_label = tk.Label(root, text="Enter city name:", bg='#ffc55a', font=("Arial", 12))
city_label.pack(pady=5)


city_entry = tk.Entry(root, font=("Arial", 12), width=25, bd=1, highlightbackground="gray", highlightthickness=1)
city_entry.pack(pady=5)

city_entry.bind("<Enter>", on_enter)
city_entry.bind("<Leave>", on_leave)


fetch_button = tk.Button(root, text="Get Weather", bg='red', fg='white', font=("Arial", 12, 'bold'), command=get_weather)
fetch_button.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), justify="left", fg="blue")
result_label.pack(pady=10)


root.mainloop()
