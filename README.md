# Cloud_Migration
cicd migration


![run server](https://user-images.githubusercontent.com/126528702/224705255-269ed2d3-bbd7-45f7-9044-25f8eba6daa3.PNG)
![output](https://user-images.githubusercontent.com/126528702/224705386-a7da6902-1b4d-4b7a-88f1-cf53a6f343ab.PNG)
![working directory](https://user-images.githubusercontent.com/126528702/224744778-c2ae516d-207b-4d77-b140-398838a42b66.PNG)

Step 1:
Install into the pc , if you do not have already:
Docker, Jenkins, Python, gitbash, aws cli,vscode, 

Step 2:
setup an Api framework by installing Fastapi module on vscode terminal
Run : pip3 install fastapi and pip3 install uvicorn

Step 3:
create an api file as shown in my api.py 
run the live server with code uvicorn api:app --port 8081 and confirm output.
[run server](https://user-images.githubusercontent.com/126528702/224705255-269ed2d3-bbd7-45f7-9044-25f8eba6daa3.PNG)
[output](https://user-images.githubusercontent.com/126528702/224705386-a7da6902-1b4d-4b7a-88f1-cf53a6f343ab.PNG)

Step 4:
Create an ec2 on aws and start jenkins. 
create a new pipeline job on jenkins : testapi_job
setup a working directory : /var/lib/jenkins/workspace/testapi_job
create a folder with the working directory
create folders api.py and dockerfiler and paste the coreesponding codes
[working directory](https://user-images.githubusercontent.com/126528702/224744778-c2ae516d-207b-4d77-b140-398838a42b66.PNG) 

How to use:
=================
Go to Jenkins, setup the appropriate configuration. The build stages script can be copied from your aws ecr push command. Click on build now. App will be migrated to aws ecr.