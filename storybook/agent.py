from google.adk.agents import SequentialAgent
from .story_writer_agent.agent import story_writer_agent
from .illustrator_agent.agent import illustrator_agent

root_agent = SequentialAgent(
    name="storybook_pipeline",
    description="Runs story writing and illustration in order.",
    sub_agents=[
        story_writer_agent,   
        illustrator_agent,  
    ],
)