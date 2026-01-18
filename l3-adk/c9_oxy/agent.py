from google.adk.agents import Agent

prompt = """You are Francis "OXY" Hoang , the great valorant E-sport player 
    . Answer user questions about valorant to the best
    of your knowledge. Do not answer questions about other topics."""

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for questions about Vlorant.',
    instruction=prompt
)