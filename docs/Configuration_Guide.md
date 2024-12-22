# Griffin MMM Configuration Guide

## Welcome to Griffin MMM

Griffin MMM is a powerful tool for marketing mix modelling that uses a YAML configuration file to define model parameters, data mappings, and custom settings. This guide will help you create and customize your configuration file to suit your marketing data and analysis needs.

---

## Key Features of the Configuration File
With the Griffin MMM configuration file, you can:
- Define data preprocessing and column mappings
- Configure Bayesian priors for model parameters
- Specify holiday and seasonality effects
- Customize media channel definitions
- Adjust advanced model settings like lags and MCMC parameters

---

## Core Configuration Components

### 1. Dataset Configuration
Define your dataset's timeframe and granularity:
```yaml
# Data timeframe settings
data_rows:
  total: 171                # Total number of observations
  start_date: 2019-07-28    # Analysis start date
  end_date: 2022-10-30      # Analysis end date

# Basic data settings  
raw_data_granularity: weekly # Options: 'daily' or 'weekly'
train_test_ratio: 0.9       # Proportion of dataset for training (e.g., 0.8-1.0)
```
**Tips:**
- Use `daily` granularity for high-frequency data like app events.
- Set `train_test_ratio` closer to 1.0 for small datasets to maximise training data.

---

### 2. Column Mapping
Map dataset columns to model requirements:
```yaml
# Core column definitions
date_col: "date"           # Date column name
target_col: "subscribers"  # Target variable
target_type: "conversion"  # Options: 'revenue' or 'conversion'

# Optional columns to exclude
ignore_cols:
  - "price"
  - "irrelevant_metric"

# External factors
extra_features_cols:
  - "covid_index"
  - "competitor_spend"
  - "promo_events"

# Direction of impact
extra_features_impact:
  "competitor_spend": "negative"
```
**Tips:**
- Ensure `date_col` matches the column name in your dataset.
- Add all external factors that influence the target variable under `extra_features_cols`.
- Clearly define whether external features have a positive or negative impact.

---

### 3. Media Channel Definitions
Define your media channels with associated impressions and spend columns:
```yaml
media:
  - display_name: "Search"
    impressions_col: search_impressions
    spend_col: search_spend

  - display_name: "Social"
    impressions_col: social_impressions
    spend_col: social_spend
```
**Tips:**
- Ensure all media channel columns exist in your dataset.
- Use descriptive `display_name` values for clear reporting.

---

### 4. Model Settings
Configure key model parameters for MCMC sampling and marketing carryover:
```yaml
# MCMC parameters
tune: 2000                  # Number of tuning steps
draws: 2000                 # Number of samples per chain
chains: 4                   # Number of chains for sampling
target_accept: 0.95         # Target acceptance rate for proposals
seed: 42                    # Random seed for reproducibility

# Marketing parameters
ad_stock_max_lag: 8         # Maximum lag for carryover effects, up to 12
```
**Tips:**
- Use at least 4 chains to ensure robust convergence checks.
- Adjust `ad_stock_max_lag` based on the expected duration of marketing effects (e.g., set higher for branding campaigns).

---

### 5. Seasonality and Trend
Add seasonality and holiday effects to your model:
```yaml
prophet:
  include_holidays: true    # Include holiday effects
  holiday_country: 'US'     # Country for holiday calendar
  yearly_seasonality: true  # Include yearly patterns
  trend: true               # Include long-term trends
```
**Tips:**
- Set `include_holidays` to `true` to account for events like Black Friday.
- Adjust `holiday_country` to match your target audience's region.

---

### 6. Bayesian Priors (Optional)
Define priors for model parameters to incorporate domain knowledge:
```yaml
custom_priors:
  # Channel effectiveness prior
  beta_channel:
    dist: LogNormal
    kwargs:
      mu: [2, 1.5, 1]        # One per channel
      sigma: [0.5, 0.8, 1.2] # One per channel

  # Response curve priors
  alpha:
    dist: Beta
    kwargs:
      alpha: 1
      beta: 3

  # Saturation prior  
  lam:
    dist: Gamma
    kwargs:
      alpha: 3
      beta: 1
```
**Tips:**
- Use priors to encode expectations based on historical data or domain expertise.
- For limited datasets, apply more informative priors to stabilise the model.

---

## Best Practices

### Data Requirements
- Ensure date formats are consistent and follow `YYYY-MM-DD`.
- Verify column names in the YAML file match your dataset exactly.

### Choosing Parameters
- **`train_test_ratio`**: Set higher values (>0.9) for small datasets.
- **`ad_stock_max_lag`**: Align with the longest carryover period expected for your campaigns.
- **`chains`**: Use 4 or more for effective posterior sampling.

### Prior Selection
- Use domain knowledge for priors when possible.
- Apply uniform or less restrictive priors for exploratory models.

---

## Example Configuration File
Here’s a complete example YAML file:
```yaml
# Basic Settings
raw_data_granularity: weekly
train_test_ratio: 0.9
ad_stock_max_lag: 8

# Data Column Mapping
date_col: "date"
target_col: "conversions"
target_type: "conversion"

extra_features_cols:
  - "seasonality_index"
  - "market_conditions"

# Media Channels  
media:
  - display_name: "Paid Search"
    impressions_col: search_imp
    spend_col: search_cost

  - display_name: "Social Media"
    impressions_col: social_imp
    spend_col: social_cost

# Model Configuration
tune: 2000
draws: 2000
chains: 4
target_accept: 0.95
seed: 42

# Seasonality
prophet:
  include_holidays: true
  holiday_country: 'US'
  yearly_seasonality: true
  trend: true
```

---

## Troubleshooting

### Common Issues
- **Date Format Errors**: Ensure all dates are in `YYYY-MM-DD` format.
- **Column Name Mismatches**: Check that all column names in the YAML file exist in your dataset.
- **Invalid Priors**: Verify that all priors follow valid distributions and parameter ranges.

### Solutions
- Use the `ignore_cols` field to exclude irrelevant or problematic columns.
- Double-check file paths and dataset headers.
