from ipywidgets import widgets, Layout
from IPython.display import display
from datetime import datetime
import yaml

desc_width = "120px"

import ipywidgets as widgets
from ipywidgets import HBox, VBox, Layout


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

def create_column_selector(initial_cols=None, description=None):
    if initial_cols is None:
        initial_cols = []
    
    # Selected columns list
    selected_cols = widgets.SelectMultiple(
        options=initial_cols,
        description=description,
        allow_duplicates=False,
        layout=Layout(height='100px'),
        style={'description_width': desc_width}
    )
    selected_cols.observe(update_yaml_preview, 'value')
    
    # Text input for new column
    new_col_input = widgets.Text(
        placeholder='Enter column name',
        layout=Layout(width='220px'),
        style={'description_width': desc_width}
    )
    
    # Add button
    add_button = widgets.Button(
        description='Add',
        button_style='success',
        layout=Layout(width='70px', margin='0 0 0 auto'),
        disabled=True  # Initially disabled
    )
    
    # Remove button
    remove_button = widgets.Button(
        description='Remove',
        button_style='danger',
        layout=Layout(width='70px', margin='0 0 0 auto'),
        disabled=True  # Initially disabled
    )
    
    def add_column(b):
        if new_col_input.value:
            new_options = list(selected_cols.options) + [new_col_input.value]
            selected_cols.options = sorted(list(set(new_options)))
            new_col_input.value = ''  # Clear input
            add_button.disabled = True  # Disable after adding
    
    def remove_columns(b):
        if selected_cols.value:  # If any columns are selected
            new_options = [col for col in selected_cols.options if col not in selected_cols.value]
            selected_cols.options = new_options
            remove_button.disabled = True  # Disable after removing
    
    def on_selection_change(change):
        remove_button.disabled = len(change['new']) == 0
    
    def on_input_change(change):
        add_button.disabled = len(change['new']) == 0
    
    add_button.on_click(add_column)
    remove_button.on_click(remove_columns)
    selected_cols.observe(on_selection_change, names='value')
    new_col_input.observe(on_input_change, names='value')
    
    # Layout
    input_box = HBox([new_col_input, add_button])
    widget = VBox([
        selected_cols,
        remove_button,
        input_box
    ])
    
    # Add method to get YAML format
    def to_yaml_format():
        return list(selected_cols.options)
    
    widget.to_yaml_format = to_yaml_format
    return widget
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
    min=0.8,
    max=1.0,
    step=0.01,
    description='Train/Test Ratio:',
    style={'description_width': desc_width}
)

# Column Definitions

ignore_cols = create_column_selector(
    initial_cols=['price', 'other_events'],
    description='extra_features_cols:'
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

extra_features = create_column_selector(
    initial_cols=['covid_index', 'competitor_spend', 'promo_events'],
    description='ignore_cols:'
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

def get_latest_config():
    # Debug information about prophet settings
    print("\nProphet Settings Debug Info:")
    print(f"Number of prophet settings widgets: {len(prophet_settings.children)}")
    print("Prophet settings children:")
    for i, child in enumerate(prophet_settings.children):
        print(f"  {i}: {type(child).__name__} - {child.description}")
    
    # Initialize prophet config with defaults
    prophet_config = {
        'include_holidays': True,
        'holiday_country': 'US',
        'yearly_seasonality': True,
        'trend': True,
        'weekly_seasonality': True
    }
    
    # Try to get values from widgets if they exist
    try:
        num_children = len(prophet_settings.children)
        if num_children > 0:
            prophet_config['include_holidays'] = prophet_settings.children[0].value
        if num_children > 1:
            prophet_config['holiday_country'] = prophet_settings.children[1].value
        if num_children > 2:
            prophet_config['yearly_seasonality'] = prophet_settings.children[2].value
        if num_children > 3:
            prophet_config['trend'] = prophet_settings.children[3].value
        if num_children > 4:
            prophet_config['weekly_seasonality'] = prophet_settings.children[4].value
    except Exception as e:
        print(f"\nError accessing prophet settings: {str(e)}")
        print("Using default values for missing settings")
    
    config = {
        '### MMM options': '\n',
        'model_name': model_name.value,
        'data_rows': {
            'total': total_rows.value,
            'start_date': start_date.value,
            'end_date': end_date.value
        },
        'raw_data_granularity': raw_data_granularity.value,
        'train_test_ratio': train_test_ratio.value,
        '\n### Column Definitions': '\n',
        'ignore_cols': list(ignore_cols.to_yaml_format()),
        'date_col': date_col.value,
        'target_col': target_col.value,
        'target_type': target_type.value,
        'extra_features_cols': list(extra_features.to_yaml_format()),
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
        'prophet': prophet_config,
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

seed = widgets.IntText(
    value=42,
    description='Random Seed:',
    style={'description_width': desc_width }
)

# Custom YAML representer for datetime objects
def datetime_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:timestamp', data.strftime('%Y-%m-%d'), style='')

yaml.add_representer(datetime, datetime_representer)

# Create YAML preview widget
yaml_preview = widgets.Textarea(
    description='config.yml:',
    disabled=True,
    layout=widgets.Layout(width='500px', height='1800px')
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
    padding='10px',
    margin='5px'
))


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
    extra_features,
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
