from crewai import Task
from tools import yt_tool
from agents import researcher, writer

research_task=Task(
    task_name="Research Task",
    description=("Get releavnt Youtube videos for the topic {topic}"
                 "And get detailed information about the videos from the channel"),
    agents=researcher,
    tools=[yt_tool],
    expected_output="A comprehensive 3 paragraph long report based on the {topic} of video content ",
  
    )


writer_task=Task(
    task_name="Write Task",
    description=("Write a blog on the topic {topic} with the information provided by the researcher"),
    agents=writer,
    tools=[yt_tool],
    expected_output="A 1000 word blog on the {topic} with the information provided by the researcher",
    async_execution=False,
    output_file="blog.md"
)