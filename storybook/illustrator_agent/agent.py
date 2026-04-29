from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from .prompt import ILLUSTRATOR_DESCRIPTION, ILLUSTRATOR_INSTRUCTIONS
from .tools import generate_images
import dotenv
dotenv.load_dotenv()

MODEL = LiteLlm(model="openai/gpt-4o-mini")

illustrator_agent = Agent(
    name="illustrator_agent",
    description=ILLUSTRATOR_DESCRIPTION,
    instruction=ILLUSTRATOR_INSTRUCTIONS,
    model=MODEL,
    output_key="illustrator_output",
    tools=[generate_images,],
)

root_agent = illustrator_agent