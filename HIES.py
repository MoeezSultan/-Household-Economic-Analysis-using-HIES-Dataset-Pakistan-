import pandas as pd

df=pd.read_excel(r"C:\Users\HP user\Desktop\Data Science\python\Household Integrated Economic Survey (HIES) Curated\HIES_Provisional.xlsx", sheet_name='Provincial')
print(df.head())

print(df.columns)

# Force numeric conversion (invalid strings will become NaN)
df['Total Expenditure'] = pd.to_numeric(df['Total Expenditure'], errors='coerce')

df = df.dropna(subset=['Total Expenditure'])


# Now apply groupby safely
category_summary = df.groupby("Category")['Total Expenditure'].sum().sort_values(ascending=False)
print(category_summary)

# Category-wise Share
import matplotlib.pyplot as plt

top_categories = category_summary.head(8)

plt.figure(figsize=(8, 8))
plt.pie(top_categories, labels=top_categories.index, autopct='%1.1f%%')
plt.title('Top Expense Categories (Pakistan – HIES)')
plt.show()

# Bar Plot – Highest Expense Categories
top_categories.plot(kind='bar', color='skyblue')
plt.ylabel('Total Expenditure (PKR)')
plt.title('Top Expense Categories')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Line Chart – Yearly Total Expenditure
yearly_exp = df.groupby('Years')['Total Expenditure'].sum()

yearly_exp.plot(kind='line', marker='o', color='green')
plt.ylabel('Total Expenditure')
plt.title('Year-wise Household Spending Trend')
plt.grid(True)
plt.show()



