import requests
import tkinter as tk
from tkinter import messagebox, simpledialog

baseurl = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'YOUR_API_KEY',
}

count = 0
stop_flag = False

def notify(message):
    messagebox.showinfo("Crypto Price Alert", message)

def recurring_notify(identifier, wait_time, max_repeats):
    global count, stop_flag
    if stop_flag or count >= max_repeats:
        output_label.config(text="Notifications stopped or completed.", fg="red")
        return

    response = requests.get(baseurl, headers=headers)
    data = response.json()

    for coin in data['data']:
        if coin['symbol'] == identifier:
            price = round(coin['quote']['USD']['price'], 2)
            timestamp = coin['quote']['USD']['last_updated']
            message = f"As of {timestamp}, the price of {identifier} is ${price}"
            notify(message)
            output_label.config(text=message, fg="green")
            break

    count += 1
    root.after(wait_time * 1000, recurring_notify, identifier, wait_time, max_repeats)

def start_alerts():
    global count, stop_flag
    count = 0
    stop_flag = False

    identifier = simpledialog.askstring("Input", "Enter Coin Symbol (e.g., BTC, ETH):")
    identifier = identifier.strip().upper()

    max_repeats = int(simpledialog.askstring("Input", "How many alerts?"))
    wait_time = int(simpledialog.askstring("Input", "Seconds between alerts?"))

    recurring_notify(identifier, wait_time, max_repeats)

def stop_alerts():
    global stop_flag
    stop_flag = True
    output_label.config(text="Notifications stopped by user.", fg="red")

root = tk.Tk()
root.title("Crypto Price Tracker")
root.geometry("400x250")
root.resizable(False, False)

tk.Button(root, text="Start Alerts", command=start_alerts, font=("Arial", 12), bg="#007acc", fg="white").pack(pady=20)
tk.Button(root, text="Stop Notifications", command=stop_alerts, font=("Arial", 12), bg="#cc0000", fg="white").pack()

output_label = tk.Label(root, text="", font=("Arial", 11))
output_label.pack(pady=20)

root.mainloop()
