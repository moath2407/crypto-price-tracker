import requests
import json
import tkinter as tk
from tkinter import messagebox

baseurl = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR_API_KEY',
}

stop_flag = False 
count = 0 

def notify(message):
    messagebox.showinfo("Crypto Price Alert", message)

def recurring_notify(message, wait_time_ms, max_count):
    global stop_flag, count
    if stop_flag or count >= max_count:
        output_label.config(text="Notifications stopped or completed.", fg="red")
        return
    notify(message)
    count += 1
    root.after(wait_time_ms, recurring_notify, message, wait_time_ms, max_count)

def check_price_of_coin(identifier, use_timer, wait_time, max_repeats):
    global stop_flag, count
    stop_flag = False
    count = 0

    response = requests.get(baseurl, headers=headers)
    print("Status Code:", response.status_code)

    data = response.json()
    found = False

    for coin in data['data']:
        if coin['symbol'] == identifier:
            price = round(coin['quote']['USD']['price'], 2)
            timestamp = coin['quote']['USD']['last_updated']

            if use_timer:
                message = f"As of {timestamp}, the price of {identifier} is ${price}"
                recurring_notify(message, wait_time * 1000, max_repeats)
                output_label.config(text="Notifications started! Click Stop to end.", fg="blue")
            else:
                output_label.config(
                    text=f"As of {timestamp}, {identifier} costs ${price}",
                    fg="green"
                )
            found = True
            break

    if not found:
        output_label.config(text="Coin not found.", fg="red")

def on_submit():
    symbol = entry.get().strip().upper()
    use_timer = notify_var.get()
    try:
        wait_time = int(time_entry.get()) if use_timer else 0
        max_repeats = int(repeats_entry.get()) if use_timer else 0
    except ValueError:
        messagebox.showwarning("Input Error", "Wait time and repeats must be numbers.")
        return

    if not symbol:
        messagebox.showwarning("Input Error", "Please enter a coin symbol.")
        return

    check_price_of_coin(symbol, use_timer, wait_time, max_repeats)

def stop_notifications():
    global stop_flag
    stop_flag = True
    output_label.config(text="Notifications stopped.", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Crypto Price Tracker")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Enter Coin Symbol (e.g., BTC, ETH):", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12))
entry.pack()

notify_var = tk.BooleanVar()
tk.Checkbutton(root, text="Enable recurring alert", variable=notify_var, font=("Arial", 10)).pack(pady=5)

tk.Label(root, text="Wait time in seconds (for alerts):", font=("Arial", 10)).pack()
time_entry = tk.Entry(root, font=("Arial", 10))
time_entry.insert(0, "10")
time_entry.pack()

tk.Label(root, text="Number of alerts to show:", font=("Arial", 10)).pack()
repeats_entry = tk.Entry(root, font=("Arial", 10))
repeats_entry.insert(0, "3")
repeats_entry.pack()

tk.Button(root, text="Check Price", command=on_submit, font=("Arial", 12), bg="#007acc", fg="white").pack(pady=10)

tk.Button(root, text="Stop Notifications", command=stop_notifications, font=("Arial", 12), bg="#cc0000", fg="white").pack(pady=5)

output_label = tk.Label(root, text="", font=("Arial", 11))
output_label.pack(pady=10)

root.mainloop()
