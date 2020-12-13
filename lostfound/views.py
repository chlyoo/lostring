from flask import render_template, Markup

from flask_login import login_required
from . import lostfound
import folium
import folium.plugins as plugins
from .forms import LostForm, FoundForm
from user_folium import ClickForOneMarker


@lostfound.route('/lost', methods=['GET', 'POST'])
@login_required
def register_lost():
    form = LostForm()
    # TODO: 폼데이터 분실 디비에 저장
    start_coords = (37.49, 127.027)
    folium_map = folium.Map(
        location=start_coords,
        zoom_start=11,
    )
    # geojson1 = folium.GeoJson(
    #     skorea_provinces_geo,
    #     name = 'skorea-provinces',
    # ).add_to(folium_map)

    plugins.LocateControl(auto_start=True).add_to(folium_map)  # 현재위치로 초기화
    folium_map.add_child(ClickForOneMarker(popup='분실위치'))
    return render_template('bootstrap/register.html', form=form, map=Markup(folium_map._repr_html_()))


@lostfound.route('/found', methods=['GET', 'POST'])
@login_required
def register_found():
    form = FoundForm()
    # TODO: 폼에서 발견 디비에 저장
    # TODO: Register Service 랑 연동
    start_coords = (37.49, 127.027)
    folium_map = folium.Map(
        location=start_coords,
        zoom_start=11,
    )
    plugins.LocateControl(auto_start=True).add_to(folium_map)  # 현재위치로 초기화
    folium_map.add_child(ClickForOneMarker(popup='습득위치'))
    return render_template('bootstrap/register.html', form=form, map=Markup(folium_map._repr_html_()))


@lostfound.route('/my_page', methods=['GET', 'POST'])
@login_required
def my_page():
    pass
    return render_template('bootstrap/mypage.html')
