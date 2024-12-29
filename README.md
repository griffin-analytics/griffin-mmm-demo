# Griffin MMM: Advanced Media Mix Modelling Workbench

<p align="center">
  <img src="images/logo.png" alt="Griffin Logo">
</p>

---

## Unlock the Potential of Bayesian Media Mix Modelling

Griffin MMM is a cutting-edge, production-ready solution designed to empower small marketing agencies and data-savvy marketers. Built on an enhanced PyMC framework, Griffin MMM delivers unparalleled insights into your marketing strategy, enabling you to:

- **Accurately Measure ROI**: Gain a clear understanding of channel performance with robust Bayesian inference.
- **Optimize Budget Allocation**: Leverage advanced algorithms to maximize marketing effectiveness.
- **Drive Confident Decisions**: Benefit from interpretable and reliable insights, even with limited data.

**Contact us today for a personal walkthrough:** info@griffin-analytics.com

---
## Quick Start Guide

### 1. Open the Demo Notebook
Once your data is ready, navigate to the /demo folder, and open the demo notebook in Google Colab (look for the .ipynb file).

### 2. Configure and Run
* Install dependencies with one click in the Colab environment.
* Use the preloaded sample data and demo configuration files (config.yaml) or load your own.
* Explore features such as budget optimization, channel contribution analysis, and predictive insights.

### 3. Visualize and Interpret
* Review results to make data-driven decisions.
* (Optional) Use PowerBI or similar for further visualisations as needed.

Need help? Contact us or raise a GitHub issue.

---

## Why Choose Griffin MMM?

Griffin MMM empowers marketing agencies with advanced capabilities to optimize their marketing strategies:

1. **Accurate and Reliable Insights**: Built on a Bayesian framework, Griffin MMM delivers stable and interpretable results, even when working with sparse or incomplete datasets. This ensures confidence in the outcomes and supports data-driven decision-making.

2. **Seamless Ease of Use**: Fully integrated with Google Colab, Griffin MMM offers a hassle-free setup process that eliminates the need for extensive coding expertise. Its intuitive design ensures that users can quickly get started and focus on insights rather than technical challenges.

3. **Tailored for Agencies**: Designed with small to medium agencies in mind, Griffin MMM is production-ready and requires minimal configuration compared to other tools like PyMC-Marketing. Its sound statistical framework ensures replicable, stable, and interpretable results, making it an ideal choice for agencies looking to deliver reliable outcomes to their clients.

4. **A Step Beyond Open-Source Solutions**: Unlike open-source alternatives like Meta's Robyn, Griffin MMM provides a more robust and statistically rigorous approach. With Griffin, users benefit from enhanced stability, greater interpretability, and a production-ready tool that is better suited to real-world applications.

---

## Demo vs Pro Comparison

| Feature                     | Demo Version                 | Pro Version                  |
|-----------------------------|------------------------------|------------------------------|
| **Price**                   | Free                         | Annual subscription          |
| **Media Channels**          | 4                            | Unlimited                    |
| **Features**                | Full access                  | Advanced tools and insights  |
| **Support**                 | Community (GitHub issues, email) | Priority                     |

---
## User Instructions for Key Files

### `budget_optimizer.py`
This module contains Griffin MMM's budget optimization code, providing essential functions to optimize marketing spend allocation across multiple channels. It enables users to:

- Calculate expected contributions for each channel using advanced models such as the Michaelis-Menten and Sigmoid response functions.
- Optimize budget distribution to maximize overall marketing impact while respecting budget constraints.
- Perform scenario analysis to compare the current spending pattern with optimized allocations, empowering data-driven decision-making.

To use this file:
1. Download `budget_optimizer.py` from the repository.
2. Place it in the same directory level as the `sample_data` folder for seamless integration with Griffin MMM.

### `demo_utils.py`

The `demo_utils.py` file provides an interactive configuration widget that simplifies the process of setting up your `config.yaml` file for Griffin MMM. This widget allows users to edit and preview their model configuration in real-time, making it easier to customize and validate the setup.

#### Key Features:
- **Live YAML Preview**: Changes made in the widget are instantly reflected in the YAML configuration file, ensuring transparency and reducing errors.
- **Editable Model Options**: Modify essential parameters such as `Model Name`, `Date Range`, `Data Granularity`, and `Train/Test Ratio`.
- **Column Management**: Add, remove, or rename input columns, including `Date Column`, `Target Column`, and `Extra Features`.
- **Media Channel Definitions**: Easily define `spend_col` and `impressions_col` for each media channel.
- **Custom Parameters**: Adjust model parameters like seasonal effects and trend components.

#### How to Use:
1. Download `demo_utils.py` from the repository.
2. Place it in the same directory as your notebook.
3. Import the file and display the widget by adding the following code snippet to your notebook:
   ```python
   from demo_utils import config_widget
   display(config_widget)
   ```
4. Use the interactive interface to configure your model. The left panel allows for value editing, while the right panel provides a live preview of the corresponding YAML configuration file.

This tool significantly streamlines the model configuration process, making it accessible even for users with minimal technical expertise.

Both files are designed to enhance your experience with Griffin MMM by streamlining critical setup and optimization workflows. Be sure to explore their functionality and integrate them into your workflow for maximum efficiency.

---

## Beta Release Notice

Griffin MMM is currently in beta until **31 March 2025**. During this beta period, we are offering early access at a special rate. By joining now, you will:

- Lock in a discounted rate before the official release.
- Gain the opportunity to provide feedback and shape the future of Griffin MMM.
- Access a stable, rigourously tested solution with cutting-edge features.

---

## How to Get Started

### Demo Version:
1. Clone this repository to access the demo.
2. Follow the Quick Start Guide above to run the demo in Colab.
3. Use the demo version for as long as you need – no registration required.

### Pro Version:
1. Contact us at info@griffin-analytics.com to discuss your needs.
2. Receive an invoice for the annual subscription fee.
3. Upon payment, gain access to the Pro version, featuring:
   - Unlimited channel analysis.
   - Priority support and advanced tools.

---

## Documentation and Support

### Documentation
For detailed setup instructions, API references, and advanced use cases, please refer to the full documentation included in this repository.

### Support
- **Issues**: Raise any questions or problems on [GitHub](https://github.com/griffin-analytics/issues).
- **Email**: Contact us directly at info@griffin-analytics.com.

---

## License

Griffin MMM is governed by our **End-User License Agreement (EULA)**.

- **Demo Version**: Licensed for internal evaluation and analysis of up to 4 media channels.
- **Pro Version**: Licensed for full feature access, subject to the terms of the EULA.

Please review the EULA before using Griffin MMM, see the LEGAL folder (https://github.com/griffin-analytics/griffin-mmm-demo/tree/main/LEGAL)

