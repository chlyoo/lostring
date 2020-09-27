from datetime import datetime, timedelta
from config import *
from instance.config import  *

class LostFound:
    def __init__(self, api):
      pass

    def get_from_api_area(self):
        url = PUBLIC_DATA_REQUEST_URL.format(quote(STATION), PUBLIC_DATA_SERVICE_KEY)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            try:
                response_body = response.read()
            except (http.client.IncompleteRead) as e:
                response_body = e.partial
            try:
                parse = json.loads(response_body)
            except:
                pass
    def get_from_api_foundArea(self):
        url = PUBLIC_DATA_REQUEST_URL.format(quote(STATION), PUBLIC_DATA_SERVICE_KEY)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            try:
                response_body = response.read()
            except (http.client.IncompleteRead) as e:
                response_body = e.partial
            try:
                parse = json.loads(response_body)
            except:
                pass
    def get_from_api_detail(self):
        url = PUBLIC_DATA_REQUEST_URL.format(quote(STATION), PUBLIC_DATA_SERVICE_KEY)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if (rescode == 200):
            try:
                response_body = response.read()
            except (http.client.IncompleteRead) as e:
                response_body = e.partial
            try:
                parse = json.loads(response_body)
            except:
                pass
#
#
#
# getLostGoodsInfoAccToClAreaPd
# getLostGoodsInfoAccTpNmCstdyPlace
# getLostGoodsDetailInfo
#
# getLostGoodsInfoAccToClAreaPd
# 분류별, 지역별, 기간별 분실물 정보 조회
# getLostGoodsInfoAccTpNmCstdyPlace
# 분실물 명칭, 보관 장소별 습득물 정보 조회
# getLostGoodsDetailInfo
# 분실물 상세정보 조회
