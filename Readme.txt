 Below are the instructions which needs to be performed for successful execution of docker container and run script inside it to get "Rotten Tomatoes" value of any movie if it exists
1. Install git 
    # yum install git

2. Run git clone command
 
   # git clone https://github.com/Nitin-1994/API.git
The above command will clone the public repo on host linux machine and "API" folder will get created at current path after it's successful execution

3. Enter into "API" directory using below command
   
    # cd API/

4. Now run "docker.sh" using below command
   # "./docker.sh" or "sh docker.sh"

After the successful execution of above command, we will be inside docker container. The script mentioned in above command pull docker image from docker hub, create container and execute bash.

5. Now run python script inside docker container and input movie whose ratings we need.
   
   # python /var/tmp/Rotten_Tomatoes.py <Movie-Name>
   
   example:-
   python /var/tmp/Rotten_Tomatoes.py zero dark thirty

######################
Notes:-
--- In case we want to get out of container we will type "exit" on shell

--- To get inside container run below command

       docker exec -it <container-name> bash

