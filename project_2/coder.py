from llm import llm
from state import AgentState

PROMPT = "Generate a simple HTML page with inline CSS for styling and JavaScript for interactivity and animation for {}"

def coder(state: AgentState):
    result = llm.invoke(PROMPT.format(state['request']))
    print("Code Generated Succesfully")
    return {"code": result.content}