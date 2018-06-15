import sys
import glob
import subprocess as sp
import os.path
from os import path
jdk_path = len(glob.glob('/usr/java/jdk1.8*'))
hadoop_path = len(glob.glob('/etc/hadoop/'))


print('|----------------------------|')
print('|   Welcome to HadoopSetup   |')
print('|----------------------------|')


print("""
What would you like to setup

1.Namenode /  Master  
2.Datanode / Slave

""")



#system_type = input('Enter your system type 1 or 2: ')


prefrence = input("Enter your prefrence 1 or 2: ")


if int(prefrence) == 1:
	print('Now we are going to setup masternode for you')
	print("""
	1.We are going to install below files for you:
	  a. JDK
`	  b. Hadoop
	
	2. We configure below hadoop files for you:
	   a.core-site.xml
       b.hdfs-site.xml
	""")
	check = input('Are your sure to continue Y/n: ')
	
	if check == 'Y':
		print('Setup started.....................')
		print('')
		print('')
		print('')
		
		
		#downloading jdk and
		#installing jdk 
		print('Installing jdk for your system')
		if jdk_path == 1:
			print(".........................")
			print('jdk already installed')
			print(sp.getoutput('rpm -q jdk1.8'))
		else:
			print('This setup can take some to time')
			print('You can have tea for a while :)')
			print('')
			print('')
			print('')
			try:
				print('Installing jdk starts.......')
				
				print("""
				
					     ,--. ,------.   ,--. ,--. 
					     |  | |  .-.  \  |  .'   / 
					,--. |  | |  |  \  : |  .   '  
					|  '-'  / |  '--'  / |  |\   \ 
					 `-----'  `-------'  `--' '--' 
				
				""")
				install_jdk = sp.check_output('rpm -ivh setup_files/jdk-8u171-linux-x64.rpm', shell=True)
				print(install_jdk)
			except sp.CalledProcessError as e:
				print('Unable to install :(')
				print('Error: ' + e)
				
			print("Adding JAVA_HOME path to .bashrc")
			java_path = "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/"
			sp.call("echo "+java_path+" >> ~/.bashrc", shell=True)
			
			#adding jdk path to .bashrc
			print("Adding jdk path")
			jdk_path = "export PATH=/usr/java/jdk1.8.0_171-amd64/bin:$PATH"
			sp.call("echo "+jdk_path+" >> ~/.bashrc", shell=True)	
			
					
		
		#installing hadoop
		#print('Installing Hadoop')		
		if hadoop_path == 1:
			print('Hadoop already installed')
			print('')
			print('Hadoop version')
			print(sp.getoutput('rpm -q hadoop'))
			
		else:
			print('Installing hadoop starts.......')
			print('')
			print("""
			
						
		@@@@@*                        @@@@@      
               ,@&**&                        @@(**@                                                
               @@**********@**********@@*********,@*********(@/********,@**********@               
              .@@**&@@@@***@@@@@@@@/**%***@@@@&**&***&@@@%******#@@@&***&**&@@@&***@               
              @@***&  @@**//**********(**@  @@***/**@  &@&**&**(   @@******@  @@**(.               
              @@**#  @@(**@**(@@@@@**/***@#%@&**&***#//@@***/**@//&@#**@**(//@@***@                
             &@***@  @@***%**********@**********@**********@,********************#                 
                                                                     @@***                         
                                                                    &@#**@                         
                                                             .                                     
                                                  .(   @@@* .....@@                                
                                                    @@   ...........@&                             
                                                  #@ .,. ............*#@.                          
                                               @@ ......................*@/   @@@*                 
                                         &@@@@@ ..&@,.......#............#%@@&,*.@.                
                                     &@%    @  ..(,,........,...#@,......@@......*@                
                           *  @@   @@     @%  ..(,.....,......%@*@&....&.@/,.....*@                
                            @ @@ &@   ...@  ...........%........,.....*.(........*@,               
                         . #,,@ @&  ....@  ............@,.................#......*@.               
                            &*,,& ......@ .............@*........................*@                
                               @  ......,@/.@..........&/.......................*@.                
                               @ ........,&@...........@*,.......*............,*@.                 
                               @ .........@.........@@@/*,.#......@@@@&/****(@@                    
                               @%..........@&...&@****......**@*..@@@&&.                           
                             .@,@.............,,...........,*@@ @@..(@                             
                            @#..*@.........,...............**#/@                                   
                            *@...*@........#..,,**(.......**@**@                                   
                              @@***@......,#/  @@(.......*/@***@                                   
                                  @*.....*/@  /@......,**@/****                                  
                                 ,@....,**@    %@,,***#@*  ....                                    
                                    %@@@@@@      @#*(@. 
						
						
			""")
			try:
				install_hadoop = sp.check_output('rpm -ivh setup_files/hadoop-1.2.1-1.x86_64.rpm --force', shell=True)
				print(install_hadoop)
				
				#setting up files for hadoop
				print("Setting up hadoop files")
				print("")
				print("Setting up core-site.xml for hadoop")
				file = open("setup_files/hadoop/core-site.xml","w") 
				ip = input("Enter master node ip: ")
				
				file.write(
				"""
				<?xml version=\"1.0\"?> 
				\n <?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?> 
				\n <!-- Put site-specific property overrides in this file. -->
				\n <configuration> 
				\n <property>
				\n <name>fs.default.name</name>
				\n <value>hdfs://"+ip+":9001</value>
				\n </property>
				\n </configuration>
				"""
				)

				file.close()
				
				
				
				
				print("Setting up hdfs-site.xml for hadoop")
				file = open("setup_files/hadoop/hdfs-site.xml","w") 
				file.write(
				"""
				<?xml version=\"1.0\"?>
				\n <?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?> 
				\n <!-- Put site-specific property overrides in this file. --> 
				\n <configuration> 
				\n <property>
				\n <name>dfs.namenode.dir</name>
				\n <value>/nn</value>
				\n </property>
				\n </configuration>
				"""
				) 
				file.close()
				
				#creating /nn dir for master node/name node
				print(sp.call("mkdir /nn", shell=True))
				
				#fromate the directory
				print(sp.call("hadoop namenode -format", shell=True))
				
								
				
			except sp.CalledProcessError as e:
				print('Unable to install :(')
				print('Error: ' + e)
		
		
	
		#start the hadoop namenode
		print("Starting hadoop namenode") 
		print(sp.call("hadoop-daemon.sh start namenode", shell=True))
		print("Hadoop Namenode running!!!")
		print(sp.getoutput("jps"))
		print('')
		print('')
		print('')
		print('Visit for Namenode Web UI')
		print('http://localhost:50070')

if int(prefrence) == 2:
	print('Lets setup namenode :)')

