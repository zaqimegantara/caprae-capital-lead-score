# Lead Scoring Tool for Caprae

A machine learning-powered lead scoring app to help prioritize high-potential leads based on business metadata like revenue, employees, and BBB rating.

---

## Features

* Predicts lead quality: **High**, **Medium**, or **Low**
* Built using **XGBoost** with **SMOTE** to address class imbalance
* Clean and interactive **Streamlit** user interface
* Accepts manual input to simulate scoring scraped companies

---

## Project Structure

```
caprae-lead-scorer/
├── app.py                       # Streamlit UI for lead prediction
├── train_model.ipynb           # Model training and preprocessing pipeline
├── create_mock_dataset.ipynb   # Optional: used to generate the mock data
├── label_leads.py              # Optional: script to label leads with quality
├── labeled_mock_leads_dataset_2000.csv  # Labeled mock dataset
├── lead_scorer_smote.pkl       # Trained XGBoost model
├── preprocessor.pkl            # Preprocessing pipeline
├── label_encoder.pkl           # Label encoder for target classes
├── report.md                   # Project summary and rationale
├── README.md                   # Project setup and usage instructions
├── requirements.txt            # Python dependencies
```

---

## How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

*(or manually install: `streamlit`, `xgboost`, `scikit-learn`, `pandas`, `imblearn`, `joblib`)*

### 2. Run the Streamlit App

```bash
streamlit run app.py
```

---

## Model Overview

* **Algorithm**: XGBoost Classifier
* **Class Labels**: High, Medium, Low
* **Features Used**:

  * Business Type
  * Revenue
  * Employees Count
  * Year Founded
  * Owner's Title
  * BBB Rating
* **Evaluation (Test Set):**

  * Accuracy: 95%
  * Precision (High): 95%
  * Macro F1-score: 0.92

---

## Business Context

Designed as an add-on to tools like **SaaSquatch**, this model can be integrated post-scraping to:

* Prioritize high-impact leads
* Reduce manual effort
* Improve B2B outreach performance

---

## Demo Video

*Include a short screen recording of your app usage here.*

---

## Author

Rizky Zaqi Megantara   
Machine Learning Intern Applicant for Caprae Capital

---

