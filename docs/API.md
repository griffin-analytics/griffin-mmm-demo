# API Reference

## MMMBaseDriver

This is the primary interface for using the MMM Wrapper.

### Methods:

- `__init__(self, config_path, data_path)`: Initializes the driver with configuration and data.
- `check_quality(self)`: Performs data quality checks.
- `fit_model(self)`: Fits the MMM model to the data.
- `predict_on_test(self)`: Generates predictions on test data.
- `plot_posterior_predictive(self)`: Visualizes posterior predictive checks.
- `plot_components_contributions(self)`: Plots component contributions.

## ModelBuilder

This class is used for building and configuring MMM models.

### Methods:

- `__init__(self, config)`: Initializes with model configuration.
- `build_model(self, data)`: Builds the PyMC model based on configuration and data.
- `fit(self, data)`: Fits the model to the provided data.

## Utility Functions

### Data Preprocessing

- `preprocessing_method_X(X)`: Preprocesses feature data.
- `preprocessing_method_y(y)`: Preprocesses target data.
- `validate_data(data)`: Validates input data structure and content.

### Optimization

- `optimize_marketing_budget(model, data, constraints)`: Optimizes marketing budget allocation.

### Visualization

- `plot_correlation_matrix(data)`: Plots correlation matrix of input features.
- `plot_model_structure(model)`: Visualizes the structure of the PyMC model.
- `plot_posterior_predictions(idata)`: Plots posterior predictive checks.

## Data Preparation Guide

### Input Data Format

The MMM Wrapper expects input data in a specific format. This guide will help you prepare your data correctly.

#### Required Columns

- Date: A datetime column representing the time period for each observation.
- Target: The metric you're trying to predict (e.g., sales, conversions).
- Media Channels: Separate columns for each media channel's spend or activity.
- Control Variables: Any additional variables that might influence the target.

#### Example DataFrame Structure

| Date       | Target | TV_Spend | Radio_Spend | Newspaper_Spend | Holiday | Temperature |
|------------|--------|----------|-------------|-----------------|---------|-------------|
| 2023-01-01 | 1000   | 5000     | 2000        | 1000            | 1       | 20          |
| 2023-01-02 | 1200   | 5500     | 2100        | 1100            | 0       | 22          |
| ...        |        |          |             |                 |         |             |

### Data Quality Checks

Before fitting the model, the MMM Wrapper performs several data quality checks:

- Missing Values: Ensure there are no missing values in your dataset.
- Data Types: Verify that all columns have the correct data types.
- Date Continuity: Check that there are no gaps in the date sequence.
- Spend Fractions: Highlight channels with very low spend fractions.
- Variance Inflation Factor (VIF): Check for multicollinearity among predictors.

### Preprocessing Steps

The MMM Wrapper includes several preprocessing steps:

- Scaling: Media spend and control variables are scaled to improve model convergence.
- Outlier Detection: Optionally remove or cap outliers in the target variable.
- Date Features: Automatically generate date-related features (e.g., day of week, month).

### Using the InputData Class

The InputData class is used to encapsulate and validate your input data:

```python
from mmm_wrapper.data import InputData

input_data = InputData(
    df=your_dataframe,
    date_col='Date',
    target_col='Target',
    media_cols=['TV_Spend', 'Radio_Spend', 'Newspaper_Spend'],
    extra_features=['Holiday', 'Temperature']
)
```

## Plotting Functions

These functions are used for visualizing various aspects of the model and its results.

