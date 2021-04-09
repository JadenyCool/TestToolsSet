import re

a = '         self.ratioLabel.text = [NSString stringWithFormat:@"%@", NSLocalizedString(    @"直流汇流箱组,串离散率",  nil), "直流汇流箱组,串离散率"];'

# line = re.sub(' ','',a)
# print(line)
# pchinese = re.compile('([\u4e00-\u9fa5]+)+?')
# CH_Key = pchinese.findall(line, re.MULTILINE)
# print(CH_Key)


#
#
# uncn = re.compile(r'([\u4e00-\u9fa5]+)+?')
# en = "".join(uncn.findall(a.lower()))
# print(en)


# b = "fr, es, pl , nl, de"
# # d = b.strip(",").split(",")
# d = re.sub(" ","", b).split(",")
# print(d)

# filepath = "D:\\Code\\fusionsolar_7\\iCleanPower\\en.lproj\\Localizable.strings"
# with open(filepath, 'r', encoding="utf-8") as f:
#     for line in f:
#         # print(line)
#         resoucefileKey = line.split("=")[0].strip().replace('"','')
#         print(resoucefileKey)


enFile = "D:\Code\\fusionsolar_7\iCleanPower\en.lproj\\Localizable.strings"
Jafile = "D:\Code\\fusionsolar_7\iCleanPower\ja.lproj\\Localizable.strings"

a = []
with open(Jafile, 'r', encoding="utf-8") as f:
    for line in f:
        line = line.replace('" =', '"=')
        resoucefileKey = line.split('\"=')[0].lstrip('"')
        a.append(resoucefileKey)
enb = []
with open(enFile, 'r', encoding="utf-8") as ff:
    for line in ff:
        if '=' in line:
            line = line.replace('" =', '"=')
            resoucefileKey = line.split('\"=')[0].lstrip('"')
            enb.append(resoucefileKey)

test = "D:\ddd\\7tran\\tranOne\\test.String"
with open(test, 'w', encoding='utf-8') as ft:
    for i in range(len(enb)):
        line = '"{}" = ""'.format(enb[i])
        print(line)
        ft.write(line + "\n")

    # with open(Jafile, 'a+', encoding='utf-8') as fw:
    #     for i in range(len(enb)):
    #         if enb[i] not in a:
    #             line = '"{}" = "{}";'.format(enb[i], "")
    #             fw.write(line + '\n')
