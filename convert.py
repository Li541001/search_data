from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import requests
import json


STUDENT_NUMBER = 7      #設定學生數量 需比原學生數多一人
EXCEL_FILE_PATH = 'database.xlsx'   #excel檔案位置

new_object = {}
xlsx = load_workbook(EXCEL_FILE_PATH)
xlsxs = xlsx.active

response = requests.get('https://api.jsonstorage.net/v1/json/4eed805d-59cf-4ff8-ad3b-faf98c316270/c0e5a20d-e108-45d2-9097-19ef727e7af4')
print(f'oldData: {response.text}')
new_object = json.loads(response.text)

for i in range(2,STUDENT_NUMBER):
    id = str(xlsxs['A'+str(i)].value)
    chinese = xlsxs['B'+str(i)].value
    english = xlsxs['C'+str(i)].value
    math = xlsxs['D'+str(i)].value
    one = xlsxs['E'+str(i)].value
    two = xlsxs['F'+str(i)].value
    new_object.update({id:{'chinese':str(chinese),'english':str(english),'math':str(math),'one':str(one),'two':str(two)}})

json_object = json.dumps(new_object)
print(f'giveData: {json_object}')

r = requests.put('https://api.jsonstorage.net/v1/json/4eed805d-59cf-4ff8-ad3b-faf98c316270/c0e5a20d-e108-45d2-9097-19ef727e7af4?apiKey=a2ddf8a1-e69b-4a56-84be-ed30fa49a6ad',data=json_object,headers = {"Content-type": "application/json"})
print(r)

response = requests.get('https://api.jsonstorage.net/v1/json/4eed805d-59cf-4ff8-ad3b-faf98c316270/c0e5a20d-e108-45d2-9097-19ef727e7af4')
print(f'newData: {response.text}')




'''
{
  0907119:{
    chinese:76,
    english:81.5,
    math:88
  }
}

'''
