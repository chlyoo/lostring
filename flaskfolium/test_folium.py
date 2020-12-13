""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""

from flask import Flask, render_template, Markup
import folium
import folium.plugins as plugins
import geopandas

states = geopandas.read_file(
    "https://rawcdn.githack.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json",
    driver="GeoJSON",
)
app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (46.9540700, 142.7360300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    # return folium_map._repr_html_()
    plugins.LocateControl(auto_start=True).add_to(folium_map)
    geojson = folium.GeoJson(states).add_to(folium_map)
    plugins.Search(geojson).add_to(folium_map)
    return render_template('foliumtest.html', map=Markup(folium_map._repr_html_()))


if __name__ == '__main__':
    app.run(debug=True)
