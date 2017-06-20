Module_Name='SystemModule9'
Queue_Name='Queue16'
CF_NAME='ConnectionFactory9'
JMSServer_Name='JMSServer9'

connect('weblogic','123webfisi','t3://localhost:7101')
edit()
startEdit()

cd('/JMSSystemResources/'+Module_Name+'/JMSResource/'+Module_Name)
cmo.createQueue(Queue_Name)

cd('/JMSSystemResources/'+Module_Name+'/JMSResource/'+Module_Name+'/Queues/'+Queue_Name)
cmo.setJNDIName('jdbc/'+Queue_Name)
cmo.setSubDeploymentName(CF_NAME)

cd('/JMSSystemResources/'+Module_Name+'/SubDeployments/'+CF_NAME)
set('Targets',jarray.array([ObjectName('com.bea:Name='+JMSServer_Name+',Type=JMSServer')], ObjectName))

activate()
startEdit()