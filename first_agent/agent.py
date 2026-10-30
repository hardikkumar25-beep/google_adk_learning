from google.adk import Agent
from datetime import date
from pydantic import Field,BaseModel

class TodoItem(BaseModel):
    task: str = Field(description="Task name")
    due_date: date = Field(description="YYYY-MM-DD format")
    priority: str = Field(description="low/medium/high")

todo_agent = Agent(
    model='gemini-3.5-flash',
    name='todo_agent',
    instruction='Generate todo items in exact JSON format',
    output_schema=TodoItem,
    output_key="todo"
)

