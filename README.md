# 🦠 COVID-19 Interactive Dashboard

An interactive data visualization dashboard built with **Python Dash** and **Plotly**, featuring real-time COVID-19 pandemic statistics for India alongside global socio-economic indicators from the Gapminder dataset.

---

## 📸 Screenshots

### COVID-19 India Dashboard
![COVID-19 Dashboard](https://img.shields.io/badge/Dashboard-COVID--19-red?style=for-the-badge&logo=plotly)

> Displays **Total Cases**, **Active (Hospitalized)**, **Recovered**, and **Deceased** counts with interactive state-wise bar charts.

### Gapminder Explorer
![Gapminder Dashboard](https://img.shields.io/badge/Dashboard-Gapminder-blue?style=for-the-badge&logo=plotly)

> Scatter plot of **Population vs GDP per Capita** and box plot distribution for countries worldwide.

---

## ✨ Features

- 📊 **Real-Time Summary Cards** — Total, Active, Recovered, and Death case counts
- 🗺️ **State-Wise Analysis** — Interactive bar chart showing COVID-19 cases by Indian states
- 🔽 **Dropdown Filter** — Filter cases by status: All, Hospitalized, Recovered, or Deceased
- 📈 **Gapminder Visualization** — Scatter plot (Population vs GDP) and Box plot for global economic data
- 🎨 **Responsive UI** — Styled with Bootstrap for a clean, mobile-friendly layout
- ⚡ **Interactive Callbacks** — Dynamic chart updates using Dash callbacks

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| [Python](https://www.python.org/) | Core programming language |
| [Dash](https://dash.plotly.com/) | Web application framework |
| [Plotly](https://plotly.com/python/) | Interactive data visualization |
| [Pandas](https://pandas.pydata.org/) | Data manipulation & analysis |
| [NumPy](https://numpy.org/) | Numerical computing |
| [Bootstrap 4](https://getbootstrap.com/) | CSS framework for styling |

---

## 📁 Project Structure

```
Dash/
├── Covid_19/
│   ├── app.py                  # Main COVID-19 dashboard application
│   ├── IndividualDetails.csv   # Individual patient-level COVID-19 data
│   ├── covid_19_india.csv      # State-wise COVID-19 data for India
│   ├── AgeGroupDetails.csv     # Age group breakdown of COVID-19 cases
│   └── assets/
│       └── styles.css          # Custom CSS styles (dark theme)
├── dashboard.py                # Gapminder data explorer dashboard
├── gapminder.csv               # Global socio-economic dataset (1952–2007)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have **Python 3.7+** installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/Gyana07-prog/Corona-virus-Covid-19-Dashboard-on-Dash.git
cd Corona-virus-Covid-19-Dashboard-on-Dash
```

### 2. Install Dependencies

```bash
pip install dash plotly pandas numpy
```

### 3. Run the COVID-19 Dashboard

```bash
python Covid_19/app.py
```

Open your browser and navigate to: **http://127.0.0.1:8050/**

### 4. Run the Gapminder Dashboard

```bash
python dashboard.py
```

Open your browser and navigate to: **http://127.0.0.1:8050/**

---

## 📊 Datasets

### COVID-19 India Data
| File | Description |
|---|---|
| `IndividualDetails.csv` | Patient-level data with status, state, age, and gender |
| `covid_19_india.csv` | State-wise aggregated COVID-19 statistics |
| `AgeGroupDetails.csv` | Case distribution across 10 age groups |

### Gapminder Data
| File | Description |
|---|---|
| `gapminder.csv` | Country-level data: life expectancy, population, GDP per capita (1952–2007) |

---

## 📌 Dashboard Details

### COVID-19 Dashboard (`Covid_19/app.py`)
- **Summary Cards**: Four color-coded cards (Red — Total, Blue — Active, Yellow — Recovered, Green — Deaths)
- **Interactive Dropdown**: Filter the bar chart by patient status
- **State-wise Bar Chart**: Dynamically updates based on the selected filter
- **Dark Theme**: Custom dark background for better readability

### Gapminder Dashboard (`dashboard.py`)
- **Scatter Plot**: Population vs GDP per Capita for all countries
- **Box Plot**: Distribution of GDP per Capita across the dataset

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Gyana Ranjan**

- GitHub: [@Gyana07-prog](https://github.com/Gyana07-prog)

---
