from jinja2 import Template
import folium


class ClickForOneMarker(folium.ClickForMarker):
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var new_mark = L.marker();
                function newMarker(e){
                    new_mark.setLatLng(e.latlng).addTo({{this._parent.get_name()}});
                    new_mark.dragging.enable();
                    new_mark.on('dblclick', function(e){ {{this._parent.get_name()}}.removeLayer(e.target)})
                    var lat = e.latlng.lat.toFixed(4),
                       lng = e.latlng.lng.toFixed(4);
                    new_mark.bindPopup({{ this.popup }});
                    parent.document.getElementById("latitude").value = lat;
                    parent.document.getElementById("longitude").value =lng;
                    };
                {{this._parent.get_name()}}.on('click', newMarker);
            {% endmacro %}
            """)  # noqa

    def __init__(self, popup=None):
        super(ClickForOneMarker, self).__init__(popup)


class LatLngtoForm(folium.LatLngPopup):
    _template = Template(u"""
            {% macro script(this, kwargs) %}
                var {{this.get_name()}} = L.popup();
                function latLngPop(e) {
                    data = [e.latlng.lat.toFixed(4) , e.latlng.lng.toFixed(4)];
                    parent.document.getElementById("latitude").value =data[0];
                    parent.document.getElementById("longitude").value =data[1];
                    {{this.get_name()}}
                        .setLatLng(e.latlng)
                        .setContent( '<span data='+data.toString()+' id="locate">여기</span>')
                        .openOn({{this._parent.get_name()}});
                    }
                {{this._parent.get_name()}}.on('click', latLngPop);
            {% endmacro %}
            """)  # noqa

    def __init__(self):
        super(LatLngtoForm, self).__init__()
        self._name = 'LatLngPopup'
