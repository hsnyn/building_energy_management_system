import pandas as pd
import pyodbc
data = pd.read_csv(r'C:\Users\user\Desktop\AI-1_235.csv')
data['Date'] = data['Date'].str.replace('/','')
data['Time'] = data['Time'].str.replace(':','')
data = data[['Date', 'Time', 'AI Chiller Cost', 'Legacy Chiller Cost','AI Chiller Energy(MJ)', 'Legacy Chiller Energy(MJ)', 'Visitors','Otemp','OHum', 'Legacy AHU RT', 'AI AHU RT', 'AI_AC-1', 'AI_AC-2','AI_AC-3','AI_AC-4', 'AI_ AC-5', 'AI_ AC-6', 'AI_LTC-1', 'AI_LTC-2','AI_LTC-3','AI_STC-1', 'AI_STC-2', 'AC-1', 'AC-2', 'AC-3', 'AC-4', 'AC-5','AC-6','LTC-1', 'LTC-2', 'LTC-3', 'STC-1', 'STC-2']].values
server = r'NYNE_PC\NYNESQL' 
database = 'testDB' 
username = 'sa' 
password = '2424' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
for i in range(len(data)):
    #cursor.execute("Delete from dbo.CSV_DATA_DONG_DAEGU where index_column = "+str(i)+";")
    cursor.execute("INSERT INTO dbo.CSV_DATA_DONG_DAEGU ([index_column],[date_col],[time_col],[AI_chiller_cost],[Legacy_chiller_cost],[AI_chiller_energy],[Legacy_chiller_energy],[visitors],[otemp],[ohum],[Legacy_AHU_RT],[AI_AHU_RT],[AI_AC_1],[AI_AC_2],[AI_AC_3],[AI_AC_4],[AI_AC_5],[AI_AC_6],[AI_LTC_1],[AI_LTC_2],[AI_LTC_3],[AI_STC_1],[AI_STC_2],[AC_1],[AC_2],[AC_3],[AC_4],[AC_5],[AC_6],[LTC_1],[LTC_2],[LTC_3],[STC_1],[STC_2]) VALUES("+str(i)+","+str(data[i][0])+","+str(data[i][1])+","+str(data[i][2])+","+str(data[i][3])+","+str(data[i][4])+","+str(data[i][5])+","+str(data[i][6])+","+str(data[i][7])+","+str(data[i][8])+","+str(data[i][9])+","+str(data[i][10])+","+str(data[i][11])+","+str(data[i][12])+","+str(data[i][13])+","+str(data[i][14])+","+str(data[i][15])+","+str(data[i][16])+","+str(data[i][17])+","+str(data[i][18])+","+str(data[i][19])+","+str(data[i][20])+","+str(data[i][21])+","+str(data[i][22])+","+str(data[i][23])+","+str(data[i][24])+","+str(data[i][25])+","+str(data[i][26])+","+str(data[i][27])+","+str(data[i][28])+","+str(data[i][29])+","+str(data[i][30])+","+str(data[i][31])+","+str(data[i][32])+");")
    cnxn.commit()
    print(i,data[i])