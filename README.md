# Serverless Flask Application on AWS Lambda + DynamoDB
This an example of simple flask application that runs on AWS Lambda and writes data to AWS DynamoDB table after POST request.

# Installation
Firstly, clone the repo.

Then, you need to have installed Serverless framework locally using _npm_:
```
npm install --save-dev serverless-wsgi serverless-python-requirements
```

Setup virtual environment inside the root of the clonned repo:
```
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

# Deployment tips
To deploy your application on AWS, you need to have AWS account with roles and user setup for Serverless.

After that, you can execute:
```
sls deploy
```

# How to run DynamoDB locally
Install additional Serverless plugin for DynamoDB emulation:
```
npm install --save-dev serverless-dynamodb-local
sls dynamodb install
```

Run the DynamoDB emulator:
```
sls dynamodb start
```

And also run the Serverless application in separate terminal window:
```
sls wsgi serve
```
