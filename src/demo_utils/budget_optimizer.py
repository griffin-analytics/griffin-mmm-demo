"""Budget optimization module."""
from typing import Dict, List, Optional, Tuple

import mmm.utils as ut
import scipy.optimize as sopt
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('bmh')


def calculate_expected_contribution(
    method: str,
    parameters: Dict[str, Tuple[float, float]],
    budget: Dict[str, float],
) -> Dict[str, float]:
    """
    Calculate expected contributions using the specified model.

    This function calculates the expected contributions for each channel
    based on the chosen model. The selected model can be either the Michaelis-Menten
    model or the sigmoid model, each described by specific parameters.
    As the allocated budget varies, the expected contribution is computed according
    to the chosen model.

    Parameters
    ----------
    method : str
        The model to use for contribution estimation. Choose from 'michaelis-menten' or 'sigmoid'.
    parameters : Dict
        Model-specific parameters for each channel. For 'michaelis-menten', each entry is a tuple (L, k) where:
        - L is the maximum potential contribution.
        - k is the budget at which the contribution is half of its maximum.

        For 'sigmoid', each entry is a tuple (alpha, lam) where:
        - alpha controls the slope of the curve.
        - lam is the budget at which the curve transitions.
    budget : Dict
        The total budget.

    Returns
    -------
    Dict
        A dictionary with channels as keys and their respective contributions as values.
        The key 'total' contains the total expected contribution across all channels.

    Raises
    ------
    ValueError
        If the specified `method` is not recognized.
    """

    total_expected_contribution = 0.0
    contributions = {}

    for channel, channe_budget in budget.items():
        if method == "michaelis-menten":
            L, k = parameters[channel]
            contributions[channel] = ut.michaelis_menten(channe_budget, L, k)

        elif method == "sigmoid":
            alpha, lam = parameters[channel]
            contributions[channel] = ut.sigmoid_saturation(channe_budget, alpha, lam)

        else:
            raise ValueError("`method` must be either 'michaelis-menten' or 'sigmoid'.")

        total_expected_contribution += contributions[channel]

    contributions["total"] = total_expected_contribution

    return contributions


def objective_distribution(
    x: List[float],
    method: str,
    channels: List[str],
    parameters: Dict[str, Tuple[float, float]],
) -> float:
    """
    Compute the total contribution for a given budget distribution.

    This function calculates the negative sum of contributions for a proposed budget
    distribution using the Michaelis-Menten model. This value will be minimized in
    the optimization process to maximize the total expected contribution.

    Parameters
    ----------
    x : List of float
        The proposed budget distribution across channels.
    channels : List of str
        The List of channels for which the budget is being optimized.
    parameters : Dict
        Michaelis-Menten parameters for each channel as described in `calculate_expected_contribution`.

    Returns
    -------
    float
        Negative of the total expected contribution for the given budget distribution.
    """

    sum_contributions = 0.0

    for channel, budget in zip(channels, x):
        if method == "michaelis-menten":
            L, k = parameters[channel]
            sum_contributions += ut.michaelis_menten(budget, L, k)

        elif method == "sigmoid":
            alpha, lam = parameters[channel]
            sum_contributions += ut.sigmoid_saturation(budget, alpha, lam)

        else:
            raise ValueError("`method` must be either 'michaelis-menten' or 'sigmoid'.")

    return -1 * sum_contributions


