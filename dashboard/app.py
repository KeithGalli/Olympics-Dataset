from shiny.express import input, render, ui
from shiny import reactive

from pathlib import Path
import pandas as pd

ui.page_opts(title="hello")

# @reactive.calc
# def dat():
#     directory = Path(__file__).parent.parent
#     return pd.read_csv(f'{directory}/clean-data/populations.csv')

# @reactive.calc
# def results():
#     directory = Path(__file__).parent.parent
#     results = pd.read_csv(f'{directory}/clean-data/results.csv')
#     # results = results[(results['noc']==input.country())]
#     # if not input.summer():
#     #     results = results[results['type'] == 'Winter']
#     # if not input.winter():
#     #     results = results[results['type'] == 'Summer']
#     # if input.medalists():
#     #     results = results[results['medal'].notna()]
#     # return results
#     return results

# with ui.layout_sidebar():
#     with ui.sidebar():
#         df = dat()
#         country_dict = df.set_index('Country Code')['Country Name'].to_dict()
#         countries = df['Country Code'].unique().tolist()
#         ui.input_select("country", "Pick your country",  country_dict)
#         ui.input_checkbox("summer", "Summer Games?", True)
#         ui.input_checkbox("winter", "Winter Games?", True)
#         ui.input_checkbox("medalists", "Only Include Medalists", False)

#     with ui.card(height='1200px'):
#         @render.data_frame
#         def show_results():
#             return results().head(250)

#     with ui.card():
#         @render.data_frame
#         def show_table():
#             df = dat()
#             return df.head(250)