
# Results Guide

## Results Directory Structure

The model generates a set of outputs organized into the following categories:

### 1. Model Configuration Files
```
📁 results/
├── config.yaml               # Original configuration
├── model_config.json         # Model parameters
└── output.txt                # Runtime information
```

### 2. Performance Analysis Files

#### Core Metrics
```
📁 results/
├── all_decomp.csv                                                     # Component breakdown
├── media_performance_effect.csv                                       # Channel effects
├── media_performance_roi.csv                                          # ROI analysis
├── response_curves.csv                                                # Detailed channel response curve data
└── media_performance_cost_per_target.csv                              # Cost efficiency
```

### 3. Visualization Outputs

#### Channel Analysis
```
📁 results/
├── Channel Performance/
│   ├── media_contribution_mean.png                                    # Mean contributions
│   ├── media_contribution_median.png                                  # Median contributions
│   ├── media_contribution_share.png                                   # Share analysis
│   ├── media_roi_mean.png                                             # Mean ROI
│   ├── media_roi_median.png                                           # Median ROI
│   └── roi_distribution.png                                           # ROI spread
│
├── Response Analysis/
│   ├── response_curves.png                                           # Channel responses
│   └── channel_contribution_as_function_of_cost_share.png            # Channel relative contribution
│
└── Time Series/
    ├── weekly_media_contribution.png                             # Media contribition over time
    └── weekly_media_and_baseline_contribution.png                # Media and baseline contribition over time
```

#### Model Diagnostics
```
📁 results/
├── Model Fit/
│   ├── model_fit_in_sample.png      # Training fit
│   └── model_fit_predictions.png    # Predictions
│
└── Model Analysis/
    ├── components_contributions.png                    # Components contribition
    ├── model_priors_and_posteriors.png                 # Model priors
    └── waterfall_plot_components_decomposition.png     # Waterfall chart of relative contributions
```

## Detailed File Descriptions

### Configuration Files

1. **model_config.json**
   - Model architecture
   - Parameter settings
   - Prior specifications

2. **output.txt**
   ```text
   Model: Griffin MMM
   Run Date: YYYY-MM-DD
   Configuration Summary:
   - Channels: n
   - Features: n
   - Observations: n
   ```

### Performance Metrics

1. **all_decomp.csv**
   ```csv
   date,baseline,channel_1,channel_2,...
   2024-01-01,value,value,value,...
   ```

2. **media_performance_roi.csv**
   ```csv
   channel,mean_roi,median_roi,lower_95,upper_95
   channel_1,value,value,value,value
   ```

3. **response_curves.csv**
   - Detailed channel response curve data
   ```csv
   channel,x_spend,y_contribution,alpha,lambda
   channel_1,spend_value,contribution_value,alpha_param,lambda_param
   ```
The `response_curves.csv` file contains data that describes the relationship between media spending and its effect on the outcome for each channel. Here's what each column means:

1. `channel`: 
   - The name/identifier of the marketing channel (e.g., TV, Radio, Social Media)

2. `x_spend`: 
   - The amount of money spent on the channel
   - These are evenly spaced points along the spending range used to plot the response curve

3. `y_contribution`: 
   - The predicted contribution (response) for that level of spend
   - Represents how much lift/effect you get from each spending level

4. `alpha`: 
   - The saturation parameter
   - Represents the maximum potential contribution a channel can achieve
   - A higher alpha means the channel has more potential impact

5. `lambda`: 
   - The shape parameter that controls how quickly the response saturates
   - A higher lambda means the response curve reaches saturation more quickly
   - A lower lambda means more gradual diminishing returns

This data essentially maps out the full response curve for each channel, showing how spending (x_spend) translates into business outcomes (y_contribution), while alpha and lambda define the shape of that relationship.

### Visualization Guide

#### Channel Performance Plots

1. **media_contribution_mean.png**
   - Bar plot with error bars
   - Y-axis: Contribution value
   - X-axis: Channels
   - Error bars: 95% HDI

2. **roi_distribution.png**
   - Density plots by channel
   - Y-axis: Density
   - X-axis: ROI values

#### Model Fit Visualizations

1. **model_fit_in_sample.png**
   - Actual vs. Predicted
   - Training period performance
   - Confidence intervals

2. **waterfall_plot_components_decomposition.png**
   - Component-wise contribution
   - Cumulative effects
   - Percentage breakdowns

## Using the Results

### 1. Performance Assessment
```python
# Example: Load ROI analysis
import pandas as pd

roi_data = pd.read_csv('results/media_performance_roi.csv')
print(f"Average ROI by channel:\n{roi_data.groupby('channel')['mean_roi'].mean()}")
```

### 2. Visualization Analysis
```python
# Example: Load and display plots
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def view_result(filename):
    img = mpimg.imread(f'results/{filename}')
    plt.figure(figsize=(12, 8))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

view_result('media_contribution_mean.png')
```

### 3. Model Diagnostics
```python
# Example: Check model fit
import numpy as np

def analyze_fit():
    fit_data = pd.read_csv('results/all_decomp.csv')
    r2 = np.mean(fit_data['r2'])
    print(f"Model R² score: {r2:.3f}")
```

## Best Practices

1. **Version Control**
   - Save results with timestamp
   - Document configuration changes
   - Track model iterations

2. **Analysis Workflow**
   ```python
   # Recommended analysis sequence
   1. Check model fit, especially in sample
   2. Review media performance roi/cpa
   3. Analyze response curves
   4. Examine contributions e.g. waterfall plot
   ```

3. **Documentation**
   - Note key insights
   - Record anomalies
   - Document decisions

