# 🚀 CI/CD Pipeline for API & UI Testing

## 📖 Project Overview
This project demonstrates an automated **CI/CD pipeline** for testing both **API and UI components** using **GitHub Actions**.
The goal is to ensure software quality by integrating continuous testing into the development workflow.

## 🛠️ Tech Stack
- **Backend API**: Node.js + Express.js
- **Database**: MongoDB (Mongoose)
- **API Testing**: Postman + Newman
- **UI Testing**: Selenium + Python
- **CI/CD Pipeline**: GitHub Actions
- **Version Control**: Git + GitHub

## 🚀 How It Works

1. **API Testing**  
   - Uses **Postman** collection (`APITesting.postman_collection.json`)
   - Runs tests using **Newman** in the CI/CD pipeline

2. **UI Testing**  
   - Uses **Selenium WebDriver** for automated UI tests
   - Written in **Python**, executed in the pipeline

3. **CI/CD Pipeline (GitHub Actions)**  
   - Runs API tests using Postman/Newman
   - Runs UI tests using Selenium/Python
   - Automatically triggered on **push & pull requests**

##  ⏳ Workflows Overview

### 📌 API Testing Workflow (`.github/workflows/api-tests.yml`)
- Runs **Postman Newman tests** on API endpoints.
- Ensures API responses match expected results.
- Checks for regressions to maintain API stability.

### 📌 UI Testing Workflow (`.github/workflows/ui-tests.yml`)
- Executes **Selenium WebDriver** tests for UI validation.
- Ensures frontend functionality remains intact.

## 📊 Test Reports
- UI Automated test reports are generated and stored as **`report.html`**.
- You can view test logs and results directly in **GitHub Actions**.




