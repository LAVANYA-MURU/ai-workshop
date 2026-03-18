import os
from state import AgentState

def saver(state: AgentState):
    folder="output"
    os.makedirs(folder,  exist_ok=True)
    with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
        f.write(state["code"])
    print("Code saved successfully")
    return state