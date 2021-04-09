import openpyxl

path = 'D:/ddd/7tran/tranOne/tranOne.xlsx'
excel_chi_otherLang = {}
openfile = openpyxl.load_workbook(filename=path, data_only=True)
getSheetData = openfile.get_sheet_by_name("Sheet1")

excelfuhao = ["。", ":", "：", ".", ";"]
j = 1
for excel_translate in list(getSheetData.columns)[3]:
    excel_value = excel_translate.value  # 小语种

    if excel_value is None:
        j = j + 1

    else:
        Ckey_value = getSheetData.cell(row=j, column=1).value
        print(Ckey_value)
        if Ckey_value:
            for i in range(len(excelfuhao)):
                if Ckey_value.endswith("{}".format(excelfuhao[i])):
                    Ckey_value = Ckey_value.replace("{}".format(excelfuhao[i]), "")
                    break
                if excel_value.endswith("{}".format(excelfuhao[i])):
                    excel_value = excel_value.replace("{}".format(excelfuhao[i]), "")
            excel_chi_otherLang.update({Ckey_value: excel_value})
            j = j + 1
        else:
            j = j + 1

# print(excel_chi_otherLang)
for k, v in excel_chi_otherLang.items():
    print("-{}-Jerry-------{}---------{}".format(j, k, v))
