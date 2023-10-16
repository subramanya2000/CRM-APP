import _mysql_connector

dataBase = _mysql_connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345'
)

curserObject = dataBase.cursor()

curserObject.execute("CREATE DATABASE crmdb")
