# Amazon-Bedrock-RAG-Kendra-POC
This is sample code demonstrating the use of Amazon Bedrock and Generative AI to implement a RAG based architecture with Amazon Kendra. The application is constructed with a simple streamlit frontend where users can ask questions against documents stored in Amazon Kendra.

# **Goal of this Repo:**
The goal of this repo is to provide users the ability to use Amazon Bedrock and generative AI to take natural language questions, and answer questions against indexed documents in Amazon Kendra.
This repo comes with a basic frontend to help users stand up a proof of concept in just a few minutes.

# How to use this Repo:

## Step 1:
The first step of utilizing this repo is performing a git clone of the repository.

```
git clone https://github.com/aws-rdoty/Amazon-Bedrock-RAG-Kendra-POC.git
```

After cloning the repo onto your local machine, open it up in your favorite code editor.The file structure of this repo is broken into 3 key files,
the app.py file, the kendra_bedrock_query.py file, and the requirements.txt. The app.py file houses the frontend application (a streamlit app). The kendra_bedrock_query.py file houses the logic of the application, including the Kendra Retrieve API calls and Amazon Bedrock API invocations.

## Step 2:
Set up a python virtual environment, and ensure that you are using Python 3.9. The virtual environment will be extremely useful when you begin installing the requirements.
After the virtual environment is created, ensure that it is activated, following the activation steps of the environment tool you are using. Likely:
```
source venv/bin activate 
```
or
```
conda activate myenv
```
After your virtual environment has been created and activated, you can install all of the requirements found in the requirements.txt file by running this command in your terminal:
```
pip install -r requirements.txt
```

## Step 3:
Now that all of the requirements have been successfully installed in your virtual environment we can begin configuring environment variables.
You will first need to create a .env file in the root of this repo. Within the .env file you just created you will need to configure the .env to contain:

```
profile_name=<aws_cli_profile_name>
kendra_index=<kendra_index>
```
Please ensure that your AWS CLI Profile has access to Amazon Bedrock!

Depending on the region and model that you are planning to use Amazon Bedrock in, you may need to reconfigure line 44 & 46 in the kendra_bedrock_query.py file:

```
bedrock = boto3.client('bedrock', 'us-east-1', endpoint_url='https://bedrock.us-east-1.amazonaws.com')

modelId = 'anthropic.claude-v2'
```