- `_plot_one_metric(metric)`: Plots a single metric over time.
- `plot_all_metrics(metrics)`: Plots all metrics over time.
- `all_contributions_plot(contributions)`: Plots the contributions of all components over time.
- `get_plot_coords(coords)`: Gets the coordinates for plotting.
- `get_total_coord_size(size)`: Gets the total size of the coordinate grid for plotting.
- `set_subplot_kwargs_defaults(defaults)`: Sets default values for subplot keyword arguments.
- `selections(selections)`: Selects which plots to display.
- `plot_hdi(hdi)`: Plots the highest density interval.
- `random_samples(samples)`: Plots random samples from the posterior distribution.
- `plot_samples(samples)`: Plots all samples from the posterior distribution.
- `plot_curve(curve)`: Plots a curve based on the model's parameters.
- `plot_channel_contributions(contributions)`: Plots the contributions of each channel over time.
- `plot_roi(roi)`: Plots the return on investment over time.
- `plot_roi_distribution(distribution)`: Plots the distribution of the return on investment.
- `plot_posterior_predictions(predictions)`: Plots the posterior predictions of the model.
- `_process_decomposition_components(components)`: Processes the decomposition components for plotting.
- `plot_waterfall_components_decomposition(decomposition)`: Plots a waterfall chart of the components' decomposition.
- `plot_correlation_matrix(matrix)`: Plots a correlation matrix of the input features.
- `plot_all_media_spend(spend)`: Plots the spend for all media channels over time.
- `plot_model_structure(structure)`: Visualizes the structure of the PyMC model.
- `plot_model_trace(trace)`: Plots the trace of the PyMC model.
- `weekly_spend_by_channel(channel)`: Plots the weekly spend by channel.

## Data Validation

These functions are used to validate the input data before fitting the model.

- `validation_method_y(y)`: Validates the target data.
- `validation_method_X(X)`: Validates the feature data.
- `validate_target(target)`: Validates the target column.
- `validate_date_col(date_col)`: Validates the date column.
- `validate_channel_columns(channels)`: Validates the media channel columns.
- `validate_control_columns(controls)`: Validates the control variable columns.

## Model Configuration

These functions are used to configure and parse the model configuration.

- `parse_model_config(config)`: Parses the model configuration.
- `handle_prior_config(prior_config)`: Handles the prior configuration.
- `handle_hggp_kwargs(kwargs)`: Handles the Hierarchical Gaussian Process (HGP) keyword arguments.

## Data Transformation

These functions are used to transform the input data for model fitting.

- `_copy_metric_values_to_media_data(data)`: Copies metric values to media data.
- `_copy_cost_values_to_media_costs(costs)`: Copies cost values to media costs.
- `transform_input_generic(input)`: Transforms generic input data.

## Model Description

These functions are used to describe the model and its results.

- `get_baseline_breakdown_df(breakdown)`: Gets a DataFrame of the baseline breakdown.
- `_dump_baseline_breakdown(breakdown)`: Dumps the baseline breakdown.
- `compute_roi_summary(summary)`: Computes a summary of the return on investment.
- `compute_cost_per_target_summary(summary)`: Computes a summary of the cost per target.
- `describe_mmm_training(training)`: Describes the MMM training process.
- `describe_mmm_prediction(prediction)`: Describes the MMM prediction process.
- `describe_input_data(data)`: Describes the input data.
- `describe_config(config)`: Describes the model configuration.
- `get_media_effect_df(effect)`: Gets a DataFrame of the media effect.
- `get_roi_df(roi)`: Gets a DataFrame of the return on investment.
- `_dump_posterior_metrics(metrics)`: Dumps the posterior metrics.
- `describe_all_media_spend(spend)`: Describes all media spend.
- `quick_stats(stats)`: Provides quick statistics of the model and its results.

## Transformers

These classes and functions are used to apply transformations to the data for model fitting.

### Classes:

- `ConvMode`: Defines the convolution mode for adstock transformation.
- `WeibullType`: Defines the type of Weibull distribution for adstock transformation.
- `TanhSaturationParameters`: Defines the parameters for Tanh saturation transformation.
- `TanhSaturationBaselinedParameters`: Defines the parameters for Tanh saturation with baseline transformation.

### Functions:

