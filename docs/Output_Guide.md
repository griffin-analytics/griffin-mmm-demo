# Griffin MMM Results Guide

## Introduction

Griffin MMM generates a variety of outputs to help you evaluate model performance, understand channel contributions, and optimise marketing strategies. This guide explains the structure and purpose of these outputs, providing practical examples to help you make the most of your results.

---

## Results Directory Structure

The results are organised into three main categories: configuration files, performance metrics, and visualisations.

### Directory Overview
```plaintext
📁 results/
├── config.yaml                                 # Original configuration
├── model_config.json                           # Model parameters
├── all_decomp.csv                              # Component breakdown
├── media_performance_roi.csv                   # ROI analysis
├── response_curves.csv                         # Response curve data
├── media_contribution_mean.png                 # Mean contributions
├── model_fit_in_sample.png                     # Training fit
└── waterfall_plot_components_decomposition.png # Contribution decomposition
```

---

## Key Files and Their Use

### Configuration Files

- **`config.yaml`**: The original configuration file used to run the model.
- **`model_config.json`**: A JSON file capturing the model parameters, priors, and architecture.
- **`output.txt`**: A summary of runtime information and configuration details.

#### Example:
```text
Model: Griffin MMM
Run Date: YYYY-MM-DD
Configuration Summary:
- Channels: n
- Features: n
- Observations: n
```

### Performance Metrics

1. **`all_decomp.csv`**: Breakdown of contributions by date and component.
   ```csv
   date,baseline,channel_1,channel_2,...
   2024-01-01,value,value,value,...
   ```
   **Use Case**: Analyse how different components contribute over time.

2. **`media_performance_roi.csv`**: Channel-level ROI metrics.
   ```csv
   channel,mean_roi,median_roi,lower_95,upper_95
   channel_1,value,value,value,value
   ```
   **Use Case**: Identify channels with the highest ROI.

3. **`response_curves.csv`**: Detailed response curve data for each channel.
   ```csv
   channel,x_spend,y_contribution,alpha,lambda
   channel_1,spend_value,contribution_value,alpha_param,lambda_param
   ```
   **Use Case**: Understand the relationship between spend and outcomes, including saturation effects.

### Practical Example
```python
import pandas as pd

# Load ROI data
roi_data = pd.read_csv('results/media_performance_roi.csv')
print(roi_data[['channel', 'mean_roi']])
```

---

## Visualisation Outputs

Griffin MMM generates visualisations to simplify analysis and support decision-making.

### Channel Performance Visualisations

- **`media_contribution_mean.png`**:
  - Bar plot showing the mean contribution of each channel.
  - **Use Case**: Compare channel effectiveness.

- **`roi_distribution.png`**:
  - Density plot of ROI values across channels.
  - **Use Case**: Evaluate ROI consistency for each channel.

### Model Diagnostics Visualisations

- **`model_fit_in_sample.png`**:
  - Plot comparing actual vs. predicted values during the training period.
  - **Use Case**: Validate model accuracy.

- **`waterfall_plot_components_decomposition.png`**:
  - Waterfall chart breaking down contributions by components.
  - **Use Case**: Understand the relative impact of different components on the target metric.

#### Practical Example
```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Display a visualisation
def view_result(filename):
    img = mpimg.imread(f'results/{filename}')
    plt.figure(figsize=(12, 8))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

view_result('media_contribution_mean.png')
```

---

## Using the Results

### Recommended Workflow

1. **Evaluate Model Fit**:
   - Check `model_fit_in_sample.png` to ensure the model accurately predicts training data.

2. **Analyse Channel Contributions**:
   - Use `media_performance_roi.csv` and `all_decomp.csv` to assess channel performance and ROI.

3. **Explore Response Curves**:
   - Review `response_curves.csv` to understand diminishing returns and optimise spend.

4. **Examine Overall Contributions**:
   - Use `waterfall_plot_components_decomposition.png` to see the relative impact of all components.

### Example Workflow
```python
# Load and summarise decomposition data
import pandas as pd

decomp_data = pd.read_csv('results/all_decomp.csv')
print(decomp_data.head())

# Calculate total baseline contribution
baseline_total = decomp_data['baseline'].sum()
print(f"Total Baseline Contribution: {baseline_total}")
```

---

## Best Practices

1. **Version Control**:
   - Save results with timestamps to track iterations.
   - Document any changes to the configuration or data.

2. **Data Validation**:
   - Ensure input data is clean and matches the configuration.
   - Verify column names in the configuration file.

3. **Documentation**:
   - Record key insights from the results.
   - Note any anomalies or unexpected outcomes.

4. **Iterative Analysis**:
   - Re-run the model periodically to account for new data or changes in strategy.

---

Griffin MMM provides a robust framework for marketing mix analysis. Use this guide to navigate your results effectively and derive actionable insights to optimise your marketing strategies.

