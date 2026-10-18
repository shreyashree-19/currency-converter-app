# 💱 Currency Converter App

A robust Python desktop application built with **Tkinter** that enables real‑time currency conversion using the `forex-python` library. Designed with a clean and intuitive interface, the app not only performs conversions but also maintains a detailed history and provides graphical insights into past transactions.  

This project demonstrates practical integration of **GUI development**, **API usage**, **data persistence**, and **data visualization** — making it a valuable learning resource and a professional‑grade utility.

---

## ✨ Key Features
- **Real‑time Forex Rates**: Fetches up‑to‑date exchange rates using `forex-python`.  
- **User‑Friendly Interface**: Built with Tkinter for simplicity and accessibility.  
- **Conversion History**: Stores all conversions in JSON format for easy retrieval.  
- **Graphical Insights**: Visualizes conversion trends with Matplotlib.  
- **Error Handling**: Gracefully manages invalid inputs and unavailable rates.  
- **Locale‑Aware Formatting**: Displays results in proper currency format.  

---

## 📂 Project Structure
```
CurrencyConverterApp/
│
├── currency_converter.py      # Main application script
├── conversion_history.json    # Auto-generated conversion history
├── README.md                  # Documentation
├── LICENSE                    # MIT License
└── .gitignore                 # Ignore unnecessary files
```

---

## ⚙️ Requirements
- Python 3.x  
- Dependencies:
  - `forex-python`  
  - `matplotlib`  
  - `tkinter` (built‑in)  
  - `locale`, `json`, `os` (built‑in)  

Install dependencies:
```bash
pip install forex-python matplotlib
```

---

## ▶️ Usage Guide
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/currency-converter-app.git
   ```
2. **Navigate to the project folder**:
   ```bash
   cd currency-converter-app
   ```
3. **Run the application**:
   ```bash
   python currency_converter.py
   ```

---

## 📊 Workflow
1. Enter the amount to convert.  
2. Select the source currency.  
3. Select the target currency.  
4. Click **Convert** to see the result.  
5. View **History** to check past conversions.  
6. Click **Show Graph** to visualize conversion trends.  

---

## 📸 Screenshots (Optional)
_Add screenshots of the GUI and graph here once available._  

---

## 📜 License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute with attribution.

---

## 🤝 Contribution Guidelines
Contributions are welcome!  
- Fork the repository.  
- Create a feature branch (`git checkout -b feature-name`).  
- Commit changes (`git commit -m "Add feature XYZ"`).  
- Push to your branch (`git push origin feature-name`).  
- Open a Pull Request with clear details.  

---

## 📈 Future Enhancements
- Add support for **offline mode** with cached rates.  
- Implement **multi‑currency batch conversion**.  
- Export conversion history to **CSV/Excel**.  
- Dark mode UI theme for better accessibility.  

---

