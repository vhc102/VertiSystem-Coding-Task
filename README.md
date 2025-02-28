# Flight Data Processing and CI/CD Pipeline for Electricity Prices Model

## Task 1: Flight Data Processing

### Overview
This project generates, analyzes, and cleans flight data stored as JSON files. The program is written in Python 3.7+ and operates in two main phases:

1. **Generation Phase**: Generates ~5000 JSON files containing random flight data.
2. **Analysis & Cleaning Phase**: Processes the generated files efficiently to derive key insights.

### Features

#### 1. Generation Phase
- Generates N ≈ 5000 JSON files in `/tmp/flights/%MM-YY%-%origin_city%-flights.json`.
- Each file contains M = [50–100] flight records.
- Flight data consists of `{date, origin_city, destination_city, flight_duration_secs, passengers_on_board}`.
- Cities range from K = [100–200].
- Random probability L = [0.5%–0.1%] for null values in records.

#### 2. Analysis & Cleaning Phase
- Processes all files efficiently.
- Outputs:
  - **Total number of records processed**
  - **Count of dirty records (records with null values)**
  - **Total runtime duration**
  - **AVG and 95th percentile (P95) of flight duration for the Top 25 destination cities**
  - **Cities with maximum passengers arriving and departing**

---

## Task 2: CI/CD Pipeline for Electricity Prices Model

### Overview
This project automates the deployment and execution of a Random Forest model for U.S. electricity prices using a CI/CD pipeline. The model is containerized for ease of deployment and reproducibility.

### Features

1. **CI/CD Pipeline**
   - Automated testing, building, and deployment.
   - High-level flow diagram for pipeline execution.

2. **Containerization**
   - Dockerized model and dependencies for portability.
   - Ensures consistent runtime across different environments.

### YAML File in CI/CD Pipelines
A **YAML (Yet Another Markup Language) file** is an essential component in automating CI/CD pipelines. It:
- Defines build, test, and deployment steps in a structured format.
- Helps ensure consistency in workflow execution.
- Is used by CI/CD tools like GitHub Actions, Jenkins, and GitLab CI/CD.

---

### Author
Developed by Vahta Chaudhary.

