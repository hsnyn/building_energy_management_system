import pyodbc, time
server = r'NYNE_PC\NYNESQL' 
database = 'testDB' 
username = 'sa' 
password = '2424' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
while 1:
    cursor.execute("SELECT TOP (1) [ID],[Name],[Position] FROM [testDB].[dbo].[autosementic_employee] ORDER BY ID DESC;")
    row = cursor.fetchone()
    time.sleep(1)
    print(row)