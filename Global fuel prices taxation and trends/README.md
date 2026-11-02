# Global Fuel Analytics: Prices & Taxation Trends 🌍⛽

> **Data Analytics Capstone Project with Tableau & Python Flask**  
> **Project Title:** *Global Fuel Prices and Taxation Trends: A Comprehensive Analysis*  
> **Author:** Mahima  
> **Status:** Local Development Ready / Configurable Tableau Embeds  

---

## 📌 Project Overview

**Global Fuel Analytics** is a modern, responsive web application built with **Python Flask** that seamlessly embeds an interactive **Tableau Public Dashboard** and **Tableau Story**.

The project investigates the global economics of retail fuel pricing, examining how international crude oil benchmarks (Brent Crude USD) interact with national fiscal taxation policies, sovereign consumer subsidies, geographic regions, and World Bank income levels.

---

## 🚀 Key Features

- **Professional Hero & Summary Cards:** High-impact landing page highlighting core analytical areas for Petrol, Diesel, LPG, and Taxation policies without fabricated figures.
- **Tableau Public Dashboard Integration:** Responsive embedded dashboard with fullscreen support, reload controls, and filter/tooltip capabilities.
- **Tableau Story Integration:** Guided sequential story points tracing the transmission of crude prices to pump prices and government taxation divergence.
- **Transparent Methodology & Schema:** Complete breakdown of the 10 dataset fields, data cleansing techniques, and analytical limitations.
- **Responsive Modern UI:** Styled using a navy blue, teal, white, and amber palette with Bootstrap 5 and custom CSS.
- **Robust Error Handling:** Built-in custom 404 and 500 error pages.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend** | Python 3, Flask, Jinja2 Templates |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+), Bootstrap 5, Bootstrap Icons |
| **Visualization** | Tableau Public (Embedded Dashboards & Stories) |
| **WSGI Server** | Gunicorn (for production deployment) |
| **Version Control** | Git & GitHub |

---

## 📁 Project Directory Structure

```text
global-fuel-analytics/
│
├── app.py                  # Main Flask application with routes and Tableau config
├── requirements.txt        # Python package dependencies
├── .gitignore              # Files and directories ignored by Git
├── README.md               # Project documentation and guide
│
├── templates/              # Jinja2 HTML templates
│   ├── base.html           # Master layout with navbar and footer
│   ├── index.html          # Home landing page with hero and commodity cards
│   ├── dashboard.html      # Interactive Tableau Public Dashboard page
│   ├── story.html          # Guided Tableau Story narrative page
│   ├── about.html          # Methodology, dataset fields, tools, and limitations
│   ├── contact.html        # Contact and feedback inquiry form
│   ├── 404.html            # Custom Page Not Found error page
│   └── 500.html            # Custom Server Error page
│
└── static/                 # Static web assets
    ├── css/
    │   └── style.css       # Custom styling (Navy, Teal, Amber theme)
    ├── js/
    │   └── main.js         # Client-side scripts (fullscreen, reload, clipboard)
    └── images/             # Visual assets and project screenshots
```

---

## 📊 Dataset Schema (10 Core Fields)

The project visualizes and models data comprising the following 10 fields:

| Field Name | Type | Description |
| :--- | :--- | :--- |
| **Country** | Dimension | Sovereign nation analyzed |
| **Date** | Date | Observation timestamp for historical tracking |
| **Income Level** | Dimension | World Bank classification (*High, Upper Middle, Lower Middle, Low*) |
| **Region** | Dimension | Geographic group (*Europe, Americas, Asia-Pacific, Africa, etc.*) |
| **Subsidy Level** | Dimension | Level of government retail subsidy support |
| **Brent Crude USD** | Measure ($) | International benchmark crude oil price per barrel |
| **Diesel USD Liter** | Measure ($) | Retail automotive diesel price per liter in USD |
| **LPG USD Liter** | Measure ($) | Retail Liquefied Petroleum Gas price per liter in USD |
| **Petrol USD Liter** | Measure ($) | Retail motor gasoline price per liter in USD |
| **Tax Percentage** | Measure (%) | Effective fiscal tax duty or levy share on retail price |

---

## ⚙️ Step-by-Step Local Setup Guide

### 1. Open Terminal or PowerShell
Navigate to the project root folder:
```bash
cd "c:\Users\Mahima\OneDrive\Desktop\Global fuel prices taxation and trends"
```

