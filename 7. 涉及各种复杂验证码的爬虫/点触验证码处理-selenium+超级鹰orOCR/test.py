posi={'err_no': 0, 'err_str': 'OK', 'pic_id': '1164016367699600001', 'pic_str': '170,64|135,135|39,113|187,146'}
posi=posi['pic_str']
result_list = posi.split('|') #返回的验证码进行分割，得到列表比如 ['125,168','148,193','188,257']
for result in result_list:
    x = result.split(',')[0]
    y = result.split(',')[1]
    print(x,y)