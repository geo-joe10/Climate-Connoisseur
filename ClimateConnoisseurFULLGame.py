import requests
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# List of predefined locations
locations = [
    {"city": "Durham", "country": "USA"},
    {"city": "Paris", "country": "France"},
    {"city": "Abuja", "country": "Nigeria"},
    {"city": "Sydney", "country": "Australia"},
    {"city": "Nuuk", "country": "Greenland"},
    {"city": "Kingston", "country": "Jamaica"},
    {"city": "New Delhi", "country": "India"},
    {"city": "San Diego", "country": "USA"},
    {"city": "Lisbon", "country": "Portugal"},
    {"city": "Puerto Plata", "country": "Dominican Republic"},
    {"city": "Cancun", "country": "Mexico"},
    {"city": "Atlanta", "country": "USA"},
    {"city": "Brussels", "country": "Belgium"},
    {"city": "Monkayo", "country": "Philippines"},
    {"city": "Årø", "country": "Norway"},
    {"city": "Death Valley", "country": "USA"},
    {"city": "Genoa", "country": "Italy"},
    {"city": "Andros Town", "country": "Bahamas"},
    {"city": "Boca Raton", "country": "USA"},
    {"city": "Rio De Janeiro", "country": "Brazil"},
    {"city": "Cairo", "country": "Egypt"},
    {"city": "Addis Ababa", "country": "Ethiopia"},
    {"city": "Shanghai", "country": "China"},
    {"city": "Manchester", "country": "United Kingdom"},
    {"city": "Naples", "country": "Italy"},
    {"city": "Venice", "country": "Italy"},
    {"city": "Munich", "country": "Germany"},
    {"city": "Sofia", "country": "Bulgaria"},
    {"city": "Ankara", "country": "Turkey"},
    {"city": "Brazzaville", "country": "Congo"},
    {"city": "Pretoria", "country": "South Africa"},
    {"city": "Miami ", "country": "USA"},
    {"city": "Williamsburg", "country": "USA"},
    {"city": "Kansas City", "country": "USA"},
    {"city": "Buffalo", "country": "USA"},
    {"city": "Maine-Soroa", "country": "Niger"},
    {"city": "Chicago", "country": "USA"},
    {"city": "Seattle", "country": "USA"},
    {"city": "Las Vegas", "country": "USA"},
    {"city": "Albuquerque ", "country": "USA"},
    {"city": "Pittsburgh", "country": "USA"},
    {"city": "Akron", "country": "USA"},
    {"city": "Cullera", "country": "USA"},
    {"city": "Ayacucho", "country": "Peru"},
    {"city": "Matsushima", "country": "Japan"},
    {"city": "Edessa", "country": "Greece"},
    {"city": "Akrotiri", "country": "Greece"},
    {"city": "Accra", "country": "Ghana"},
    {"city": "Cape Town", "country": "South Africa"},
    {"city": "Jakarta", "country": "Indonesia"},
    {"city": "Mount Cook", "country": "New Zealand"},
    {"city": "Brisbane", "country": "Australia"},
    {"city": "Punta Arenas", "country": "Chile"},
    {"city": "Istanbul", "country": "Turkey"},
    {"city": "Helsinki", "country": "Finland"},
    {"city": "Mumbai", "country": "India"},
    {"city": "Kyoto", "country": "Japan"},
    {"city": "Reykjavik", "country": "Iceland"},
    {"city": "Montreal", "country": "Canada"},
    {"city": "Riyadh", "country": "Saudi Arabia"},
    {"city": "Kota Bharu", "country": "Malaysia"},
    {"city": "Yamoussoukro", "country": "Cote d'Ivoire"},
    {"city": "Alwar", "country": "India"},
    {"city": "Lille", "country": "France"},
    {"city": "Lyon", "country": "France"},
    {"city": "Rennes", "country": "France"},
    {"city": "Nice", "country": "France"},
    {"city": "Toledo", "country": "USA"},
    {"city": "Seoul", "country": "South Korea"},
    {"city": "Berlin", "country": "Germany"},
    {"city": "Moscow", "country": "Russia"},
    {"city": "Saint Petersburg", "country": "Russia"},
    {"city": "Grozny", "country": "Russia"},
    {"city": "Tolyatti", "country": "Russia"},
    {"city": "Qer Misi", "country": "Afghanistan"},
    {"city": "Luanda", "country": "Angola"},
    {"city": "London", "country": "United Kingdom"},
    {"city": "London", "country": "Canada"},
    {"city": "Madrid", "country": "Spain"},
    {"city": "Barcelona", "country": "Spain"},
    {"city": "Kyiv", "country": "Ukraine"},
    {"city": "Gothenburg", "country": "Sweden"},
    {"city": "Malmo", "country": "Sweden"},
    {"city": "Stockholm", "country": "Sweden"},
    {"city": "Tashkent", "country": "Uzbekistan"},
    {"city": "Kabul", "country": "Afghanistan"},
    {"city": "Jalalabad", "country": "Afghanistan"},
    {"city": "Herat", "country": "Afghanistan"},
    {"city": "Touho", "country": "New Caledonia"},
    {"city": "Punta Cana", "country": "Dominican Republic"},
    {"city": "La Romana", "country": "Dominican Republic"},
    {"city": "Kinshasa", "country": "Democratic Republic of Congo"},
    {"city": "Byumba", "country": "Rwanda"},
    {"city": "Kigali", "country": "Rwanda"},
    {"city": "Mombasa", "country": "Kenya"},
    {"city": "Kitale", "country": "Kenya"},
    {"city": "Hargeisa", "country": "Somalia"},
    {"city": "Norddeich", "country": "Germany"},
    {"city": "Kanungu", "country": "Uganda"},
    {"city": "Port Harcourt", "country": "Nigeria"},
    {"city": "Ibadan", "country": "Nigeria"},
    {"city": "Mendoza", "country": "Argentina"},
    {"city": "Salta", "country": "Argentina"},
    {"city": "Buenos Aires", "country": "Argentina"},
    {"city": "Apia", "country": "Samoa"},
    {"city": "Sanaa", "country": "Yemen"},
    {"city": "Lae", "country": "Papua New Guinea"},
    {"city": "Hobart", "country": "Australia"},
    {"city": "Gary", "country": "USA"},
    {"city": "Warsaw", "country": "Poland"},
    {"city": "Hefei", "country": "China"},
    {"city": "Beijing", "country": "China"},
    {"city": "Guangzhou", "country": "China"},
    {"city": "Avila", "country": "Spain"},
    {"city": "Bilbao", "country": "Spain"},
    {"city": "Murphy Town", "country": "Bahamas"},
    {"city": "Clarence Town", "country": "Bahamas"},
    {"city": "Nassau", "country": "Bahamas"},
    {"city": "Anchorage", "country": "USA"},
    {"city": "Honolulu", "country": "USA"},
    {"city": "New Orleans", "country": "USA"},
    {"city": "Leeds", "country": "United Kingdom"},
    {"city": "Liverpool", "country": "United Kingdom"},
    {"city": "Cape Coast", "country": "Ghana"},
    {"city": "Tamale", "country": "Ghana"},
    {"city": "Chapel Hill", "country": "Bahamas"},
    {"city": "Lome", "country": "Togo"},
    {"city": "Beverly Hills", "country": "USA"},
    {"city": "Denver ", "country": "USA"},
    {"city": "Hanoi", "country": "Vietnam"},
    {"city": "Islamabad", "country": "Pakistan"},
    {"city": "Tbilisi", "country": "Georgia"},
    {"city": "Phnum Penh", "country": "Cambodia"},
    {"city": "Tehran", "country": "Iran"},
    {"city": "Athens", "country": "Greece"},
    {"city": "Florina", "country": "Greece"},
    {"city": "Holetown", "country": "Barbados"},
    {"city": "Crab Hill", "country": "Barbados"},
    {"city": "Roseau", "country": "Dominica"},
    {"city": "Bridgetown", "country": "Barbados"},
    {"city": "Saint George's", "country": "Grenada"},
    {"city": "Port Of Spain", "country": "Trinidad and Tobago"},
    {"city": "Port-Au-Prince", "country": "Haiti"},
    {"city": "Paramaribo", "country": "Suriname"},
    {"city": "Georgetown", "country": "Guyana"},
    {"city": "Quito", "country": "Ecuador"},
    {"city": "Ecuandureo", "country": "Mexico"},
    {"city": "Asuncion", "country": "Paraguay"},
    {"city": "Montevideo", "country": "Uruguay"},
    {"city": "Caracas", "country": "Venezuela"},
    {"city": "Tegucigalpa", "country": "Honduras"},
    {"city": "Lima", "country": "Peru"},
    {"city": "La Paz", "country": "Bolivia"},
    {"city": "Fresno", "country": "USA"},
    {"city": "San Jose", "country": "Costa Rica"},
    {"city": "Santiago", "country": "Chile"}
]

