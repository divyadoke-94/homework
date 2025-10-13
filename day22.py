#Seaborn Implementation - All in One Code

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
tips = sns.load_dataset("tips")

# 1. Scatter Plot
plt.figure(figsize=(6,4))
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex", style="time")
plt.title("Scatter Plot - Total Bill vs Tip")
plt.show()

# 2. Line Plot
plt.figure(figsize=(6,4))
sns.lineplot(x="size", y="total_bill", data=tips, ci=None)
plt.title("Line Plot - Total Bill vs Size")
plt.show()

# 3. Bar Plot
plt.figure(figsize=(6,4))
sns.barplot(x="day", y="total_bill", data=tips, hue="sex")
plt.title("Bar Plot - Average Total Bill per Day")
plt.show()

# 4. Count Plot
plt.figure(figsize=(6,4))
sns.countplot(x="day", data=tips, hue="sex")
plt.title("Count Plot - Customers per Day")
plt.show()

# 5. Box Plot
plt.figure(figsize=(6,4))
sns.boxplot(x="day", y="total_bill", data=tips, hue="sex")
plt.title("Box Plot - Total Bill Distribution")
plt.show()

# 6. Violin Plot
plt.figure(figsize=(6,4))
sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
plt.title("Violin Plot - Distribution by Day and Gender")
plt.show()

# 7. Heatmap (Correlation Matrix)
plt.figure(figsize=(6,4))
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# 8. Pairplot
sns.pairplot(tips, hue="sex")
plt.suptitle("Pairplot of Tips Dataset", y=1.02)
plt.show()

# 9. Distribution Plot (Histogram + KDE)
plt.figure(figsize=(6,4))
sns.histplot(tips["total_bill"], kde=True, bins=20)
plt.title("Distribution of Total Bill")
plt.show()

# 10. Regression Plot
plt.figure(figsize=(6,4))
sns.regplot(x="total_bill", y="tip", data=tips)
plt.title("Regression Plot - Tip vs Total Bill")
plt.show()