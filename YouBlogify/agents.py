from crewai import Agent
from tools import yt_tool
from ollama import Ollama
##Create a blog researchers
llm=Ollama.model('gpt-3.5-turbo')

researcher=Agent(
    role="Blog Researcher from YoutTube Videos ",
    goal="Get releavnt Youtube videos for the blog for the particular topic {topic}",
    name="Researcher",
    verbose=True,
    memory=True,
    backstory=('Expert in understanding GenAI, ML and DL concepts from Youtube videos'),
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm
    )  ##DEFAULT PARAMETERS



##Create a blog writers
writer=Agent(
    role="Blog Writer",
    goal='Write a blog on the topic {topic} with the information provided by the researcher',
    name="Writer",
    verbose=True,
    memory=True,
    backstory=('Expert in writing blogs on GenAI, ML and DL concepts'),
    tools=[yt_tool],
    allow_delegation=False
)
