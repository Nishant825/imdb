import pandas as pd
import mysql.connector
import time
import openpyxl

# mydb = mysql.connector.connect(
#     host = "dimoaurora-instance-1.cmrqk9dxqqdd.ap-southeast-2.rds.amazonaws.com",
#     user = "cpsadmin",
#     password = "aXBB41nbEZQ3qjRcV2uv",
#     database = 'demo_books'
# )


# df = pd.read_excel("/home/bh/Pictures/Schedular_list.xlsx", skiprows=[1], engine='odf')
# completed_time = []
# for value in df['Script name']:
#   cursor = mydb.cursor(dictionary=True)
#   while cursor.nextset():
#         pass
#   print("started")
#   cursor.execute(f"""SELECT id, program_name, timestamp, status, `result`, error
#           FROM scheduler_log where machine_id = 'cps_update' and `timestamp` like '%2023-07-20%' and program_name like '%{value}%' order by id desc;""")
#   result = cursor.fetchone()
#   if result:
#     result['status'] =='Complete'
#     print(value)
#     datetime = result["timestamp"]
#     formatted  = datetime.strftime("%Y-%m-%d %H:%M:%S")
#   else:
#     formatted = "error"
#   completed_time.append(formatted)
#   cursor.fetchall()
#   time.sleep(5)
#   cursor.close()
# mydb.close()


workbook = openpyxl.load_workbook("/home/bh/Pictures/Schedular_list.xlsx")
sheet = workbook['Sheet1']  # Replace 'Sheet1' with the name of your sheet

# Modify the data in the sheet (example: updating cell B2)
# sheet['C'] = completed_time
# sheet['C:C'] = ['2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21', '2023-06-28 23:16:21']

# data = ['2023-07-28 23:16:21'] * 25
for index, value in enumerate(data, start=3):
    print(index,"yooooo")
    sheet.cell(row=index, column=4, value=value)

print("success")
# Save the changes to the same Excel file
workbook.save("/home/bh/Pictures/Schedular_list.xlsx")
workbook.close()

# print(completed_time,"88888888888888888888888")
# df['Time Run'] = completed_time

# df.to_excel('/home/bh/Pictures/Schedular_list.ods', index=False, engine='odf')


