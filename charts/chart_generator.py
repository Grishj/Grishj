# charts/chart_generator.py
import matplotlib.pyplot as plt
import os

# Data for test case distribution
data = {'Automated': 75, 'Manual': 25}
labels = list(data.keys())
values = list(data.values())
colors = ['#4CAF50', '#FFC107']

# Create chart
plt.figure(figsize=(6, 4))
plt.bar(labels, values, color=colors)
plt.title("Test Execution Distribution")
plt.ylabel("Test Count")
plt.tight_layout()

# Make sure charts directory exists
os.makedirs("charts", exist_ok=True)
plt.savefig("charts/test_distribution.png")
