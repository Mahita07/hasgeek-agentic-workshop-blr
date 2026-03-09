from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class EnergyState(TypedDict):
    input: str
    energy_level: str
    response: str

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

def detect_energy_level(state: EnergyState):
    prompt = f"""
    Analyze the following message and classify the user's energy level.
    Only return one word strictly from the following options:
    - low
    - medium
    - high

    Message: "{state['input']}"
    """
    
    result = llm.invoke(prompt).content.strip().lower()
            
    state["energy_level"] = result
    return state

def low_energy_node(state: EnergyState):
    state["response"] = "It sounds like you have low energy. You should take a nap or maybe Netflix and chill 🛋️😴"
    return state

def medium_energy_node(state: EnergyState):
    state["response"] = "You have medium energy! Going for a walk or reading a good book might be perfect for you right now 🚶‍♂️📚"
    return state

def high_energy_node(state: EnergyState):
    state["response"] = "High energy! That's awesome! You should definitely go for a run, hit the gym, or play a sport 🏃‍♂️⚽🔥"
    return state

def route_energy(state: EnergyState):
    return state["energy_level"]

# Build the graph
builder = StateGraph(EnergyState)

# Add nodes
builder.add_node("detect_energy_level", detect_energy_level)
builder.add_node("low", low_energy_node)
builder.add_node("medium", medium_energy_node)
builder.add_node("high", high_energy_node)

# Set entry point
builder.set_entry_point("detect_energy_level")

# Add conditional edges
builder.add_conditional_edges(
    "detect_energy_level",
    route_energy,
    {
        "low": "low",
        "medium": "medium",
        "high": "high",
    },
)

# Add edges to END
builder.add_edge("low", END)
builder.add_edge("medium", END)
builder.add_edge("high", END)

# Compile graph
graph = builder.compile()

if __name__ == "__main__":
    print("-" * 50)
    print("Welcome to the Weekend Activity Recommender!")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nHey how are you feeling today? (or type 'quit' to exit): ")
            if user_input.strip().lower() in ['quit', 'exit', 'q']:
                break
                
            if not user_input.strip():
                continue
                
            print("\nProcessing...")
            result = graph.invoke({"input": user_input})
            
            print(f"Detected Energy Level: [{result['energy_level'].upper()}]")
            print(f"Recommendation: {result['response']}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            break
