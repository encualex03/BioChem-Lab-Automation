# 🧬 Bio-Analytical Data Processor (Automated Lab Reporting)

### 🌟 Project Overview
This project demonstrates an automated pipeline for processing biochemical laboratory data using **Python** and **Pandas**. As a student in **Technological Biochemistry** transitioning into **Bioinformatics**, I developed this tool to bridge the gap between manual laboratory observations and scalable data engineering.

The script automates the application of the **Beer-Lambert Law**, transforming raw absorbance readings into precise molar concentrations while ensuring data integrity through rigorous cleaning protocols.

---

### 🚀 Key Technical Features
* **Automated Data Ingestion:** Reads experimental data directly from CSV files, simulating real-world lab outputs.
* **Advanced Data Cleaning:** * Utilizes `pd.to_numeric` with `errors='coerce'` to handle corrupted data or manual entry errors.
    * Filters out non-physical values (e.g., negative absorbance) to ensure scientific accuracy.
* **Vectorized Calculations:** Uses Pandas' vectorized operations for high-performance calculations.
* **Robust Error Handling:** Implements `try-except` blocks to manage missing files and unexpected runtime exceptions.

---

### 🛠 Tech Stack
* **Language:** Python 3.x
* **Libraries:** `pandas`, `numpy`
* **Domain Knowledge:** Biochemistry (Beer-Lambert Law), Data Validation.

---

### 📊 How it Works
The script processes a raw dataset (e.g., `raw_lab_data.csv`), removes invalid entries, calculates concentrations based on a molar extinction coefficient, and exports a final report ready for analysis.