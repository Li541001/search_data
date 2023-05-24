from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import requests
import json


STUDENT_NUMBER = 7      #設定學生數量 需比原學生數多一人
EXCEL_FILE_PATH = 'database.xlsx'   #excel檔案位置
CHOICE_COLUMN = "BCDEFG"   #輸入判斷格位


new_object = {}
xlsx = load_workbook(EXCEL_FILE_PATH)
xlsxs = xlsx.active
#連接excel

response = requests.get('https://api.jsonstorage.net/v1/json/4eed805d-59cf-4ff8-ad3b-faf98c316270/c0e5a20d-e108-45d2-9097-19ef727e7af4')
print(f'oldData: {response.text}')
new_object = json.loads(response.text)
#取得database


for i in range(2,STUDENT_NUMBER):     #key為標題,value為值
    value = []
    title = []
    id = str(xlsxs['A'+str(i)].value)
    id_object={}
    new_object.update({id:id_object})
    id_object = new_object[id]
    
    for j in CHOICE_COLUMN:
      title = xlsxs[str(j)+'1'].value
      value = str(xlsxs[str(j)+str(i)].value)
      id_object.update({title:value})


    new_object.update({id:id_object})
#迴圈取得成績並轉換成正確形式

json_object = json.dumps(new_object)  #轉成json
print(f'giveData: {json_object}')

r = requests.put('https://api.jsonstorage.net/v1/json/4eed805d-59cf-4ff8-ad3b-faf98c316270/c0e5a20d-e108-45d2-9097-19ef727e7af4?apiKey=a2ddf8a1-e69b-4a56-84be-ed30fa49a6ad',data=json_object,headers = {"Content-type": "application/json"})
print(r)
#put到database

response = requests.get('https://api.jsonstorage.net/v1/json/4eed805d-59cf-4ff8-ad3b-faf98c316270/c0e5a20d-e108-45d2-9097-19ef727e7af4')
print(f'newData: {response.text}')
#再次讀取database



'''
{
  0907119:{
    chinese:76,
    english:81.5,
    math:88
  }
}

'''