def optimize_budget_distribution(
    method: str,
    total_budget: int,
    budget_ranges: Optional[Dict[str, Tuple[float, float]]],
    parameters: Dict[str, Tuple[float, float]],
    channels: List[str],
) -> Dict[str, float]:
    """
    Optimize the budget allocation across channels to maximize total contribution.

    Using the Michaelis-Menten or Sigmoid function, this function seeks the best budget distribution across
    channels that maximizes the total expected contribution.

    This function leverages the Sequential Least Squares Quadratic Programming (SLSQP) optimization
    algorithm to find the best budget distribution across channels that maximizes the total
    expected contribution based on the Michaelis-Menten or Sigmoid functions.

    The optimization is constrained such that:
    1. The sum of budgets across all channels equals the total available budget.
    2. The budget allocated to each individual channel lies within its specified range.

    The SLSQP method is particularly suited for this kind of problem as it can handle
    both equality and inequality constraints.

    Parameters
    ----------
    total_budget : int
        The total budget to be distributed across channels.
    budget_ranges : Dict or None
        An optional dictionary defining the minimum and maximum budget for each channel.
        If not provided, the budget for each channel is constrained between 0 and its L value.
    parameters : Dict
        Michaelis-Menten parameters for each channel as described in `calculate_expected_contribution`.
    channels : list of str
        The list of channels for which the budget is being optimized.

    Returns
    -------
    Dict
        A dictionary with channels as keys and the optimal budget for each channel as values.
    """

    # Check if budget_ranges is the correct type
    if not isinstance(budget_ranges, (dict, type(None))):
        raise TypeError("`budget_ranges` should be a dictionary or None.")

    if budget_ranges is None:
        budget_ranges = {
            channel: (0, min(total_budget, parameters[channel][0]))
            for channel in channels
        }

    initial_guess = [total_budget // len(channels)] * len(channels)

    bounds = [budget_ranges[channel] for channel in channels]

    constraints = {"type": "eq", "fun": lambda x: np.sum(x) - total_budget}

    result = sopt.minimize(
        lambda x: objective_distribution(x, method, channels, parameters),
        initial_guess,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints,
    )

    return {channel: budget for channel, budget in zip(channels, result.x)}


def budget_allocator(
    method: str,
    total_budget: int,
    channels: List[str],
    parameters: Dict[str, Tuple[float, float]],
    budget_ranges: Optional[Dict[str, Tuple[float, float]]],
) -> pd.DataFrame:
    """
    Allocate the optimal marketing budget across multiple channels based on specified optimization criteria.

    This function determines the best way to distribute a given total marketing budget across different channels
    to maximize the expected contribution to a desired outcome, such as conversions or revenue. The allocation is
    guided by a chosen optimization method (e.g., sigmoid, linear), and considers parameters that describe the
    relationship between spend and contribution for each channel. The function also respects any predefined budget
    ranges for each channel, ensuring that the allocation stays within practical limits.

    ### Key Components:
    1. **Optimization Method:**
       - The `method` parameter specifies the mathematical approach used to optimize the budget allocation.
       - Common methods include sigmoid or linear models, which define how spending impacts contribution across channels.

    2. **Budget Constraints:**
       - `total_budget` sets the overall limit for how much can be allocated across all channels.
       - `budget_ranges` optionally allows setting specific minimum and maximum bounds for individual channels, ensuring
         that the budget distribution adheres to strategic constraints or real-world limitations.

    3. **Channel Parameters:**
       - The `parameters` dictionary contains key-value pairs where each key is a channel name, and each value is a tuple
         representing the parameters (e.g., alpha, lambda for sigmoid) that define the spend-contribution curve for that channel.
       - These parameters are essential for calculating how efficiently each dollar spent on a channel converts into the desired outcome.

    4. **Output:**
       - The function returns a DataFrame that includes both the `optimal_budget` allocation for each channel and the
         `estimated_contribution` resulting from this allocation.
       - This output enables data-driven decision-making, allowing marketers to see the expected returns for each channel
         and adjust their strategies accordingly.

    ### Parameters:
    - `method` (str):
        - The optimization method to be used (e.g., 'sigmoid', 'linear').
        - This method dictates how the relationship between spend and contribution is modeled.
    - `total_budget` (int):
        - The total budget available for allocation across all channels.
        - This budget is distributed among the channels in a way that maximizes the overall contribution.
    - `channels` (List[str]):
        - A list of channel names that represent the marketing channels available for budget allocation.
        - Each channel in this list should have corresponding parameters defined in the `parameters` dictionary.
    - `parameters` (Dict[str, Tuple[float, float]]):
        - A dictionary where each key is a channel name and each value is a tuple representing the parameters for
          that channel’s spend-contribution curve.
        - These parameters guide the optimization process by defining how effective each dollar of spend is on a given channel.
    - `budget_ranges` (Optional[Dict[str, Tuple[float, float]]]):
        - An optional dictionary where each key is a channel name and each value is a tuple specifying the minimum and
          maximum budget that can be allocated to that channel.
        - If provided, these ranges ensure the budget allocation stays within practical or strategic limits.
    """

    optimal_budget = optimize_budget_distribution(
        method=method,
        total_budget=total_budget,
        budget_ranges=budget_ranges,
        parameters=parameters,
        channels=channels,
    )

    expected_contribution = calculate_expected_contribution(
        method=method, parameters=parameters, budget=optimal_budget
    )

    optimal_budget.update({"total": sum(optimal_budget.values())})

    return pd.DataFrame(
        {
            "estimated_contribution": expected_contribution,
            "optimal_budget": optimal_budget,
        }
    )

def get_lower_and_upper_bounds(media, n_time_periods, lower_pct, upper_pct):
    """
    Calculate dynamic lower and upper bounds for media spend based on historical data and specified adjustment percentages.

    This function determines the permissible range (lower and upper bounds) for future media spending by analyzing historical
    spending patterns. The bounds are calculated as a percentage adjustment from the mean historical spend, providing a flexible
    framework for budgeting that accounts for possible variations in spend while ensuring it stays within realistic limits.

    ### Key Components:
    1. **Historical Media Spend Analysis:**
       - The function begins by calculating the mean spend for each media channel over the historical period provided.
       - This mean serves as the baseline for determining future spend bounds, ensuring that projections are grounded in actual
         historical performance.

    2. **Dynamic Bound Adjustment:**
       - The lower and upper bounds are calculated by applying the `lower_pct` and `upper_pct` adjustments to the mean spend.
       - `lower_pct` defines the percentage by which the spend can decrease from the mean, while `upper_pct` defines the
         percentage by which it can increase.
       - The bounds are scaled by the number of time periods (`n_time_periods`) to reflect the cumulative effect over the
         optimization horizon.

    3. **Constraints and Flexibility:**
       - The lower bounds are capped at zero to prevent negative spend values, ensuring practical and realistic budget constraints.
       - The resulting bounds provide flexibility in budget allocation, allowing for increased spending in high-performing
         channels while capping potential overspend in others.

    ### Parameters:
    - `media` (pd.DataFrame):
        - A DataFrame containing historical spending data for each media channel.
        - Each column corresponds to a media channel, and each row represents a historical time period.
    - `n_time_periods` (int):
        - The number of future periods (e.g., weeks, months) for which the bounds should be calculated.
        - This parameter scales the bounds to ensure they are applicable over the entire projection horizon.
    - `lower_pct` (np.ndarray):
        - An array of percentage values representing the allowable decrease from the mean spend for each media channel.
        - Each value corresponds to a specific media channel and defines the lower bound as a percentage below the mean.
    - `upper_pct` (np.ndarray):
        - An array of percentage values representing the allowable increase from the mean spend for each media channel.
        - Each value defines the upper bound as a percentage above the mean for its respective channel.

    ### Returns:
    - `Tuple[np.ndarray, np.ndarray]`:
        - A tuple containing two numpy arrays: `lower_bounds` and `upper_bounds`.
        - `lower_bounds` represents the calculated lower bounds for each media channel, scaled by `n_time_periods`.
        - `upper_bounds` represents the calculated upper bounds for each media channel, also scaled by `n_time_periods`.

    """
    mean_data = media.mean(axis=0)
    lower_bounds = np.maximum(mean_data * (1 - lower_pct), 0)
    upper_bounds = mean_data * (1 + upper_pct)

    return (lower_bounds * n_time_periods, upper_bounds * n_time_periods)

def calculate_total_budget(mean_costs, n_time_periods):
    """
    Calculate the total marketing budget required for a specified number of future time periods.

    This function computes the total budget necessary to sustain marketing activities across various channels over a defined
    number of time periods (e.g., months, quarters). The budget is calculated based on the average historical spending for
    each media channel, scaled by the number of time periods for which the budget needs to be projected.

    Key Considerations:
    1. **Mean Media Costs:**
       - The `mean_costs` parameter represents the average historical spending per time period for each media channel.
       - This array typically reflects the mean of past expenditures, providing a baseline for projecting future budget needs.

    2. **Time Period Scaling:**
       - The `n_time_periods` parameter determines how many future periods the total budget should cover.
       - By multiplying the sum of the mean costs by the number of periods, the function scales the budget to ensure it supports
         sustained marketing efforts over the desired time horizon.

    3. **Budget Allocation Assumptions:**
       - The calculated budget assumes a consistent spending pattern across the future periods, based on the historical averages.
       - This approach is useful for planning purposes, especially when forecasting the financial requirements for maintaining
         or scaling marketing activities over time.

    ### Parameters:
    - `mean_costs` (np.ndarray):
        - An array containing the average historical costs for each media channel.
        - Each element in the array corresponds to a specific channel and represents the mean cost over past time periods.
    - `n_time_periods` (int):
        - The number of future time periods for which the total budget is being calculated.
        - This could be any unit of time, such as months or quarters, depending on the context of the optimization.

    ### Returns:
    - `float`:
        - The total budget required to cover the specified number of time periods, calculated as the sum of mean costs
          across all media channels, scaled by `n_time_periods`.
        - This scalar value represents the overall financial commitment needed to sustain the marketing strategy over
          the defined future periods.
    """
    return np.sum(mean_costs) * n_time_periods


def optimize_marketing_budget(model, data, config, results_dir,total_budget=None, frequency='M', n_time_periods=1):
    """
    Optimize the allocation of a marketing budget across various channels using a fitted marketing mix model and historical data.

    This function performs budget optimization by leveraging a calibrated marketing mix model to maximize the expected contribution
    to the overall marketing objective (e.g., sales, conversions) given a specified total budget. The process involves aggregating
    historical spending data at a chosen frequency (e.g., monthly, quarterly), defining dynamic budget bounds based on historical
    spending patterns, and optimizing budget allocations using a non-linear optimization approach.

    Key Steps:
    1. **Data Aggregation:**
       - Historical media spending data is aggregated according to the specified time frequency (e.g., 'M' for monthly, 'Q' for quarterly).
       - This aggregation helps to smooth out fluctuations and focus on broader spending trends over time, which are more indicative
         of strategic budget adjustments.

    2. **Budget Bound Calculation:**
       - For each media channel, dynamic lower and upper bounds for spending are calculated based on historical spending patterns.
       - These bounds are defined as a percentage deviation from the historical averages, allowing the optimization to explore budget
         allocations within realistic limits while considering potential scaling up or down.

    3. **Sigmoid Function Optimization:**
       - The function utilizes a sigmoid response curve to model the diminishing returns on spending, which is a common phenomenon in
         marketing where additional spending leads to progressively smaller gains.
       - The sigmoid parameters for each channel are estimated using the fitted model, capturing the relationship between spending and
         the marketing objective.

    4. **Optimization Process:**
       - A constrained optimization algorithm is employed to maximize the expected contribution to the marketing objective under the
         given budget constraints.
       - The optimization considers both the total budget available and the channel-specific budget bounds, aiming to allocate the budget
         where it is expected to yield the highest return.

    5. **Scenario Analysis:**
       - The function compares the optimized budget allocation against the initial scenario (i.e., the historical spending pattern).
       - The comparison is visualized to highlight potential improvements in marketing performance due to the optimized allocation.

    6. **Result Visualization and Saving:**
       - The optimized budget scenario, along with the initial budget scenario, is plotted for easy comparison.
       - The visualization is saved as an image file in the specified directory for reporting and further analysis.

    Parameters
    ----------
    model : PyMC-Marketing model
        The already fitted marketing mix model that will be used to optimize the budget.

    data : pd.DataFrame
        A DataFrame containing historical spending data. It must include a 'date' column and columns corresponding
        to each media channel specified in the configuration.

    config : dict
        A dictionary containing configuration data for media channels. This should include the names of the columns
        in the data that correspond to media spending.

    results_dir : str
        The directory where the optimization results, including plots, will be saved.

    total_budget : float, optional
        The total marketing budget to be allocated across the channels. If not provided, it will be calculated based
        on the average historical spending and the number of periods to optimize.

    frequency : str, optional
        The frequency for aggregating the spending data. Typical values are 'M' for monthly, 'Q' for quarterly, and
        'W' for weekly. Defaults to 'M' (monthly).

    n_time_periods : int, optional
        The number of future time periods (based on the specified frequency) for which the budget is to be optimized.
        Defaults to 1.

    Returns
    -------
    None
        The function does not return any value. It saves a plot of the optimized budget scenario compared to the
        initial scenario in the specified results directory.

    Notes
    -----
    - The optimization is based on a sigmoid function fitted to each channel's response curve.
    - Budget bounds are dynamically calculated as a percentage increase or decrease from historical averages.
    - The resulting budget allocation is visualized and saved as a PNG file in the results directory.

    Example
    -------
    >>> optimize_marketing_budget(model, data, config, 'results/', total_budget=1.0, frequency='M', n_time_periods=3)
    """
    aggregated_data = data.groupby(pd.Grouper(key='date', freq=frequency)).sum()

    media_columns = [entry['spend_col'] for entry in config.get('media', [])]
    aggregated_media_data = aggregated_data[media_columns]
    # Calculate total budget if not provided
    if total_budget is None:
        mean_media_costs = aggregated_media_data.mean()
        total_budget = calculate_total_budget(mean_media_costs, n_time_periods)


    # Set percentage increases and decreases for bounds
    lower_pct = np.array([0.20] * len(media_columns))  # 20% decrease for lower bounds
    upper_pct = np.array([0.20] * len(media_columns))  # 20% increase for upper bounds


    # Calculate bounds directly from the aggregated media data
    lower_bounds, upper_bounds = get_lower_and_upper_bounds(
        aggregated_media_data, n_time_periods, lower_pct=lower_pct, upper_pct=upper_pct)

    # Convert bounds arrays into dictionaries for each media channel
    budget_bounds = {media_columns[i]: [lower_bounds[i], upper_bounds[i]] for i in range(len(media_columns))}

    # Compute parameters for the sigmoid function
    sigmoid_params = model.compute_channel_curve_optimization_parameters_original_scale(method='sigmoid')

    # Optimize the channel budget using sigmoid function parameters
    result_sigmoid = model.optimize_channel_budget_for_maximum_contribution(
        method='sigmoid',
        total_budget=total_budget,
        parameters=sigmoid_params,
        budget_bounds=budget_bounds
    )
    initial_budget_dict = {media_columns[i]: mean_media_costs[i] for i in range(len(media_columns))}


    # Calculate expected contribution based on the initial budget
    initial_contribution = calculate_expected_contribution(
        method='sigmoid',
        parameters=sigmoid_params,
        budget=initial_budget_dict
    )

    # Setup the initial scenario for comparison
    initial_scenario = {
        'initial_contribution': initial_contribution,
        'initial_budget': initial_budget_dict
    }

    # Plot and save the budget scenarios comparison
    figure_ = model.plot_budget_scenarios(base_data=initial_scenario, method='sigmoid', scenarios_data=[result_sigmoid])
    import os
    import matplotlib.pyplot as plt
    plt.savefig(os.path.join(results_dir, 'budget_optimisation.png'), bbox_inches="tight")
