![Logo](logo)

# Guide to Griffin MMM

## Introduction

### What is Griffin MMM?

Griffin MMM is a Media Mix Modeling solution designed to empower marketers with advanced analytics and intelligent insights. As part of an evolving suite of tools, Griffin MMM stands at the forefront of marketing technology, enabling users to optimize their strategies across various channels effectively.

At its core, Griffin MMM is a powerful analytical tool that helps navigate the complex marketing landscape. It provides a robust framework for analyzing the effectiveness of different marketing channels, allowing marketers to make data-driven decisions and maximize their return on investment (ROI).

### Key Features

Griffin MMM offers a range of features tailored to meet the needs of technically-minded marketers and consultants:

- **Advanced Media Mix Modeling**: Utilize state-of-the-art statistical techniques to understand the impact of various marketing channels on your key performance indicators (KPIs).
- **Cross-Channel Optimization**: Gain insights into how different marketing channels interact and influence each other, allowing for more effective budget allocation.
- **Customizable Models**: Tailor the modeling approach to your specific business needs and data structures.
- **Data-Driven Insights**: Transform complex data into actionable insights, enabling informed decision-making.
- **Scalable Solutions**: Whether you're a small agency or a large corporation, Griffin MMM can adapt to your needs.
- **Visualization Tools**: Powerful plotting functions to help you communicate results effectively to stakeholders.
- **Flexible API**: A comprehensive API that allows for integration with your existing workflow and tools.

### Who Should Use This Guide

This guide is primarily designed for:

- **Marketing Consultants**: Professionals who provide strategic marketing advice to clients and need robust tools to support their recommendations.
- **Technically-Minded Marketers**: Marketers with a strong analytical background who are comfortable with advanced statistical concepts and programming.
- **Small Agencies**: Marketing agencies looking to enhance their analytical capabilities and offer data-driven strategies to their clients.
- **Data Scientists in Marketing**: Professionals who bridge the gap between complex data analysis and marketing strategy.
- **Marketing Analysts**: Individuals responsible for measuring and optimizing marketing performance across channels.

Users of Griffin MMM are expected to have experience in technical modeling and be comfortable with concepts such as statistical analysis, data preprocessing, and interpretation of complex models. This guide assumes a basic understanding of marketing principles, statistics, and programming (particularly Python).

While Griffin MMM provides powerful tools, it's important to note that it's designed for users who already have a foundation in technical modeling. The product aims to enhance and streamline your existing workflow, providing you with advanced capabilities to perform in-depth marketing analytics.

Throughout this guide, you'll learn how to leverage Griffin MMM to its full potential, enabling you to make more informed decisions, optimize your marketing mix, and drive better results for your organization or clients.

## Getting Started

This section will guide you through the process of accessing, installing, and setting up Griffin MMM based on your subscription level. Whether you're using the free demo or have subscribed to the Pro version, we'll help you get up and running quickly.

### Accessing Griffin MMM

Griffin MMM is distributed via a private GitHub repository. Your access level depends on your subscription:

#### Demo Version (Free)

The demo version of Griffin MMM is available at no cost and offers:

- Unlimited access to the demo version
- Support for up to 4 media channels
- All features and visualizations
- Basic / Community support

This version is perfect for businesses or marketers looking to explore MMM capabilities.

#### Pro Version (Yearly Subscription)

The Pro version unlocks the full potential of Griffin MMM with an annual subscription, offering:

- Full access to all features
- Support for unlimited media channels
- Advanced analytics and visualizations
- Priority email support
- Quarterly strategy consultation
- Regular software updates

This version is ideal for agencies of all sizes and mid-size to large businesses serious about optimizing their marketing mix.

Getting started with Griffin MMM is incredibly simple and user-friendly. We provide a Jupyter notebook that can be easily accessed and run through platforms like Google Colab or similar services.

1. **Access the Notebook:** Upon subscription (Demo or Pro), you'll receive a link to the Griffin MMM Jupyter notebook.

2. **Open in Colab:** Click the link to open the notebook in Google Colab (or your preferred Jupyter notebook platform).

3. **Run the Notebook:** Follow the step-by-step instructions in the notebook. All necessary dependencies and code are included.

4. **Upload Your Data:** When prompted, upload your CSV data file to the notebook environment.

5. **Execute the Analysis:** Run each cell in the notebook to perform your Media Mix Modeling analysis.

That's it! No complex installation or setup is required. The notebook guides you through the entire process, from data input to result interpretation.

**Note for Pro Users:** Your Pro access key will be required to unlock advanced features within the notebook. Enter it when prompted.

This streamlined approach allows you to focus on your analysis rather than technical setup. The notebook includes detailed explanations and visualizations at each step, making the MMM process accessible and insightful.

### Basic Setup

After installation, you'll need to prepare your data and create a configuration file:

1. **Prepare your data:** Ensure your data is in a CSV format with columns for date, target variable, media channels (impressions and spend), and any additional features.

2. **Create a configuration file:** Create a file named `config.yaml` in your project directory. Here's a basic template:

   ```yaml
   model_name: MMM
   raw_data_granularity: weekly
   train_test_ratio: 0.9
   date_col: "date"
   target_col: "sales"
   media:
     - display_name: "TV"
       impressions_col: tv_impressions
       spend_col: tv_spend
     - display_name: "Radio"
       impressions_col: radio_impressions
       spend_col: radio_spend
     - display_name: "Digital"
       impressions_col: digital_impressions
       spend_col: digital_spend
```

3. **Set up your project directory:** Your project directory should look like this:

```
project_directory/
├── config.yaml
├── data.csv
└── results/
```