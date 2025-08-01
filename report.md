# Lead Scoring Tool for Caprae

## Objective

This tool is a lead quality prediction system that scores potential company leads as **High**, **Medium**, or **Low** quality. It is designed to enhance the lead generation process by helping businesses prioritize outreach and focus efforts on leads with the highest potential.

## Why Machine Learning (ML)?

Rather than applying hardcoded rules, we used a **machine learning model (XGBoost)** to learn patterns from historical data. This approach captures non-obvious interactions between variables like revenue, employee count, business type, and BBB rating, leading to **more accurate and flexible predictions**.

## Dataset and Preprocessing

We created a mock dataset of 2,000 company leads, each with features commonly available in SaaSquatch:

* Business Type (B2B, B2B2C, B2C)
* Revenue
* Employees Count
* Year Founded
* Owner's Title
* BBB Rating

The target label was `Lead Quality` with 3 classes: High, Medium, Low.

### Class Imbalance & SMOTE

Initial class distribution was imbalanced, with more Medium and Low labels. To address this, we used **SMOTE (Synthetic Minority Oversampling Technique)** on the training set, improving the model's ability to learn minority class patterns.

## Model

We used **XGBoost Classifier**, a gradient boosting algorithm suitable for structured data and small-to-medium datasets.

### Evaluation Results:

On a 20% test split:

* **Precision (High Class):** 95%
* **Recall (High Class):** 75%
* **Macro F1-Score:** 0.92
* **Accuracy:** 95%

### Why Precision and Recall Matter More than Accuracy

Instead of focusing on overall accuracy, we prioritized **precision and recall**, particularly for the 'High' lead class. In a real-world sales context, it's critical that leads labeled 'High' are genuinely high-value — mislabeling poor leads as 'High' wastes time and resources. Therefore, precision was our key evaluation metric for business relevance.

## Business Value

Sales teams can use this tool to:

* **Prioritize outreach** to "High" score leads
* **Filter out low-value contacts**
* **Automate lead qualification** within SaaSquatch

## Integration Suggestion

This scoring model can be wrapped as a microservice and integrated into the SaaSquatch pipeline. After scraping lead data, SaaSquatch can call the model to assign a score before displaying or exporting leads.

## Tools Used

* Python, pandas, scikit-learn, imbalanced-learn, xgboost
* Streamlit (for the UI)
* Jupyter Notebook (for model training)

---

This tool aligns with real business needs by offering actionable, scalable lead insights from scraped company metadata.
