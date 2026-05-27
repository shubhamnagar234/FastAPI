# How to Deploy a FastAPI API on AWS 

## Steps for Deployment
- **Step 1**. Create an EC2 instance
- **Step 2**. Connect to the EC2 intance
- **Step 3**. Run the following commands
    - sudo apt-get update
    - sudo apt-get install -y docker.io
    - sudo systemcti start docker
    - sudo systemcti enable docker
    - sudo usermod -aG docker $USER
    - exit
- **Step 4**. Restart a new connection to EC2 instance
- **Step 5**. Run the following commands
    - docker pull your-docker-username/your-docker-reponame:latest
    - docker run -p 8080:8080 your-docker-username/your-docker-reponame:latest
- **Step 6**. Change the security group settings
- **Step 7**. Check the API