DS_NAME='jdbc/DSFISI13'
connect('weblogic','123webfisi','t3://localhost:7101')
edit()
startEdit()
cd('/')

cmo.createJDBCSystemResource(DS_NAME)

cd('/JDBCSystemResources/'+DS_NAME+'/JDBCResource/'+DS_NAME)
cmo.setName(DS_NAME)

cd('/JDBCSystemResources/'+DS_NAME+'/JDBCResource/'+DS_NAME+'/JDBCDataSourceParams/'+DS_NAME)
set('JNDINames',jarray.array([String(DS_NAME)], String))

cd('/JDBCSystemResources/'+DS_NAME+'/JDBCResource/'+DS_NAME+'/JDBCDriverParams/'+DS_NAME)
cmo.setUrl('jdbc:oracle:thin:@172.16.1.210:1521:xe')
cmo.setDriverName('oracle.jdbc.OracleDriver')
set('Password','TESTM')

cd('/JDBCSystemResources/'+DS_NAME+'/JDBCResource/'+DS_NAME+'/JDBCConnectionPoolParams/'+DS_NAME)
cmo.setTestTableName('SQL ISVALID\r\n\r\n')

cd('/JDBCSystemResources/'+DS_NAME+'/JDBCResource/'+DS_NAME+'/JDBCDriverParams/'+DS_NAME+'/Properties/'+DS_NAME)
cmo.createProperty('user')

cd('/JDBCSystemResources/'+DS_NAME+'/JDBCResource/'+DS_NAME+'/JDBCDriverParams/'+DS_NAME+'/Properties/'+DS_NAME+'/Properties/user')
cmo.setValue('TESTM')

cd('/JDBCSystemResources/'+DS_NAME+'/JDBCResource/'+DS_NAME+'/JDBCDataSourceParams/'+DS_NAME)
cmo.setGlobalTransactionsProtocol('OnePhaseCommit')

cd('/JDBCSystemResources/'+DS_NAME)
set('Targets',jarray.array([ObjectName('com.bea:Name=DefaultServer,Type=Server')], ObjectName))

save()
activate()
disconnect()
exit()