- `batched_convolution(signal, kernel)`: Applies batched convolution to a signal with a given kernel.
- `geometric_adstock(x, rate)`: Applies geometric adstock transformation.
- `delayed_adstock(x, delay, rate)`: Applies delayed adstock transformation.
- `weibull_adstock(x, shape, scale)`: Applies Weibull adstock transformation.
- `logistic_saturation(x, max, midpoint, rate)`: Applies logistic saturation transformation.
- `inverse_scaled_logistic_saturation(x, max, midpoint, rate)`: Applies inverse scaled logistic saturation transformation.
- `tanh_saturation(x, max, midpoint, scale)`: Applies Tanh saturation transformation.
- `tanh_saturation_baselined(x, max, midpoint, scale, baseline)`: Applies Tanh saturation with baseline transformation.
- `michaelis_menten(x, max, michaelis_constant)`: Applies Michaelis-Menten saturation transformation.
- `hill_saturation(x, max, hill_coefficient, half_maximal_concentration)`: Applies Hill saturation transformation.
- `root_saturation(x, max, root)`: Applies root saturation transformation.
- `baseline(x, params)`: Applies baseline transformation.
- `debaseline(x, params)`: Removes baseline transformation.
- `rebaseline(x, params)`: Reapplies baseline transformation.

## Outlier Handling

These functions are used to handle outliers in the input data.

- `print_outliers(outliers)`: Prints the outliers in the data.
- `_compute_outlier_replacement_value(value)`: Computes the replacement value for an outlier.
- `_replace_outlier_editor_func(func)`: Replaces the outlier editor function.
- `remove_outliers_from_input(input)`: Removes outliers from the input data.

## Model

These classes and functions are used to define and fit the MMM model.

### Classes:

- `BaseDelayedSaturatedMMM`: Base class for Delayed Saturated MMM models.
- `DelayedSaturatedMMM`: Class for Delayed Saturated MMM models.

### Functions:

- `__init__(self, config)`: Initializes the model with configuration.
- `default_sampler_config(self)`: Provides default sampler configuration.
- `output_var(self, var)`: Outputs a variable from the model.
- `build_model(self, data)`: Builds the PyMC model based on configuration and data.
- `load(self, path)`: Loads a saved model from a file path.
- `fit(self, data)`: Fits the model to the provided data.
- `predict(self, data)`: Generates predictions on new data.
- `sample_prior_predictive(self, samples)`: Samples from the prior predictive distribution.
- `sample_posterior_predictive(self, samples)`: Samples from the posterior predictive distribution.
- `get_params(self)`: Gets the model parameters.
- `set_params(self, params)`: Sets the model parameters.

## Model Configuration Parsing

These functions are used to parse and handle the model configuration.

- `parse_model_config(config)`: Parses the model configuration.
- `handle_prior_config(prior_config)`: Handles the prior configuration.
- `handle_hggp_kwargs(kwargs)`: Handles the Hierarchical Gaussian Process (HGP) keyword arguments.

## Data Storage

These functions are used to store and retrieve models and results.

- `generate_unique_date_key()`: Generates a unique key based on the current date and time.
- `make_results_dir(dir)`: Creates a directory for storing results.
- `create_output_folder(folder)`: Creates an output folder for storing results.
- `get_folder_creation_time(folder)`: Gets the creation time of a folder.

## Model Saturation

These classes are used to define different types of saturation transformations.

### Classes:

- `SaturationTransformation`: Base class for saturation transformations.
- `LogisticSaturation`: Class for logistic saturation transformation.
- `InverseScaledLogisticSaturation`: Class for inverse scaled logistic saturation transformation.
- `TanhSaturation`: Class for Tanh saturation transformation.
- `TanhSaturationBaselined`: Class for Tanh saturation with baseline transformation.
- `MichaelisMentenSaturation`: Class for Michaelis-Menten saturation transformation.
- `HillSaturation`: Class for Hill saturation transformation.
- `RootSaturation`: Class for root saturation transformation.

## Time-related Functions

These functions are used to handle time-related aspects of the model and data.

