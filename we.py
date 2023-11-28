import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")

        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(root)
        self.city_entry.pack(pady=10)

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

    def get_weather(self):
        api_key = "691ef005672ab7177e546d4e887e4cb1"
        # Replace with your OpenWeatherMap API key
        city = self.city_entry.get()
        if not city:
            messagebox.showwarning("Warning", "Please enter a city.")
            return

        try:
            
            url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={691ef005672ab7177e546d4e887e4cb1}"
            response = requests.get(url)
            data = response.json()

            # Parse the response and display the weather information
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            message = f"Weather in {city}: {temperature}°C, {description.capitalize()}"
            messagebox.showinfo("Weather Forecast", message)
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching weather data: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
