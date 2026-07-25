# Türkiye Yazılımcı Maaşları

An end-to-end Data Engineering and Data Visualization project that transforms raw software salary survey data into an interactive analytics website.

**Live Demo:** https://www.egeaksoy.net/yazilimcimaaslari/

---

## Overview

This project analyzes salary data collected from **5,003 anonymous software professionals** in Turkey and presents the results through an interactive web application.

Instead of exposing the raw survey data, the project focuses on building a complete data pipeline that cleans, validates, transforms, aggregates, and visualizes the information.

The goal was not only to create charts, but to simulate a real-world data engineering workflow—from raw data ingestion to a production-ready analytics product.

---

## Features

- Interactive salary analytics
- Position-based median salary comparison
- Salary progression by experience level
- Company size vs. salary analysis
- Position-to-position salary comparison
- Dynamic filtering
- Responsive design
- SEO-friendly pages
- Accessible and mobile-friendly interface

---

# Project Architecture

```
Raw Survey Data
        │
        ▼
Python ETL Pipeline
        │
        ▼
Validation
        │
        ▼
Cleaning & Transformation
        │
        ▼
Aggregation
        │
        ▼
Processed CSV Files
        │
        ▼
React Dashboard
        │
        ▼
Interactive Data Visualizations
```

---

# Data Engineering Workflow

The project was intentionally designed around an ETL pipeline rather than directly visualizing raw survey data.

### 1. Extraction

Raw survey data was imported from Excel using **pandas**.

---

### 2. Validation

Before processing, the dataset is validated to ensure that all required columns exist.

Validation prevents the pipeline from continuing when mandatory fields are missing.

---

### 3. Data Cleaning

The pipeline standardizes:

- Salary values
- Experience categories
- Company size labels
- Currency values

Invalid or unexpected values are detected during this stage.

---

### 4. Currency Normalization

Salary values originally stored in different currencies are converted into Turkish Lira using predefined exchange rates.

This allows all salaries to be compared on the same scale.

---

### 5. Aggregation

Instead of exposing individual salaries, multiple analytical datasets are generated.

The project currently produces three processed datasets:

- Salary summary by position
- Salary summary by position and experience
- Salary summary by company size and seniority

Median salary is used throughout the project because salary distributions often contain significant outliers.

---

### 6. Visualization

The processed datasets are consumed by a React application that renders interactive charts using Recharts.

Users can explore the data without exposing any raw survey responses.

---

# Tech Stack

## Data Engineering

- Python
- pandas

## Frontend

- React
- Recharts
- Papa Parse

## Deployment

- Vercel

---

# What I Learned

This project was built primarily as a learning experience in Data Engineering.

Throughout the development process I gained hands-on experience with:

## ETL Pipelines

- Designing modular ETL pipelines
- Separating extraction, transformation, validation and loading logic
- Building reusable pipeline components

---

## Data Validation

- Detecting malformed datasets
- Validating required columns
- Preventing invalid data from entering the pipeline

---

## Data Cleaning

- Standardizing categorical values
- Cleaning inconsistent labels
- Preparing datasets for aggregation

---

## Data Transformation

- Currency normalization
- Feature engineering
- Dataset restructuring

---

## Data Aggregation

- Grouping data using pandas
- Computing median salary statistics
- Creating analysis-ready datasets

---

## Frontend Data Visualization

- Building reusable chart components
- Working with CSV datasets in React
- Designing interactive analytical dashboards
- Creating responsive data visualizations

---

## Software Engineering

- Modular project structure
- Separation of concerns
- Reusable components
- Clean code practices
- End-to-end project organization

---

# Repository Structure

```
project
│
├── data
│
├── reports
│
├── src
│   └── salary_switch
│       ├── extraction
│       ├── validation
│       ├── transformation
│       ├── loading
│       └── pipelines
│
├── processed_data
│
└── frontend
```

---

# Data Source

The original survey data used in this project was obtained from the following public GitHub repository:

https://github.com/oncekiyazilimci/2026-yazilim-sektoru-maaslari

The original survey and raw responses belong to the repository owner and contributors.

This project does **not** claim ownership of the original dataset.

My contribution consists of:

- data validation
- data cleaning
- data transformation
- aggregation
- ETL pipeline development
- frontend implementation
- interactive visualization
- analytical presentation

---

# Disclaimer

This project is an independent educational and portfolio project.

The visualizations are based on publicly available anonymous survey responses.

The results should be interpreted as aggregated survey statistics and **not** as official salary benchmarks for the Turkish software industry.

Sample sizes differ across positions, experience levels and company sizes.

---

# Future Improvements

Some ideas planned for future versions:

- Multi-year salary comparisons
- Inflation-adjusted salaries
- Additional analytical datasets
- Interactive filtering improvements
- Downloadable reports
- More advanced statistical analysis
- Automated ETL updates
- CI/CD pipeline for automatic data refresh

---

# Author

**Ege Aksoy**

Computer Technologies and Information Systems (CTIS) Student  
Bilkent University

Portfolio  
https://www.egeaksoy.net

LinkedIn  
https://www.linkedin.com/in/egeaksoy00/

GitHub  
https://github.com/egeaksoy00

Email

egeaksoy@ug.bilkent.edu.tr

---

If you have any suggestions, improvements, or find any issues, feel free to contact me.
