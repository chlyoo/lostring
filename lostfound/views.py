from flask import render_template, Markup, url_for, redirect, flash

from flask_login import login_required, current_user
from . import lostfound
import folium
import folium.plugins as plugins
from .forms import LostForm, FoundForm
from user_folium import ClickForOneMarker
from app import db
from models import FoundedItem, LostedItem

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
    if form.validate_on_submit():
        lostitem = LostedItem(form.itemname.data, form.category.data, form.place.data, form.latitude.data, form.longitude.data, form.lost_date.data, current_user.id, form.detail.data)
        collection = db.get_collection('lostdata')
        collection.insert_one(lostitem.to_dict())
        flash('등록되었습니다.')
        return redirect(url_for('lostfound.my_page'))
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
    if form.validate_on_submit():
        founditem = FoundedItem(current_user.id)
        collection = db.get_collection('founddata')
        collection.insert_one(founditem.to_dict())
        return redirect(url_for('lostfound.my_page'))
    return render_template('bootstrap/register.html', form=form, map=Markup(folium_map._repr_html_()))


@lostfound.route('/my_page', methods=['GET', 'POST'])
@login_required
def my_page():
    found = None
    lost = None
    lost_collection = db.get_collection('lostdata')
    lost_result = lost_collection.find_one({'who':current_user.id})
    if lost_result:
        lost = [lost_result['when'], lost_result['status']]
    # result = lost_collection.find_one({'who':current_user.id}, sort=[('now',-1)])
    found_collection = db.get_collection('founddata')
    found_result = found_collection.find_one({'who':current_user.id})
    if found_result:
        found = [found_result['when'],found_result['status']]
    return render_template('bootstrap/mypage.html', lost= lost, found=found)
