import boto3
import botocore
import os
from dotenv import load_dotenv
import json

load_dotenv()
boto3.setup_default_session(profile_name=os.getenv('profile_name'))


def kendraSearch(question):
    kendra = boto3.client('kendra')
    kendra_response = kendra.retrieve(
        IndexId=os.getenv('kendra_index'),  # Put INDEX in .env file
        QueryText=question,
        PageNumber=1,
        PageSize=15
    )
    return invokeLLM(question, kendra_response)


def invokeLLM(question, kendra_response):
    # Setup Bedrock client
    bedrock = boto3.client('bedrock', 'us-east-1', endpoint_url='https://bedrock.us-east-1.amazonaws.com')

    modelId = 'anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'

    prompt_data = f"""
Human:    
Answer the following question to the best of your ability based on the context provided.
Provide an answer and provide sources and the source link to where the relevant infomration can be found. Include this at the end of the response
Do not include information that is not relevant to the question.
Only provide information based on the context provided, and do not make assumptions
Only Provide the source if relevant information came from that source in your answer
Use the provded exmaples as reference
###
Question: {question}

Context: {kendra_response}
###

Assitant:

"""
    body = json.dumps({"prompt": prompt_data,
                       "max_tokens_to_sample": 8191,
                       "temperature": 0,
                       "top_k": 250,
                       "top_p": 0.5,
                       "stop_sequences": []
                       })
    response = bedrock.invoke_model(body=body,
                                    modelId=modelId,
                                    accept=accept,
                                    contentType=contentType)

    response_body = json.loads(response.get('body').read())
    answer = response_body.get('completion')
    return answer
