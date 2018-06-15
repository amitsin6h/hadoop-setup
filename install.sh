#!/bin/sh


#check for internet connection
echo "Checking for internet connection"
wget -q --tries=10 --timeout=20 --spider http://google.com
if [[ $? -eq 0 ]]; then
	echo "Online"
    	echo ""
    	rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
	if [[ $? -eq 0 ]]; then
		echo OK
		
		#Install epel-release rpm:
		yum repolist

		#Install python36 rpm package:
		yum install python36
		
		#check if python36 installed
		rpm -q python36
		if [ $? -eq 0 ]; then
			echo "Python36 succesfully installed"
			echo OK
			
			#if python36 installed we will run the 
			#python36 script to setup_hadoop
			echo "Checking for httpd package......" 
			rpm -q httpd
			if [ $? -eq 0 ]; then
				echo "........................................."
				echo OK
				echo "Looks good your system has httpd installed :)"
		
				#start httpd service
				echo "We are going to start, httpd service"
				systemctl start httpd
		
				#if installed and httpd running
				#we will run python36 script to 
				#setup_hadoop for client
	
				#run python36 to setup_hadoop
				python36 setup_hadoop.py
	
			else
				echo FAIL
				echo "Oops!! We have detected your system does not have httpd installed"
				echo "..........................................."
				echo "We will install httpd package for you. Chill!!"
				#installing httpd 
				yum install httpd
				echo "Successfully installed.."
				rpm -q httpd
	
				#start httpd service
				echo "We are going to start, httpd service"
				systemctl start httpd
		
				#if installed and httpd running
				#we will run python36 script to 
				#setup_hadoop for client
	
				#run python36 to setup_hadoop
				python36 setup_hadoop.py
			fi
			
		else
			echo FAIL
			echo "Python36 not installed"
		fi
		
	else
		echo FAIL
		echo "yum failed"
		echo "going to run yum clone......"
		sudo yum clean
		sudo rm -f /var/lib/rpm/__db*
		sudo rpm --rebuilddb
		
		
		
		#once cleaned it will run the below script
		
		#Install epel-release rpm:
		yum repolist

		#Install python36 rpm package:
		yum install python36
		
		#check if python36 installed
		rpm -q python36
		if [ $? -eq 0 ]; then
			echo "Python36 succesfully installed"
			echo OK
			
			#if python36 installed we will run the 
			#python36 script to setup_hadoop
			echo "Checking for httpd package......" 
			rpm -q gedit
			if [ $? -eq 0 ]; then
				echo "........................................."
				echo OK
				echo "Looks good your system has httpd installed :)"
		
				#start httpd service
				echo "We are going to start, httpd service"
				systemctl start httpd
		
				#if installed and httpd running
				#we will run python36 script to 
				#setup_hadoop for client
	
				#run python36 to setup_hadoop
				python36 setup_hadoop.py
	
			else
				echo FAIL
				echo "Oops!! We have detected your system does not have httpd installed"
				echo "..........................................."
				echo "We will install httpd package for you. Chill!!"
				#installing httpd 
				yum install httpd
				echo "Successfully installed.."
				rpm -q httpd
	
				#start httpd service
				echo "We are going to start, httpd service"
				systemctl start httpd
		
				#if installed and httpd running
				#we will run python36 script to 
				#setup_hadoop for client
	
				#run python36 to setup_hadoop
				python36 setup_hadoop.py
			fi
			
		else
			echo FAIL
			echo "Python36 not installed"
		fi
	fi
	
else
	echo "Offline"
fi
