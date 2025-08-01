import pandas as pd

# Load the dataset
df = pd.read_csv("mock_leads_dataset_2000.csv")

# Labeling function
def label_lead(row):
    score = 0

    # Business Type
    if row['Business Type'] == 'B2B':
        score += 20
    elif row['Business Type'] == 'B2B2C':
        score += 10

    # Revenue (in millions)
    if 0.5 <= row['Revenue'] <= 5:
        score += 20
    elif row['Revenue'] > 5:
        score += 10

    # Employees
    if 10 <= row['Employees Count'] <= 100:
        score += 15

    # Age
    company_age = 2025 - int(row['Year Founded'])
    if 5 <= company_age <= 15:
        score += 15

    # Owner Title
    title = str(row["Owner's Title"]).lower()
    if 'ceo' in title or 'founder' in title:
        score += 10

    # BBB Rating
    if row['BBB Rating'] in ['A+', 'A']:
        score += 5

    # Final label
    if score >= 70:
        return 'High'
    elif score >= 40:
        return 'Medium'
    else:
        return 'Low'

# Apply labeling
df['Lead Quality'] = df.apply(label_lead, axis=1)

# Save the labeled dataset
df.to_csv("labeled_mock_leads_dataset_2000.csv", index=False)
