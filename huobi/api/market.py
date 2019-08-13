import requests
import json
import traceback



def get_kline(symbol="btcusdt",period="5min",size=200):
    r=requests.get('https://api.huobi.pro/market/history/kline?period='+period+'&size='+str(size)+'&symbol='+symbol)
    try:
        result = json.loads(r.text)
        if result['status'] == 'ok' :
            data = result['data']
            return data
    except:
        print("查询klin失败！")
        traceback.print_exc()
    return []
    
