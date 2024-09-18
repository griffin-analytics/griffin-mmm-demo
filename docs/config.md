# Configuration Guide for PyMC Marketing-based Media Mix Model

## Overview

To run the Media Mix Model (MMM), you need to create a YAML configuration file. This file specifies the model parameters, data handling options, and column definitions for your input data. This guide explains each section of the configuration file and its parameters.

## Config File Structure

The configuration file is divided into several sections:

1. Data handling options
2. Column definitions
3. Model parameters
4. Prophet components
5. Custom priors

## Data Handling Options

* `raw_data_granularity`: (required) Frequency of the input data. Values: `daily` or `weekly`.
* `train_test_ratio`: (optional) Proportion of the dataset to use for training (in-sample), with the remainder used for out-of-sample testing. Defaults to 0.9 (90% train, 10% test). Possible range: [0.8,1].
* `data_rows`: (optional) Specifies the range of data to use:
  - `total`: Total number of rows in the dataset.
  - `start_date`: Start date of the data to use (format: YYYY-MM-DD).
  - `end_date`: End date of the data to use (format: YYYY-MM-DD).

## Column Definitions

* `ignore_cols`: (optional) List of columns from your CSV that should be ignored.
* `date_col`: (optional) Name of the date column in your CSV. Dates should be in ISO 8601 format (YYYY-MM-DD). Defaults to "date".
* `target_col`: (required) Name of the column with the target (output) metric.
* `extra_features_cols`: (optional) List of extra feature columns. Extra features are factors external to marketing that influence the target.
* `extra_features_impact`: (optional) Specifies the impact direction of extra features (e.g., "negative" for features that decrease the target).
* `media`: (required) One block per media input metric to include in your model. Each block should contain:
  - `display_name`: Name used in charts and reports.
  - `impressions_col`: Column name for impressions data.
  - `spend_col`: Column name for cost data.

## Model Parameters

* `tune`: (optional) Number of tuning steps for the MCMC sampler. Defaults to 2000.
* `draws`: (optional) Number of samples to draw after tuning. Defaults to 2000.
* `chains`: (optional) Number of chains to sample on. Defaults to 4.
* `ad_stock_max_lag`: (optional) Maximum lag for the adstock transformation. Defaults to 8.
* `target_accept`: (optional) Target acceptance rate for the MCMC sampler. Defaults to 0.95.
* `seed`: (optional) Fixed seed for random numbers in the MCMC process.
* `custom_sigma`: (optional) If true, uses custom sigma values for beta_channel priors based on media spend. Defaults to false.

## Prophet Components

* `prophet`: (optional) Configuration for including Prophet components in the model:
  - `include_holidays`: Whether to include holiday effects.
  - `holiday_country`: Country code for holidays (e.g., 'US').
  - `yearly_seasonality`: Whether to include yearly seasonality.
  - `trend`: Whether to include a trend component.
  - `weekly_seasonality`: (optional) Whether to include weekly seasonality.
  - `daily_seasonality`: (optional) Whether to include daily seasonality. Careful: this does not make sense unless using intraday data.

## Custom Priors

* `custom_priors`: (optional) Bayesian priors for model parameters. You can set custom priors for:
  - `intercept`: Base level of the target variable.
  - `beta_channel`: Effectiveness of each marketing channel.
  - `alpha`: Decay rate for the adstock transformation.
  - `lam`: Saturation rate for the marketing response.
  - `likelihood`: Distribution of the target variable.
  - `gamma_control`: Effect of control variables.
  - `gamma_fourier`: Effect of Fourier terms for seasonality.

Each prior is defined by a distribution type (`dist`) and its parameters (`kwargs`).

## Example Configuration

Here's a sample YAML configuration file that demonstrates how to set up the model:

```yaml
################################
# MMM options
################################

model_name: MMM

data_rows:
  total: 171
  start_date: 2019-07-28
  end_date: 2022-10-30  

################################
# Data handling options
################################

raw_data_granularity: weekly
train_test_ratio: 1

################################
# Column definitions
################################

ignore_cols:
  - "price"

date_col: "date"
target_col: "subscribers"

extra_features_cols:
  - "covid_index"
  - "competitor_spend"
  - "promo_events"
  - "other_events"

extra_features_impact:
   "competitor_spend": "negative"

media:
  - display_name: "Media Channel 1"
    impressions_col: media_imp_1
    spend_col: media_cost_1

  - display_name: "Media Channel 2"
    impressions_col: media_imp_2
    spend_col: media_cost_2

  # ... additional media channels ...

################################
# Model parameters
################################

tune: 2000
draws: 2000
chains: 4
ad_stock_max_lag: 8
target_accept: 0.95
seed: 42

################################
# Prophet components
################################

prophet:
  include_holidays: true
  holiday_country: 'US'
  yearly_seasonality: true
  trend: true

################################
# Custom priors
################################

custom_sigma: true
custom_priors:
  intercept:
    dist: LogNormal
    kwargs:
      mu: 0
      sigma: 2
  beta_channel:
    dist: HalfNormal
    kwargs:
      sigma: 2
  alpha:
    dist: Beta
    kwargs:
      alpha: 1
      beta: 3
  lam:
    dist: Gamma
    kwargs:
      alpha: 3
      beta: 1
  likelihood:
    dist: Normal
    kwargs:
      sigma:
        dist: HalfNormal
        kwargs:
          sigma: 2
  gamma_control:
    dist: HalfNormal
    kwargs:
      sigma: 1
  gamma_fourier:
    dist: Laplace
    kwargs:
      mu: 0
      b: 1
```

## Notes

- All columns in the dataset should be mentioned in the config file; if you don't want to use a column in your model, add it to `ignore_cols`.
- The `custom_priors` section allows for fine-tuning of the model's prior distributions. Adjust these based on your domain knowledge or previous modeling results.
- The `prophet` section allows you to incorporate seasonality and holiday effects using Facebook's Prophet library.
- Ensure that your data granularity (`raw_data_granularity`) matches the frequency of your input data.
- The `train_test_ratio` can be set to 1 if you want to use all data for training and don't need a separate test set.

Remember to adjust your configuration file as needed based on your specific data and modeling requirements. The flexibility of the model allows for a wide range of customization in your Media Mix Modeling approach.
