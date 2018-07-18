Using this tool all developers, developer apps and Users can be migrated from one server to another.
For Users to migrate the users should be present in OpenLdap or atleast in one organization of the same Setup.

Procedure to use the tool.

1. run the command 
	java -jar APIGEE_MIGRATION_PAJ.jar
	
	ener the asked inputs further 
	
	a. managemnet api uri : enter management url from http till .com  or management IP with port
		eg : http://xyz.com  	or 		http://xxx.xxx.xxx.xxx:8080
	
	b. basic Authorization : enter the basic Uthorization of the SysAdmin including Basic 
		eg : Basic xxxxxxxxxxxxxxxxxxxxxxxxxxx
	c. organization name : enter organization details
		eg : production
	
	Note : Old is the one from which the data will be migrated
		   New is the one to whcih the data will be migrated
	
	