### 2. (Recommended) Create and Activate a Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activate on Windows (Command Prompt)
.\venv\Scripts\activate.bat

# Activate on macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 4. Start the Flask Application
```bash
python app.py
```

### 5. Access the Web Application
Open your web browser and navigate to:
```text
http://127.0.0.1:5000/
```

---

## 🔗 How to Embed Your Own Tableau Public Dashboard & Story

### Step A: Publish to Tableau Public
1. Open your completed workbook in **Tableau Desktop**.
2. Go to **Server** &rarr; **Tableau Public** &rarr; **Save to Tableau Public As...**
3. Log in with your Tableau Public account and publish your workbook.

### Step B: Copy the Link
1. On your published Tableau Public webpage, click the **Share** icon (bottom right of viz).
2. Under **Link**, copy the clean URL.
   - Example: `https://public.tableau.com/views/YourWorkbook/YourDashboard`

### Step C: Update `app.py`
The application is pre-configured with Mahima's Tableau Public link:

```python
TABLEAU_CONFIG = {
    "DASHBOARD_URL": "https://public.tableau.com/shared/BWMJZ7N7Z?:display_count=n&:origin=viz_share_link",
    "STORY_URL": "https://public.tableau.com/shared/BWMJZ7N7Z?:display_count=n&:origin=viz_share_link",
    "PROJECT_TITLE": "Global Fuel Prices and Taxation Trends",
    "SUBTITLE": "A Comprehensive Visual Analytics Platform"
}
```

Save `app.py`. The website will automatically reload and display your visualizations!

---

## 🐙 Git and GitHub Instructions

### 1. Initialize Git in the Project
```bash
git init
```

### 2. Stage All Project Files
```bash
git add .
```

### 3. Create First Commit
```bash
git commit -m "Initial commit: Global Fuel Analytics Flask web app with Tableau integration"
```

### 4. Link to Your GitHub Repository
1. Go to [GitHub.com](https://github.com) and click **New Repository**.
2. Name it `global-fuel-analytics`.
3. Keep it **Public** and do NOT check "Add a README" (we already created one).
4. Run:
```bash
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/global-fuel-analytics.git
git push -u origin main
```

---

## ☁️ Free Cloud Deployment Options

You can deploy this Flask application online for free using any of these services:

### Option 1: Deploy on Render.com (Recommended)
1. Sign up for a free account at [Render.com](https://render.com).
2. Click **New +** &rarr; **Web Service**.
3. Connect your GitHub repository `global-fuel-analytics`.
4. Configure settings:
   - **Environment:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Deploy Web Service**. Render will generate your live URL (e.g., `https://global-fuel-analytics.onrender.com`).

### Option 2: Deploy on PythonAnywhere
1. Sign up at [PythonAnywhere.com](https://www.pythonanywhere.com).
2. Go to the **Web** tab &rarr; **Add a new web app** &rarr; Select **Flask** (Python 3.10+).
3. Clone or upload your files and set the WSGI configuration to point to `app.py`.

---

## 💼 SkillWallet Submission Instructions

To submit this project for evaluation on **SkillWallet**:

1. **GitHub Repository URL:**
   - Copy your public GitHub link:
     `https://github.com/<YOUR_GITHUB_USERNAME>/global-fuel-analytics`
   - Paste into the *GitHub URL* field in your SkillWallet project submission.

2. **Live Deployed URL:**
   - Once deployed on Render/PythonAnywhere, copy the live URL (e.g. `https://global-fuel-analytics.onrender.com`).
   - Paste into the *Live Application URL* field in SkillWallet.

3. **Tableau Public Dashboard Link:**
   - Copy your public Tableau dashboard link and add it to your project description or notes section.

---

## ❓ Troubleshooting & FAQs

| Issue | Cause | Solution |
| :--- | :--- | :--- |
| `pip is not recognized` | Python Scripts directory not in Windows PATH | Run commands using `python -m pip install -r requirements.txt` |
| `Address already in use: Port 5000` | Another process is using port 5000 | In `app.py`, change `port=5000` to `port=5001` or run `python app.py --port=5001` |
| Tableau dashboard displays a blank box | Browser tracking prevention or cookie block | Open the link directly using the **Open on Tableau Public** button on the dashboard page |
| `ModuleNotFoundError: No module named 'flask'` | Flask not installed in active environment | Run `python -m pip install flask` |

---

## 📄 License & Attribution

This project is open-source under the MIT License. Developed for academic data visualization and portfolio demonstration.

