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

### Step 1: Run the Demo in Google Colab

Griffin MMM is designed for a seamless experience in Google Colab. Here’s how to get started:

1. **Open the Demo Notebook in Colab**:
   (https://colab.research.google.com)

2. **Run the Setup Cell**:
   - Install required libraries with a single click.
   - Load the sample configuration and datasets included in the `/demo` folder.

3. **Explore Griffin MMM’s Features**:
   - Visualize key metrics, such as ROI and channel contributions.
   - Run advanced budget optimization scenarios.

4. **Need Help?** Raise an issue on [GitHub](https://github.com/griffin-analytics) or email us at info@griffin-analytics.com.

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
This utility file provides interactive widgets for configuring and generating the `config.yaml` file. It simplifies the process of setting up your model by allowing you to:

- Select and modify input columns for your dataset.
- Configure model parameters such as `tune`, `draws`, and `chains`.
- Define media channels and specify their spend and impressions columns.
- Set up seasonal and trend components using Prophet integration settings.

To use this file:
1. Download `demo_utils.py` from the repository.
2. Import the file in your Jupyter Notebook to create interactive widgets for your configuration tasks.

Both files are designed to enhance your experience with Griffin MMM by streamlining critical setup and optimization workflows. Be sure to explore their functionality and integrate them into your workflow for maximum efficiency.

---

## Why Choose Griffin MMM?

| Feature                     | Griffin MMM Highlights |
|-----------------------------|-------------------------|
| **Accurate Insights**       | Powered by Bayesian inference for stable and interpretable results. |
| **Seamless Integration**    | Merge and analyze data from multiple marketing channels effortlessly. |
| **Advanced Visualizations** | Transform complex data into clear, actionable insights. |
| **Customizable Models**     | Tailor models to your unique marketing ecosystem and goals. |

---

## Demo vs Pro Comparison

| Feature                     | Demo Version                 | Pro Version                  |
|-----------------------------|------------------------------|------------------------------|
| **Price**                   | Free                         | Annual subscription          |
| **Media Channels**          | 4                            | Unlimited                    |
| **Features**                | Full access                  | Advanced tools and insights  |
| **Support**                 | Community (GitHub issues, email) | Priority                     |

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

Please review the EULA before using Griffin MMM.

