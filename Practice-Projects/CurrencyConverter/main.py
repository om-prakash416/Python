from tkinter import *
from tkinter import messagebox

def fetch_exchange_rates():
    try:
        api_url = ""
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        
        if data.get("result") == "success":
            return data[rates]
        else:
            messagebox.showerror("Error","Failed to fetch_exchange_rates")
            
            return None
    
    except Exception as e:
        messagebox.showerror("Error",f"Error fetching exchange rates: {e}")
        return None
    
def convert_currency():
    try:
        amount = float(amount_entry.get())
        