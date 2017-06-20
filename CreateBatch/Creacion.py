import sys
#DS_NAME='jdbc/DSFISI23'
#FS_NAME='FileStore23'
#JMSServer_Name='JMSServer24'
#Module_Name='SystemModule23'
#CF_NAME='ConnectionFactory23'
#Queue_Name='Queue23'

#print 'Argument List:', str(sys.argv)

argList= sys.argv

DS_NAME=argList[2]
FS_NAME=argList[3]
JMSServer_Name=argList[4]
Module_Name=argList[5]
CF_NAME=argList[6]
Queue_Name=argList[7]

#for i in argList:
#    print i
	 
		
		 
connect('weblogic','123webfisi','t3://localhost:7101')
#*********CREACION DE DATA SOURCE********

#DS_NAME='jdbc/DSFISI19'

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


#*************CREACION DE JMS**********************

#FS_NAME='FileStore21'
#JMSServer_Name='JMSServer21'
#Module_Name='SystemModule21'
#CF_NAME='ConnectionFactory21'



#Creacion de File Store
cd('/')
cmo.createFileStore(FS_NAME)
cd('/FileStores/'+FS_NAME)
set('Targets',jarray.array([ObjectName('com.bea:Name=DefaultServer,Type=Server')], ObjectName))

#Creacion de JMSServer
cd('/')
cmo.createJMSServer(JMSServer_Name)

cd('/JMSServers/'+JMSServer_Name)
cmo.setPersistentStore(getMBean('/FileStores/'+FS_NAME))
set('Targets',jarray.array([ObjectName('com.bea:Name=DefaultServer,Type=Server')], ObjectName))

#Creacion de Module Name
cd('/')
cmo.createJMSSystemResource(Module_Name)

cd('/JMSSystemResources/'+Module_Name)
set('Targets',jarray.array([ObjectName('com.bea:Name=DefaultServer,Type=Server')], ObjectName))


#Creacion de ConnectionFactories
cmo.createSubDeployment(CF_NAME)

cd('/JMSSystemResources/'+Module_Name+'/JMSResource/'+Module_Name)
cmo.createConnectionFactory(CF_NAME)

cd('/JMSSystemResources/'+Module_Name+'/JMSResource/'+Module_Name+'/ConnectionFactories/'+CF_NAME)
cmo.setJNDIName('jdbc/'+CF_NAME)

cd('/JMSSystemResources/'+Module_Name+'/JMSResource/'+Module_Name+'/ConnectionFactories/'+CF_NAME+'/SecurityParams/'+CF_NAME)
cmo.setAttachJMSXUserId(false)

cd('/JMSSystemResources/'+Module_Name+'/JMSResource/'+Module_Name+'/ConnectionFactories/'+CF_NAME+'/ClientParams/'+CF_NAME)
cmo.setClientIdPolicy('Restricted')
cmo.setSubscriptionSharingPolicy('Exclusive')
cmo.setMessagesMaximum(10)

cd('/JMSSystemResources/'+Module_Name+'/JMSResource/'+Module_Name+'/ConnectionFactories/'+CF_NAME+'/TransactionParams/'+CF_NAME)
cmo.setXAConnectionFactoryEnabled(true)

cd('/JMSSystemResources/'+Module_Name+'/SubDeployments/'+CF_NAME)
set('Targets',jarray.array([ObjectName('com.bea:Name='+JMSServer_Name+',Type=JMSServer')], ObjectName))

cd('/JMSSystemResources/'+Module_Name+'/JMSResource/'+Module_Name+'/ConnectionFactories/'+CF_NAME)
cmo.setSubDeploymentName(CF_NAME)

save()


#***********CREACION DE QUEUE*****************

#Queue_Name='Queue19'

cd('/')
cd('/JMSSystemResources/'+Module_Name+'/JMSResource/'+Module_Name)
cmo.createQueue(Queue_Name)

cd('/JMSSystemResources/'+Module_Name+'/JMSResource/'+Module_Name+'/Queues/'+Queue_Name)
cmo.setJNDIName('jdbc/'+Queue_Name)
cmo.setSubDeploymentName(CF_NAME)

cd('/JMSSystemResources/'+Module_Name+'/SubDeployments/'+CF_NAME)
set('Targets',jarray.array([ObjectName('com.bea:Name='+JMSServer_Name+',Type=JMSServer')], ObjectName))

save()


activate()
disconnect()
exit()