# Function to fetch weather data
def get_weather(city):
    api_key = "8a2a9d9f356f4707877202528242912"  # Replace with your WeatherAPI key
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": api_key, "q": city}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to update the streak label
def update_streak_label():
    """Updates the streak counter label in the UI."""
    streak_label.config(text=f"Streak Counter: {streak}")

# Function to handle the game logic
def check_guess():
    """Handles the player's guess and updates the game state."""
    global streak, weather_data, current_location

    guessed_temp = temp_entry.get()
    guessed_condition = condition_entry.get().lower()

    if not guessed_temp.isdigit():
        messagebox.showerror("Invalid Input", "Please enter a valid number for the temperature.")
        return

    guessed_temp = float(guessed_temp)
    actual_temp = weather_data["current"]["temp_f"]
    actual_condition = weather_data["current"]["condition"]["text"].lower()

    temp_diff = abs(guessed_temp - actual_temp)
    correct_condition = guessed_condition in actual_condition

    if temp_diff <= 5 or correct_condition:
        streak += 1  # Increment the streak
        messagebox.showinfo("Correct!", f"Great guess! Your streak is now: {streak}\n"
                                        f"Actual Temp: {actual_temp}°F\nCondition: {actual_condition}")
        next_round()  # Move to the next round
    else:
        show_game_over()

