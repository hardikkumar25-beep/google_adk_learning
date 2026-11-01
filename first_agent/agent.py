from google.adk.agents.llm_agent import LlmAgent

root_agent = LlmAgent(
    name="test_agent",
    model="gemini-flash-latest",
    instruction="You are a helpful assistant. Reply briefly to the user's message."
)