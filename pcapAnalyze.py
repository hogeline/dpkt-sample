import dpkt # version 1.9.0
import socket

# 解析したいpcapファイルを読み込ませる
with open("./tcp-ecn-sample.pcap", "rb") as f:
    pcr = dpkt.pcap.Reader(f)
    frame_count = 0
    flow_list = {}
    for t, buf in pcr:
        frame_count += 1
        try:
            eth = dpkt.ethernet.Ethernet(buf)
        except:
            print("Fail parse FrameNo: ", frame_count, '...skipped')
            continue
        # 型がIPアドレスなら
        if type(eth.data) == dpkt.ip.IP:
            ip = eth.data
            # 送信元IPアドレス
            src = socket.inet_ntoa(ip.src)
            # 送信先IPアドレス
            dst = socket.inet_ntoa(ip.dst)
            flow_word = src + " to " + dst
            # 同じipアドレスがflow_listにあれば
            if  flow_word in flow_list:
                # パケットサイズを更新
                flow_list[flow_word] += len(str(buf))
            else:
                # パケットサイズの初期値を代入
                flow_list[flow_word] = len(str(buf))
    # 結果表示
    for k,v in flow_list.items():
        print(k, ':', v, '[Byte]')
