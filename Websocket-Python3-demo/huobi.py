# -*- coding: utf-8 -*-

from websocket import create_connection
import gzip
import time
import traceback
import jsons
import numpy as np

if __name__ == '__main__':
    while(1):
        try:
            ws = create_connection("wss://www.hbdm.com/ws")
            break
        except:
            print('connect ws error,retry...')
            time.sleep(5)

    # 订阅 KLine 数据
    
    tradeStr_kline="""
    {"sub": "market.BTC_CQ.kline.1min",  "id": "id1"}
    """

    # 订阅 Market Detail 数据
    tradeStr_marketDetail="""
    {"sub": "market.BTC_CQ.detail",  "id": "id6" }
    """

    # 订阅 Trade Detail 数据
    tradeStr_tradeDetail="""
    {"sub": "market.BTC_CQ.trade.detail", "id": "id7"}
    """

    # 请求 KLine 数据
    tradeStr_klinereq="""
    {"req": "market.BTC_CQ.kline.1min", "id": "id4"}
    """

    # 请求 Trade Detail 数据
    tradeStr_tradeDetail_req="""
    {"req": "market.BTC_CQ.trade.detail", "id": "id5"}
    """

    # 订阅 Market Depth 数据
    tradeStr_marketDepth="""
    {
        "sub": "market.BTC_CQ.depth.step0", "id": "id9"
    }
    """
    
    maxlen = 60
    buyline = []
    sellline = []
    lastts = 0
    lastbuy = 0
    lastsell = 0
    for i in range(maxlen):
        buyline.append(0)
        sellline.append(0)
    
    ws.send(tradeStr_tradeDetail)
    trade_id = ''
    while(1):
        compressData=ws.recv()
        result=gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            ts=result[8:21]
            pong='{"pong":'+ts+'}'
            ws.send(pong)
#             ws.send(tradeStr_kline)
        else:
            try:
                result = jsons.loads(result)
                datas = result['tick']['data']
                for data in datas:
                    amount = data['amount']
                    direction = data['direction']
                    ts = int(data['ts'] /1000)
                    if lastts != ts :
                        lastts = ts
                        if direction == "sell":
                            sellline.append(lastsell)
                            sellline = sellline[1:]
                            sellavg = int( np.mean(sellline) )
                            print("1分钟平均卖出："+str(sellavg))
                            lastsell = 0
                        else:
                            buyline.append(lastbuy)
                            buyline = buyline[1:]
                            buysvg = int(np.mean(buyline) )
                            print("1分钟平均                         买入："+str(buysvg))
                            lastbuy = 0
                        
                    else:
                        if direction == "sell":
                            lastsell += amount
                        else:
                            lastbuy += amount

            except Exception:
                print(result)
                traceback.print_exc()

            

    
