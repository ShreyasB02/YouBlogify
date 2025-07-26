from crewai import Crew,Process
from agents import researcher, writer
from tasks import research_task, writer_task
from tools import yt_tool

crew=Crew (
    agents=[researcher, writer],
    tasks=[research_task, writer_task],
    process=Process.sequential,
    memory=True,
    max_rpm=100,
    share_crew=True,
    cache=True
    )

## Start Task Execution with feedback

result=crew.kickoff(inputs={'topic':'AI vs ML vs DL vs Data Science'})
print(result)