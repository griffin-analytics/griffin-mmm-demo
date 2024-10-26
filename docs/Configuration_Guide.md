# Griffin MMM Configuration Guide

## Introduction
The Griffin Media Mix Model requires a YAML configuration file to define model parameters and data specifications. This guide explains how to create and customize your configuration file.

## Core Configuration Components

### 1. Dataset Configuration
```yaml
# Data timeframe settings
data_rows:
  total: 171                # Total number of observations
  start_date: 2019-07-28    # Analysis start date
  end_date: 2022-10-30      # Analysis end date

# Basic data settings  
raw_data_granularity: weekly # Options: 'daily' or 'weekly'
train_test_ratio: 0.9       # Training set size (0.8-1.0)
```

### 2. Column Mapping
```yaml
# Core column definitions
date_col: "date"           # Date column name
target_col: "subscribers"  # Target variable
target_type: "conversion"  # Target type: 'revenue' or 'conversion'

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

### 3. Media Channel Definitions
```yaml
media:
  - display_name: "Search"
    impressions_col: search_impressions
    spend_col: search_spend

  - display_name: "Social"
    impressions_col: social_impressions
    spend_col: social_spend
```

### 4. Model Settings
```yaml
# MCMC parameters
tune: 2000                  # Tuning steps
draws: 2000                 # Number of samples
chains: 4                   # Number of chains
target_accept: 0.95         # Target acceptance rate
seed: 42                    # Random seed

# Marketing parameters
ad_stock_max_lag: 8         # Maximum lag for carryover
```

### 5. Seasonality Components
```yaml
prophet:
  include_holidays: true    # Include holiday effects
  holiday_country: 'US'     # Country for holidays
  yearly_seasonality: true  # Annual patterns
  trend: true              # Long-term trend
```

### 6. Bayesian Priors (Optional)
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

## Key Considerations

### Data Requirements
- Ensure date formats follow YYYY-MM-DD
- Include all relevant columns in configuration
- Match data granularity with configuration

### Model Parameters
- `train_test_ratio`: Higher values (>0.9) for small datasets
- `ad_stock_max_lag`: Based on expected carryover period
- `chains`: 4+ recommended for convergence checking

### Prior Selection
- Use domain knowledge for prior selection
- Consider historical performance data
- More informative priors for limited data

## Example Configuration
Below is a complete example showcasing all features:

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

## Troubleshooting
- Verify date format consistency
- Check column name accuracy
- Ensure media channel definitions match data
- Validate custom prior specifications

You should adjust parameters based on your specific marketing data and business context.
