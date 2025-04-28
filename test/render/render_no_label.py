!python -m pip install seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Set random seed for reproducibility
np.random.seed(42)

# Simulate a dataset with 1000 samples and 3 classes
n_samples = 1000
classes = ['Positive', 'Negative']
data = pd.DataFrame({
    'features': np.random.randn(n_samples),
    'label': np.random.choice(classes, size=n_samples, p=[0.8, 0.2])
})

# Define train-test split proportions
test_proportions = [0.2, 0.3, 0.4, 0.8]

# Function to compute class distribution
def get_class_distribution(y, dataset_name):
    distribution = y.value_counts(normalize=True).sort_index()
    return pd.DataFrame({
        'Class': distribution.index,
        'Proportion': distribution.values,
        'Dataset': dataset_name
    })

# Collect distributions for visualization
distributions = [get_class_distribution(data['label'], 'Original')]

# Original dataset distribution

# Perform train-test splits and collect distributions
for test_size in test_proportions:
    # Stratified split
    X_train, X_test, y_train, y_test = train_test_split(
        data['features'], data['label'],
        train_size=1 - test_size, test_size=test_size,
        stratify=data['label'], random_state=42
    )

    # Training set distribution
    distributions.append(get_class_distribution(y_train, f'Train ({int((1 - test_size)*100)}%)'))

    # Test set distribution
    distributions.append(get_class_distribution(y_test, f'Test ({int(test_size*100)}%)'))

# Combine all distributions into a single DataFrame
dist_df = pd.concat(distributions, ignore_index=True)

# Visualize class distributions
plt.figure(figsize=(12, 6))
sns.barplot(x='Class', y='Proportion', hue='Dataset', data=dist_df)
plt.title('Class Distributions Across Original, Training, and Test Sets')
plt.ylabel('Proportion')
plt.xlabel('Class')
plt.legend(title='Dataset', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()