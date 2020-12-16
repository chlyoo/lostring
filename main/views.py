from flask import render_template, send_from_directory, request, Markup
from werkzeug.utils import redirect

from app import service
from . import main
from config import *
from instance.config import *
import folium
import folium.plugins as plugins
# from ipywidgets import interact


@main.route('/', methods=['GET', 'POST'])
def index():
    start_coords = (37.49, 127.027)
    folium_map = folium.Map(
        # width='100%',
        # height='75%',
        min_zoom=7,
        location=start_coords,
        zoom_start=11,
        prefer_canvas=True,
    )
    skorea_provinces = folium.GeoJson(
        'user_folium/skorea-provinces-2018-geo.json',
        name='skorea-provinces',
        tooltip=folium.GeoJsonTooltip(
            fields=['name', 'base_year', 'name_eng', 'code'],
            aliases=['지역', '연도', '영문명', '지역코드'],
            localize=True
        )
    )
    plugins.LocateControl(auto_start=True).add_to(folium_map)  # 현재위치로 초기화

    skorea_municipalities = folium.GeoJson(
        'user_folium/skorea-municipalities-2018-geo.json',
        name='skorea-municipalities',
        tooltip=folium.GeoJsonTooltip(
            fields=['name', 'base_year', 'name_eng', 'code'],
            aliases=['지역', '연도', '영문명', '지역코드'],
            localize=True)
    )
    plugins.Search(
        layer=skorea_provinces,
        search_label='name',
        search_zoom=11,
        placeholder='province'
    ).add_to(folium_map)
    plugins.Search(
        layer=skorea_municipalities,
        search_label='name',
        search_zoom=11,
        placeholder='state'
    ).add_to(folium_map)

    # return render_template('v2temp/index.html', map=Markup(folium_map._repr_html_()))
    return render_template('bootstrap/folium_index.html', map=Markup(folium_map._repr_html_()))
