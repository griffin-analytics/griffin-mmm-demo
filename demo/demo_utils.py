from ipywidgets import widgets, Layout
from IPython.display import display
from datetime import datetime
import yaml

desc_width = "120px"

# Basic Settings
model_name = widgets.Text(
    value='MMM',
    description='Model Name:',
    disabled=True,
    style={'description_width': desc_width}
)

total_rows = draws = widgets.IntText(
    value=171,
    description='Total:',
    style={'description_width': desc_width}
)

start_date = widgets.DatePicker(
    value=datetime.strptime('2019-07-28', '%Y-%m-%d'),
    description='Start Date:',
    style={'description_width': desc_width}
)

end_date = widgets.DatePicker(
    value=datetime.strptime('2022-10-30', '%Y-%m-%d'),
    description='End Date:',
    style={'description_width': desc_width}
)

raw_data_granularity = widgets.Dropdown(
    options=['daily', 'weekly'],
    value='weekly',
    description='Data Granularity:',
    style={'description_width': desc_width}
)

train_test_ratio = widgets.FloatSlider(
    value=1.0,
    min=0.1,
    max=1.0,
    step=0.01,
    description='Train/Test Ratio:',
    style={'description_width': desc_width}
)

# Column Definitions

# Create the TagsInput widget
ignore_cols = widgets.TagsInput(
    value=['price', 'other_events'],
    description='Ignore Columns:',
    style={'description_width': 'initial'}
)

date_col = widgets.Text(
    value='date',
    description='Date Column:',
    style={'description_width': desc_width}
)

target_col = widgets.Text(
    value='subscribers',
    description='Target Column:',
    style={'description_width': desc_width}
)

target_type = widgets.Dropdown(
    options=['conversion', 'revenue'],
    value='conversion',
    description='Target Type:',
    style={'description_width': desc_width}
)

extra_features = widgets.TagsInput(
    value=['covid_index', 'competitor_spend', 'promo_events'],
    description='Extra Features:',
    allow_duplicates=False,
    style={'description_width': 'initial'}
)

# Media Channels
def create_media_channel_widgets(num=4):
    channels = []
    for i in range(num):
        channel = widgets.VBox([
            widgets.HTML(f'<h4>Media Channel {i+1}</h4>'),
            widgets.Text(
                value=f'Media Channel {i+1}',
                description='Display Name:',
                style={'description_width': desc_width}
            ),
            widgets.Text(
                value=f'media_imp_{i+1}',
                description='Impressions Col:',
                style={'description_width': desc_width}
            ),
            widgets.Text(
                value=f'media_cost_{i+1}',
                description='Spend Col:',
                style={'description_width': desc_width}
            )
        ])
        channels.append(channel)
    return widgets.VBox(channels)

media_channels = create_media_channel_widgets()

# Model Parameters
tune = widgets.IntText(
    value=1000,
    description='Tune:',
    style={'description_width': desc_width }
)

draws = widgets.IntText(
    value=2000,
    description='Draws:',
    style={'description_width': desc_width }
)

chains = widgets.IntText(
    value=4,
    description='Chains:',
    style={'description_width': desc_width }
)

ad_stock_max_lag = widgets.IntText(
    value=8,
    description='Ad Stock Max Lag:',
    style={'description_width': desc_width}
)

target_accept = widgets.FloatText(
    value=0.95,
    description='Target Accept:',
    style={'description_width': desc_width }
)

# Prophet Settings
prophet_settings = widgets.VBox([
    widgets.Checkbox(value=True, description='Include Holidays'),
    widgets.Text(value='US', description='Holiday Country:', style={'description_width': desc_width }),
    widgets.Checkbox(value=True, description='Yearly Seasonality'),
    widgets.Checkbox(value=True, description='Trend'),
    widgets.Checkbox(value=True, description='Weekly Seasonality')
])

seed = widgets.IntText(
    value=42,
    description='Random Seed:',
    style={'description_width': desc_width }
)

