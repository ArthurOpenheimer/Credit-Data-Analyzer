# Credit Risk Classifier

This project is a machine learning pipeline to classify credit risk (good or bad) based on the German Credit dataset. The system uses a Decision Tree classifier optimized to identify risky (bad) credit applicants.

---

## Features

- Clean and preprocess dataset
- Split data into training and testing sets (80/20 split)
- Perform hyperparameter tuning using `GridSearchCV` focusing on maximizing recall for the bad credit class
- Evaluate model with accuracy, confusion matrix, classification report, and visualization
- Interactive command-line input for predicting new credit applications

---

## Libraries Used

- **pandas** — Data manipulation and analysis  
- **SQLAlchemy** — Database connection and querying  
- **scikit-learn** — Machine learning algorithms, model selection, and evaluation  
- **matplotlib** — Plotting and visualization (confusion matrix)  

These libraries provide the core functionality for data loading, preprocessing, model training, tuning, and evaluation.

---

## Project Structure

- `src/main.py` — Main script to run the full workflow: load data, train, tune, evaluate, and predict
- `src/database.py` — Connects to MySQL and loads the dataset
- `src/menu.py` — Interactive terminal menu for user input (currently a stub)
- `src/config.py` — Configuration for database credentials (uses environment variables)
- `init/` — Contains initialization scripts and dataset schema for MySQL
- `docker-compose.yml` — Defines a MySQL service with data initialization
- `requirements.txt` — Python dependencies

---

## Setup Instructions

1. Create a `.env` file in the root folder with your MySQL credentials:
```bash
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=your_database_name
```


2. Ensure MySQL is running on port 3307 (or modify connection string in `src/database.py` accordingly).

3. Run MySQL with the initialization scripts inside `init/` to create the database and load the German Credit dataset.

4. Install Python dependencies:

```bash
pip install -r requirements.txt
```

5. Run the main script:
```bash
python src/main.py
```