# Hadoop Setup
Setup hadoop > MasterNode or NameNode using python36 and bash script
>
> This setup uses: 
1. Python36
2. Bash


## Instruction
This hadoop setup helps you setup hadoop in your local system.
This hadoop setup has been tested in RHEL 7.5 , not sure if it will work on other linux.
You can test for other linux and give your feedback
>
>
**Regarding the setup_files/ folder**

_Please add_

    a) hadoop-1.2.1-1.x86_64.rpm
    b) jdk-8u171-linux-x64.rpm
    
_the above files in the setup_files/ directory and make sure the file name matches._


## How to use
>
  1.Make sure your to move **hadoop-1.2.1-1.x86_64.rpm** and **jdk-8u171-linux-x64.rpm** to _setup_files/_ directory
  
  2.Make sure the **install.sh** is executable
    
    if not executable:
    
      a) run > chmod +x install.sh
      
  3.Make sure pyhton36 is installed 
  
  4.Run the _install.sh as root user_
      
      ./install.sh


**Note: This hadoop setup is still in development phase, so it may create some problem. Please create an issue in issue section it will help us to build a great hadoop setup using bash and python36.**
