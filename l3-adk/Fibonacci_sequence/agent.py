from google.adk.agents import Agent

def verify_fibonacci_sequence(fibonacci: str) -> bool:
    """What is the 77th number in the Fibonacci sequence, assuming the sequence starts with F(0)=0 and F(1)=1?."""
    return fibonacci == '3,416,454,622,906,707'

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[verify_fibonacci_sequence]
)