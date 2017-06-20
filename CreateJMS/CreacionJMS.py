FS_NAME='FileStore9'
JMSServer_Name='JMSServer9'
Module_Name='SystemModule9'
CF_NAME='ConnectionFactory9'

connect('weblogic','123webfisi','t3://localhost:7101')
edit()
startEdit()
cd('/')

#********Creacion de JMS********

#Creacion de File Store
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
activate()
disconnect()
exit()


