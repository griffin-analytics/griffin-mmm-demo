## Dictionary  

The config.yaml file contains all the configuration settings that are needed to deploy your model:
* `config.yaml`: the config provided when running MMM.
  
After running the Media Mix Model, the following files are generated in the results directory:

## Configuration and Summary Files

* `model_config.json`: JSON file containing the configuration settings used for the model.
* `model_summary.csv`: CSV file providing a summary of the model's performance and key metrics.
* `output.txt`: Text file with general output information from the model run.

## Performance Metrics

* `all_decomp.csv`: CSV file with a comprehensive decomposition of all factors contributing to the model.
* `media_performance_cost_per_target.csv`: CSV file detailing the cost per target for each media channel.
* `media_performance_effect.csv`: CSV file showing the effect of each media channel.
* `media_performance_roi.csv`: CSV file with Return on Investment (ROI) metrics for each media channel.

## Visualizations

### Channel Performance

* `budget_optimisation.png`: Visual representation of budget optimization results.
* `channel_contribution_as_function_of_cost_share.png`: Graph showing how channel contribution relates to cost share.
* `components_contributions.png`: Visualization of the contributions of different components in the model.
* `media_contribution_mean.png`: Graph of mean media contribution by channel.
* `media_contribution_median.png`: Graph of median media contribution by channel.
* `media_contribution_share.png`: Pie chart or similar showing the share of contribution for each media channel.
* `media_roi_mean.png`: Graph of mean ROI by media channel.
* `media_roi_median.png`: Graph of median ROI by media channel.
* `roi_distribution.png`: Distribution plot of ROI across channels.

### Model Fit and Predictions

* `model_fit_in_sample.png`: Visualization of the model's fit to the training data.
* `model_fit_predictions.png`: Graph showing the model's predictions compared to actual data.
* `model_priors_and_posteriors.png`: Visualization of the model's prior and posterior distributions.

### Response Curves and Decomposition

* `response_curves.png`: Graph showing response curves for different channels or variables.
* `waterfall_plot_components_decomposition.png`: Waterfall plot breaking down the components of the model.

### Time Series Analysis

* `weekly_media_and_baseline_contribution.png`: Time series plot of media and baseline contributions on a weekly basis.
* `weekly_media_contribution.png`: Time series plot focusing on weekly media contributions.
