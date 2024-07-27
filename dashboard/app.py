import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from shiny.express import ui, input, render
from shiny import reactive
import folium
from folium.plugins import HeatMap

ui.page_opts()

directory = Path(__file__).parent
nocs = pd.read_csv(f"{directory}/clean-data/noc_regions.csv")
nocs = nocs.sort_values('region', ascending=True)
region_to_noc = dict(zip(nocs['NOC'], nocs['region']))

with ui.layout_sidebar():
    with ui.sidebar(open='open'):
        ui.input_select("country", "Select a country", region_to_noc, selected='FRA')
        ui.input_checkbox("winter", "Include winter games?", True)
        ui.input_checkbox("medalists", "Only include medalists?", False)


    with ui.card():
        "Medals"

        @render.plot()
        def show_medals():
            df = get_medals()
            plt.plot(df['year'], df['medal'])
            plt.xlabel('Year')
            plt.ylabel('Medal Count')
            plt.title('Medals by Year')
            
        ## Print medals by country over time

    with ui.card():
        "Heatmap of athletes"
        @render.ui
        def show_heatmap():
            df = bios_df()
            m = folium.Map(location=[df['lat'].mean(), df['long'].mean()], zoom_start=2)
            heat_data = [[row['lat'], row['long']] for index, row in df.iterrows()]
            HeatMap(heat_data).add_to(m)
            return m
        

    with ui.card():
        @render.data_frame
        def results():
            return results_df().head(100)

@reactive.calc
def bios_df():
    bios = pd.read_csv(f'{directory}/clean-data/bios_locs.csv')
    print(input.country())
    bios = bios[bios['born_country'] == input.country()]
    country_df = bios[(bios['lat'].notna()) & (bios['long'].notna())]
    return country_df

@reactive.calc
def results_df():
    directory = Path(__file__).parent
    df = pd.read_csv(f'{directory}/clean-data/results.csv')
    df = df[df['noc'] == input.country()]
    if not input.winter():
        df = df[df['type']=='Summer']
    if input.medalists():
        df = df[df['medal'].notna()]
    return df

@reactive.calc
def get_medals():
    # Let's start simple and see if that works
    results = results_df()
    medals = results[(results['medal'].notna()) & (~results['event'].str.endswith('(YOG)'))]
    medals_filtered = medals.drop_duplicates(['year','type','discipline','noc','event','medal'])
    medals_by_year =  medals_filtered.groupby(['noc', 'year'])['medal'].count().loc[input.country()]
    return medals_by_year.reset_index()