import boto3
import botocore.config
import json
from datetime import datetime
def blog_generate_using_bedrock(blogtopic)->str:
    prompt=f'''
    <s>[INST]Human:Write a 200 words Blog on the topic {blogtopic}
    Assistant:/INST]

    '''
    body={
        "prompt":prompt,
        "max_gen_len":512,
        'temperature':0.5,
        'top_p':0.9
    }

    try:
        bedrock=boto3.client(service_name='bedrock-runtime',config=botocore.config.Config(read_timeout=300,retries={'max_attempts':3}))
        response=bedrock.invoke_model(json.dumps(body),modelId="meta.llama3-8b-instruct-v1:0")
        response_content=response.get('body').read()
        response_text=json.loads(response_content)
        blog_details=response_text['generation']
        return blog_details
    except Exception as e:
        print("Error",e)
        return " "

def save_blog_details_s3(s3_key,s3_bucket,generate_blog):
    s3=boto3.client('s3')
    try:
        s3.put_object(Bucket=s3_bucket,Key=s3_key,Body=generate_blog)
        print("Code saved to S3")
    except Exception as e:
        print("Error when savig file to s3")

    

## LAMBDA TO BEDROCK
def lambda_handler(event, context):
    # TODO implement
    event=json.loads(event['body'])
    blogtopic=event['blog_topic']

    generate_blog=blog_generate_using_bedrock(blog_topic=blogtopic)

    if generate_blog:
        ##Save into txt file in S3
        current_time=datetime.now()
        s3_key=f"blog-output/{current_time}.txt"
        s3_bucket='aws_bedrock_c1'
        save_blog_details_s3(s3_key,s3_bucket,generate_blog)
    else:
        print("No blog generated")
    return
    {
        'statusCode':200,
        'body':json.dumps("Blog Gen is Completed")

    }