def get_latest_config():
    config = {
        '### MMM options': '\n',
        'model_name': model_name.value,
        'data_rows': {
            'total': total_rows.value,
            # 'start_date': start_date.value,
            # 'end_date': end_date.value
            'start_date': start_date.value,
            'end_date': end_date.value
        },
        'raw_data_granularity': raw_data_granularity.value,
        'train_test_ratio': train_test_ratio.value,
        '\n### Column Definitions': '\n',
        'ignore_cols': list(ignore_cols.value),
        'date_col': date_col.value,
        'target_col': target_col.value,
        'target_type': target_type.value,
        'extra_features_cols': list(extra_features.value),
        'extra_features_impact': {
            'competitor_spend': 'negative'
        },
        'media': [
            {
                'display_name': media_channels.children[i].children[1].value,
                'impressions_col': media_channels.children[i].children[2].value,
                'spend_col': media_channels.children[i].children[3].value
            }
            for i in range(len(media_channels.children))
        ],
        '\n### Model Parameters': '\n',
        'tune': tune.value,
        'draws': draws.value,
        'chains': chains.value,
        'ad_stock_max_lag': ad_stock_max_lag.value,
        'target_accept': target_accept.value,
        '\n### Prophet seasonality settings': '\n',
        'prophet': {
            'include_holidays': prophet_settings.children[0].value,
            'holiday_country': prophet_settings.children[1].value,
            'yearly_seasonality': prophet_settings.children[2].value,
            'trend': prophet_settings.children[3].value,
            'weekly_seasonality': prophet_settings.children[4].value
        },
        'seed': seed.value,
        '\n### Custom priors': '\n',
        'custom_sigma': False,
        'custom_priors': {
            'intercept': {
                'dist': 'LogNormal',
                'kwargs': {
                    'mu': 0,
                    'sigma': 5
                }
            },
            'saturation_beta': {
                'dist': 'HalfNormal',
                'kwargs': {
                    'sigma': 2
                }
            },
            'adstock_alpha': {
                'dist': 'Beta',
                'kwargs': {
                    'alpha': 1,
                    'beta': 3
                }
            },
            'saturation_lam': {
                'dist': 'Gamma',
                'kwargs': {
                    'alpha': 3,
                    'beta': 1
                }
            },
            'likelihood': {
                'dist': 'Normal',
                'kwargs': {
                    'sigma': {
                        'dist': 'HalfNormal',
                        'kwargs': {
                            'sigma': 2
                        }
                    }
                }
            },
            'gamma_control': {
                'dist': 'HalfNormal',
                'kwargs': {
                    'sigma': 1
                }
            },
            'gamma_fourier': {
                'dist': 'Laplace',
                'kwargs': {
                    'mu': 0,
                    'b': 1
                }
            }
        }
    }
    return config

# Custom YAML representer for datetime objects
def datetime_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:timestamp', data.strftime('%Y-%m-%d'), style='')

yaml.add_representer(datetime, datetime_representer)

# Create YAML preview widget
yaml_preview = widgets.Textarea(
    description='config.yml:',
    disabled=True,
    layout=widgets.Layout(width='500px', height='1700px')
)

# Save Button and Output
save_button = widgets.Button(
    description='Save as config.yml',
    button_style='success',
    layout=widgets.Layout(width='150px')
)

def save_config(button):
    # Get the config dictionary directly - no need to parse it
    config_dict = get_latest_config()
    
    # Dump it to file
    with open('config.yml', 'w') as f:
        yaml.dump(
            config_dict,
            f,
            default_flow_style=False,
            sort_keys=False,
            indent=3,
            default_style='', # Prevents adding quotes
            allow_unicode=True
        )
    print("Saved to config.yml")
save_button.on_click(save_config)

# Create button container for centering
button_container = widgets.HBox([save_button], 
    layout=Layout(
        display='flex',
        justify_content='center',
        width='500px'  # Match textarea width
    )
)

# Combine into vertical layout
right_panel = widgets.VBox([
    yaml_preview,
    button_container
], layout=Layout(
    # border='1px solid #ccc',
    padding='10px',
    margin='5px'
))

def update_yaml_preview(*args):
    """Update the YAML preview whenever any widget changes"""
    config = get_latest_config()
    
    # Convert to YAML and update preview
    yaml_str = yaml.dump(
        config,
        sort_keys=False,
        indent=3,
        default_style='',  # Prevents adding quotes
        allow_unicode=True
    )
    yaml_preview.value = yaml_str

# Create section headers
basic_header = widgets.HTML(value='<h3 style="margin-top:20px">MMM Options</h3>')
columns_header = widgets.HTML(value='<h3 style="margin-top:20px">Column Definitions</h3>')
media_header = widgets.HTML(value='<h3 style="margin-top:20px">Media Channels</h3>')
model_header = widgets.HTML(value='<h3 style="margin-top:20px">Model Parameters</h3>')
prophet_header = widgets.HTML(value='<h3 style="margin-top:20px">Prophet Settings</h3>')

# Create left panel with all widgets
left_panel = widgets.VBox([
    basic_header,
    model_name,
    total_rows,
    start_date, 
    end_date, 
    raw_data_granularity, 
    train_test_ratio,
    columns_header,
    date_col, 
    target_col, 
    target_type,
    widgets.Label('extra_features_cols:'),
    extra_features,
    widgets.Label('ignore_cols: '),
    ignore_cols, 
    media_header,
    media_channels,
    model_header,
    tune, 
    draws, 
    chains, 
    ad_stock_max_lag, 
    target_accept, 
    seed,
    prophet_header,
    prophet_settings
])

# Create horizontal layout with widgets and YAML preview
config_widget = widgets.HBox([
    left_panel,
    right_panel
], layout=widgets.Layout(width='100%'), justify_content='space-around')

# Register observers for all widgets to update YAML preview
for widget in [model_name, start_date, end_date, raw_data_granularity, train_test_ratio,
               ignore_cols, date_col, target_col, target_type, extra_features,
               tune, draws, chains, ad_stock_max_lag, target_accept, seed]:
    widget.observe(update_yaml_preview, 'value')

# Register observers for media channel widgets
for channel in media_channels.children:
    for widget in channel.children[1:]:  # Skip the header
        widget.observe(update_yaml_preview, 'value')

# Register observers for prophet settings
for widget in prophet_settings.children:
    widget.observe(update_yaml_preview, 'value')

# Initial update of YAML preview
update_yaml_preview()