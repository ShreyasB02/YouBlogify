from crewai import Agent, Task, Crew,Process
from tools import yt_tool
import boto3
import json

# Initialize AWS Clients
s3 = boto3.client("s3")
bedrock = boto3.client("bedrock-runtime")

# Function to invoke Bedrock LLM
def invoke_bedrock_llm(prompt):
    response = bedrock.invoke_model(
        modelId="meta.llama2B-v2",
        body=json.dumps({"prompt": prompt})
    )
    return response["body"].read().decode()

# Define Researcher Agent
researcher = Agent(
    role="Blog Researcher from YouTube Videos",
    goal="Get relevant YouTube videos for the blog topic {topic}",
    name="Researcher",
    verbose=True,
    memory=True,
    backstory='Expert in understanding GenAI, ML, and DL concepts from YouTube videos.',
    tools=[yt_tool],
    allow_delegation=True,
    llm=invoke_bedrock_llm
)

# Define Writer Agent
writer = Agent(
    role="Blog Writer",
    goal="Write a blog on the topic {topic} with the information provided by the researcher",
    name="Writer",
    verbose=True,
    memory=True,
    backstory='Expert in writing blogs on GenAI, ML, and DL concepts.',
    tools=[yt_tool],
    allow_delegation=False,
    llm=invoke_bedrock_llm
)

# Define Research Task
research_task = Task(
    task_name="Research Task",
    description=("Get relevant YouTube videos for the topic {topic} "
                 "and retrieve detailed information about the videos from the channel."),
    agent=researcher,
    tools=[yt_tool],
    expected_output="A comprehensive three-paragraph report based on the {topic} of video content."
)

# Define Writing Task
writer_task = Task(
    task_name="Write Task",
    description="Write a 1000-word blog on the topic {topic} using the information provided by the researcher.",
    agent=writer,
    tools=[yt_tool],
    expected_output="A 1000-word blog on {topic} based on the researcher's findings.",
    async_execution=False,
    output_file="blog.md"
)

# Define Crew Orchestration
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writer_task],
    process=Process.sequential,
    cache=True
)

# AWS Lambda Handler
def lambda_handler(event, context):
    topic = event.get("queryStringParameters", {}).get("topic", "default topic")
    result = crew.kickoff()
    
    # Store the generated blog in S3
    bucket_name = "your-s3-bucket"
    s3.put_object(Bucket=bucket_name, Key=f"blogs/{topic}.md", Body=result)
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Blog created successfully!", "topic": topic})
    }

# Execute Locally for Testing
if __name__ == "__main__":
    test_event = {"queryStringParameters": {"topic": "AI in Healthcare"}}
    print(lambda_handler(test_event, None))
