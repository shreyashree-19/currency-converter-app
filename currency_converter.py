import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
from datetime import datetime
import locale
import json
import os


class CurrencyConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        # Load currency data
        self.currency_rates = CurrencyRates()
        # Use 'USD' as base to get available currency codes
        self.currency_codes = sorted(self.currency_rates.get_rates('USD').keys())
        self.currency_symbols = CurrencyCodes().get_symbol('USD')


        # GUI Components
        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=5, pady=5)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        self.from_currency_label = tk.Label(master, text="From Currency:")
        self.from_currency_label.grid(row=1, column=0, padx=5, pady=5)

        self.from_currency_combobox = ttk.Combobox(master, values=self.currency_codes)
        self.from_currency_combobox.grid(row=1, column=1, padx=5, pady=5)

        self.to_currency_label = tk.Label(master, text="To Currency:")
        self.to_currency_label.grid(row=2, column=0, padx=5, pady=5)

        self.to_currency_combobox = ttk.Combobox(master, values=self.currency_codes)
        self.to_currency_combobox.grid(row=2, column=1, padx=5, pady=5)

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.show_history_button = tk.Button(master, text="Show History", command=self.show_history)
        self.show_history_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.graph_button = tk.Button(master, text="Show Graph", command=self.show_graph)
        self.graph_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Set locale for currency formatting
        try:
            locale.setlocale(locale.LC_ALL, '')
        except locale.Error:
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

        # Load conversion history
        self.load_history()

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combobox.get()
            to_currency = self.to_currency_combobox.get()

            result = self.currency_rates.convert(from_currency, to_currency, amount)
            result_formatted = locale.currency(result, grouping=True)

            # Add to conversion history
            self.add_to_history(amount, from_currency, to_currency, result)

            messagebox.showinfo("Conversion Result", f"Converted Amount: {result_formatted}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
        except RatesNotAvailableError:
            messagebox.showerror("Error", "Exchange rate data is not available.")

    def show_history(self):
        if os.path.exists("conversion_history.json"):
            with open("conversion_history.json", "r") as f:
                history = json.load(f)
                history_text = "\n".join(
                    [f"{record['amount']} {record['from']} -> {record['to']}: {record['result']}" for record in history]
                )
                messagebox.showinfo("Conversion History", history_text)
        else:
            messagebox.showinfo("Conversion History", "No conversion history available.")

    def show_graph(self):
        if os.path.exists("conversion_history.json"):
            with open("conversion_history.json", "r") as f:
                history = json.load(f)
                if history:
                    dates = [datetime.strptime(record['timestamp'], "%Y-%m-%d %H:%M:%S") for record in history]
                    results = [record['result'] for record in history]

                    plt.plot(dates, results, marker='o')
                    plt.xlabel("Date")
                    plt.ylabel("Converted Amount")
                    plt.title("Conversion History")
                    plt.grid(True)
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()
                else:
                    messagebox.showinfo("Conversion History", "No data to plot.")
        else:
            messagebox.showinfo("Conversion History", "No conversion history available.")

    def add_to_history(self, amount, from_currency, to_currency, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            'timestamp': timestamp,
            'amount': amount,
            'from': from_currency,
            'to': to_currency,
            'result': result
        }

        if os.path.exists("conversion_history.json"):
            with open("conversion_history.json", "r") as f:
                history = json.load(f)
                history.append(record)

            with open("conversion_history.json", "w") as f:
                json.dump(history, f, indent=4)
        else:
            with open("conversion_history.json", "w") as f:
                json.dump([record], f, indent=4)

    def load_history(self):
        if not os.path.exists("conversion_history.json"):
            with open("conversion_history.json", "w") as f:
                json.dump([], f)


def main():
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
