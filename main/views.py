from flask import render_template, send_from_directory, request, Markup
from werkzeug.utils import redirect

from app import service
from . import main
from config import *
from instance.config import *
import folium
import folium.plugins as plugins

@main.route('/', methods=['GET', 'POST'])
def index():
    start_coords = (37.49, 127.027)
    folium_map = folium.Map(location=start_coords, zoom_start=11)
    plugins.LocateControl(auto_start=True).add_to(folium_map)
    # geojson = folium.GeoJson(states).add_to(folium_map)
    # plugins.Search(geojson).add_to(folium_map)
    return render_template('bootstrap/folium_index.html', map=Markup(folium_map._repr_html_()))