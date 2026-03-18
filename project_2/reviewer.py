from llm import llm
from state import AgentState

PROMT="Review the following html code for any errors or improvements.\n\n{}"

def reviewer(state:AgentState):
    result=llm.invoke(PROMT.format(state["code"]))
    print("Code reviewed successfully")
    return{"review": result.content}