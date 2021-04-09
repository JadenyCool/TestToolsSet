import unicodedata
ad = "当前节点不能退回，上一节点用户已被删除，请走下一步流程【】！（）；;  "

table = {ord(f):ord(t) for f,t in zip(
     u'，。！？【】（）％＃＠＆１２３４５６７８９０',
     u',.!?[]()%#@&1234567890')}

t = ad.translate(table)
print(t)

b = "登 录"
print(b.replace(" ",""))