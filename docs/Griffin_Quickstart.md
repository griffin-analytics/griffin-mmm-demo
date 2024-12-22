<p align="center">
  <img src="https://github.com/griffin-analytics/griffin-mmm-demo/raw/main/images/logo.png" alt="Griffin Logo">
</p>

----

# Griffin MMM Quickstart Guide

## Welcome to Griffin MMM

Griffin MMM simplifies complex Media Mix Modeling, empowering marketers with actionable insights and data-driven decision-making tools. Whether you’re analysing ROI or optimising your marketing mix, Griffin MMM provides an intuitive and powerful platform.

### Why Choose Griffin MMM?
- **Accurate Analytics**: Advanced statistical models to evaluate channel effectiveness.
- **Scalable**: Works for both small agencies and large organisations.
- **User-Friendly**: Accessible via Jupyter notebooks, no complex installation required.
- **Cross-Channel Insights**: Optimise spend allocation with a clear understanding of channel interactions.
- **Customisation**: Tailor models to fit your unique business needs.

---

## Getting Started

This section will guide you through the process of accessing and setting up Griffin MMM, whether you are using the free demo version or the Pro version.

### Step-by-Step Guide

1. **Access the Notebook**: Navigate to the demo folder on GitHub.
2. **Launch in Colab**: Open the notebook in Google Colab or any Jupyter-compatible platform.
3. **Configure Your Model**: Define your settings in a `config.yaml` file (see the Configuration Guide for details).
4. **Upload Your Data**: Provide a CSV file containing your marketing data.
5. **Run the Notebook**: Execute cells sequentially to complete your Media Mix Modeling workflow.

**Note for Pro Users**: Your Pro access key will be required to unlock advanced features within the notebook. Enter it when prompted.

---

## Demo vs Pro Comparison

| Feature               | Demo Version       | Pro Version        |
|-----------------------|--------------------|--------------------|
| Media Channels        | Up to 4           | Unlimited          |
| Support               | Community         | Priority Support   |
| Advanced Features     | Basic             | Full Access        |
| Visualisations        | Standard          | Advanced           |
| Strategy Consultation | Not Included      | Quarterly          |
| Software Updates      | Limited           | Regular Updates    |

### Demo Version
The free demo version is ideal for exploring Griffin MMM’s capabilities. It includes:
- Unlimited access to the notebook
- Support for up to 4 media channels
- Basic visualisations and analysis tools

### Pro Version
The Pro version unlocks the full potential of Griffin MMM with:
- Support for unlimited media channels
- Advanced analytics and visualisations
- Priority email support
- Quarterly strategy consultations
- Regular updates with the latest features

---

## Example Workflow

Here is an example of how you can use Griffin MMM:

1. **Prepare Your Data**: Format your CSV file to include required columns (e.g., `date`, `target`, `media spend`).

2. **Define Your Configuration**: Create a `config.yaml` file. Example:
   ```yaml
   raw_data_granularity: weekly
   target_col: "conversions"
   media:
     - display_name: "Social Media"
       impressions_col: social_impressions
       spend_col: social_cost
   ```

3. **Run the Notebook**: Follow the instructions in the notebook to load your data, configure the model, and execute the analysis.

4. **Interpret Results**: Use the visualisations and metrics generated to gain insights into your marketing performance.

---

## Key Features

- **Interactive Visualisations**: Easily interpret channel contributions, ROI, and response curves.
- **Bayesian Framework**: Robust uncertainty quantification for confident decision-making.
- **Custom Priors**: Leverage domain expertise to refine model accuracy.

---

## Support and Troubleshooting

### Community Support
- Post your questions and issues on our GitHub repository.

### Pro Support
- Email us at support@griffin-analytics.com for priority assistance.

### Common Issues
- **Data Format Errors**: Ensure your date column follows the `YYYY-MM-DD` format.
- **Configuration Mismatches**: Verify that column names in `config.yaml` match your dataset exactly.
- **Pro Key Issues**: Contact support if you experience problems unlocking advanced features.

---

Griffin MMM is designed to help you optimise your marketing efforts with powerful and flexible tools. Start your journey today and unlock the full potential of your marketing mix!

