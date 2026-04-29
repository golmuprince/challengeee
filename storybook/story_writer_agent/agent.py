from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field
from typing import List
from .prompt import STORY_WRITER_DESCRIPTION, STORY_WRITER_INSTRUCTIONS


class StoryPage(BaseModel):
    page_no: int = Field(description="Page number")
    text: str = Field(description="Korean story text for this page")
    visual_desc: str = Field(description="English scene description for image generation")

class StoryOutput(BaseModel):
    pages: List[StoryPage]


MODEL = LiteLlm(model="openai/gpt-4o-mini")

story_writer_agent = Agent(
    name="story_writer_agent",
    description=STORY_WRITER_DESCRIPTION,
    instruction=STORY_WRITER_INSTRUCTIONS,
    model=MODEL,
    output_schema=StoryOutput,
    output_key="story_writer_output",
)

root_agnet= story_writer_agent