- `set_holidays(holidays)`: Sets the holidays for the model.
- `prophet_decomp(components)`: Decomposes the components of the model using Facebook's Prophet model.
- `update_config_with_prophet_components(config, components)`: Updates the model configuration with the components from the Prophet decomposition.

## Data Input and Transformation

These classes and functions are used to handle input data and apply transformations.

### Classes:

- `InputData`: Class for encapsulating and validating input data.
- `DataToFit`: Class for transforming input data to fit the model.
- `SerializableScaler`: Class for applying scaling transformations that can be serialized.

### Functions:

- `_validate(data)`: Validates the input data.
- `clone_with_data_edits(data, edits)`: Clones the input data and applies edits.
- `dump(data, path)`: Dumps the input data to a file.
- `clone_and_add_extra_features(data, features)`: Clones the input data and adds extra features.
- `clone_as_weekly(data)`: Clones the input data and resamples it to a weekly frequency.
- `clone_and_log_transform_target_data(data)`: Clones the input data and applies a log transformation to the target data.
- `clone_and_split_media_data(data, split)`: Clones the input data and splits the media data.

## Model Base Classes

These classes are used as base classes for defining MMM models.

### Classes:

- `BaseMMM`: Base class for MMM models.
- `MMM`: Class for MMM models.

### Functions:

- `__init__(self, config)`: Initializes the model with configuration.
- `methods(self)`: Returns the methods of the model.
- `validation_methods(self)`: Returns the validation methods of the model.
- `validate(self, data)`: Validates the input data.
- `preprocessing_methods(self)`: Returns the preprocessing methods of the model.
- `preprocess(self, data)`: Preprocesses the input data.
- `get_target_transformer(self)`: Gets the transformer for the target variable.
- `prior(self, prior)`: Sets the prior for the model.
- `prior_predictive(self, predictive)`: Sets the prior predictive for the model.
- `fit_result(self, result)`: Sets the fit result for the model.
- `posterior_predictive(self, predictive)`: Sets the posterior predictive for the model.
- `plot_prior_predictive(self)`: Plots the prior predictive of the model.
- `plot_posterior_predictive(self)`: Plots the posterior predictive of the model.
- `_format_model_contributions(self, contributions)`: Formats the model contributions.
- `plot_components_contributions(self)`: Plots the component contributions of the model.
- `plot_channel_parameter(self, parameter)`: Plots a channel parameter of the model.
- `compute_channel_contribution_original_scale(self, scale)`: Computes the channel contribution on the original scale.
- `_estimate_budget_contribution_fit(self, fit)`: Estimates the budget contribution fit of the model.
- `_plot_scenario(self, scenario)`: Plots a scenario of the model.
- `plot_budget_scenarios(self, scenarios)`: Plots budget scenarios of the model.
- `_plot_response_curve_fit(self, fit)`: Plots the response curve fit of the model.
- `optimize_channel_budget_for_maximum_contribution(self, contribution)`: Optimizes the channel budget for maximum contribution.
- `compute_channel_curve_optimization_parameters_original_scale(self, scale)`: Computes the channel curve optimization parameters on the original scale.
- `plot_direct_contribution_curves(self, curves)`: Plots the direct contribution curves of the model.
- `_get_distribution(self, distribution)`: Gets a distribution of the model.
- `compute_mean_contributions_over_time(self, time)`: Computes the mean contributions over time.
- `plot_grouped_contribution_breakdown_over_time(self, time)`: Plots the grouped contribution breakdown over time.
- `_get_channel_contributions_share_samples(self, samples)`: Gets the channel contributions share samples.
- `plot_channel_contribution_share_hdi(self, hdi)`: Plots the channel contribution share highest density interval.
- `plot_channel_contribution_stats(self, stats)`: Plots the channel contribution statistics.
- `graphviz(self)`: Visualizes the model using Graphviz.
- `_process_decomposition_components(self, components)`: Processes the decomposition components for plotting.
- `plot_waterfall_components_decomposition(self, decomposition)`: Plots a waterfall chart of the components' decomposition.
