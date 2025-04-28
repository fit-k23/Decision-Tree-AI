import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Generate the dataset
n_samples = 1000
classes = ['Positive', 'Negative']
data = pd.DataFrame({
    'features': np.random.randn(n_samples),
    'label': np.random.choice(classes, size=n_samples, p=[0.8, 0.2])
})

# Define test proportions
test_proportions = [0.2, 0.4, 0.6, 0.8]

# Prepare figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, test_size in enumerate(test_proportions):
    # Split dataset with stratification
    X_train, X_test, y_train, y_test = train_test_split(
        data['features'], data['label'], test_size=test_size, stratify=data['label'], random_state=42
    )

    # Count class distributions
    original_counts = data['label'].value_counts().reindex(classes)
    train_counts = pd.Series(y_train).value_counts().reindex(classes)
    test_counts = original_counts - train_counts # pd.Series(y_test).value_counts().reindex(classes)
    test_counts2 = pd.Series(y_test).value_counts().reindex(classes)
    print(f"O: {original_counts}\nT: {train_counts}\nt1: {test_counts}\nt2: {test_counts2}")
    # Create DataFrame for plotting
    df = pd.DataFrame({
        'Original': original_counts,
        'Train': train_counts,
        'Test': test_counts
    })

    # Plot stacked bar chart
    df.T.plot(kind='bar', stacked=True, ax=axes[i], color=['#1f77b4', '#ff7f0e'], width=0.8)
    axes[i].set_facecolor('white')

    axes[i].set_title(f'Train/Test Split: {round((1-test_size)*100)}/{round(test_size*100)}')
    axes[i].set_ylabel('Count')
    axes[i].legend(title='Class', labels=classes)
    axes[i].tick_params(axis='x', rotation=0)

plt.tight_layout()
# plt.savefig('class_distribution_stacked.png')
plt.show()