# Function to start the next round
def next_round():
    """Prepares the next question and updates the UI."""
    global weather_data, current_location

    current_location = random.choice(locations)
    weather_data = get_weather(current_location["city"])

    if weather_data:
        location_label.config(text=f"What is the Weather in:\n{current_location['city']}, {current_location['country']}")
        temp_entry.delete(0, tk.END)
        condition_entry.delete(0, tk.END)
        update_streak_label()  # Update streak in the UI
    else:
        messagebox.showerror("Error", "Failed to fetch weather data. Skipping this location...", )
        next_round()

# Function for game over
def show_game_over():
    """Handles the game over screen."""
    global streak

    # Clear the existing game widgets
    for widget in app.winfo_children():
        widget.destroy()

    # Create Game Over Screen UI
    game_over_label = tk.Label(app, text="Game Over! Do Better next time!", font=("Arial", 14), fg="red")
    game_over_label.pack(pady=20)

    streak_label_final = tk.Label(app, text=f"Your final streak was: {streak}", font=("Arial", 18))
    streak_label_final.pack(pady=10)

    restart_button = tk.Button(app, text="Restart Game", font=("Arial", 14), command=restart_game)
    restart_button.pack(pady=10)

    quit_button = tk.Button(app, text="Quit", font=("Arial", 14), command=app.quit)
    quit_button.pack(pady=10)

    # Function to add a background image
def add_background_image():
        image = Image.open(image_path)
        image = image.resize((500, 450), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(image)
        background_label = tk.Label(app, image=bg_image)
        background_label.image = bg_image
        background_label.place(relwidth=1, relheight=1)

# Restart the game
def restart_game():
    """Restarts the game by resetting variables and UI."""
    global streak
    streak = 0  # Reset streak counter
    for widget in app.winfo_children():
        widget.destroy()
    initialize_ui()
    next_round()

# Initialize the GUI app
def initialize_ui():
    """Sets up the initial game UI."""
    global location_label, temp_entry, condition_entry, streak_label

    # Background image
    add_background_image()

    location_label = tk.Label(app, text="", font=("Arial", 16), justify="center", bg="light cyan", bd=1)
    location_label.pack(pady=20)



    temp_label = tk.Label(app, text="Guess the temperature (°F):", font=("Arial", 14, "bold"), bg="light cyan", bd=0)
    temp_label.pack()
    temp_entry = tk.Entry(app, font=("Arial", 14), bg="white", bd=1)
    temp_entry.pack()

    condition_label = tk.Label(app, text="Guess the condition", font=("Arial", 12, "bold", ), bg="light cyan", bd=1)
    condition_label.pack()
    condition_labeltwo = tk.Label(app, text="(sunny, rain, snow, thunder, clear, fog, etc...)", font=("Arial", 10), bg="light cyan", bd=0)
    condition_labeltwo.pack()
    condition_entry = tk.Entry(app, font=("Arial", 14))
    condition_entry.pack()

    submit_button = tk.Button(app, text="Submit Guess", font=("Arial", 14), command=check_guess)
    submit_button.pack(pady=20)

    streak_label = tk.Label(app, text=f"Streak Counter: {streak}", fg="red", font=("Arial", 12))
    streak_label.pack()

    def open_weatherapi():
        import webbrowser
        webbrowser.open("https://www.weatherapi.com/")

    link_label = tk.Label(app, text="Powered by WeatherAPI.com", fg="blue", cursor="hand2",
                          font=("Arial", 10, "italic"))
    link_label.pack(pady=5)
    link_label.bind("<Button-1>", lambda e: open_weatherapi())





# Path to your background image
image_path =  "ccbackground.png"  # Image file must be in the same directory as the script

# Start the app
app = tk.Tk()
app.title("Climate Connoisseur")
app.geometry("500x450")
streak = 0  # Initialize streak counter

initialize_ui()
next_round()

app.mainloop()
