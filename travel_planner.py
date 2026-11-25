import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

# 1. Load API keys from the .env file automatically
load_dotenv()

# 2. Initialize the Search Tool
search_tool = SerperDevTool()

# 3. Create a Concise Travel Planner Agent
travel_planner = Agent(
    role="Concise Travel & Budget Planner",
    goal="Provide ultra-short, numbered one-line recommendations for places with best visiting times, restaurants, food to try, and trip cost in {city}.",
    backstory=(
        "You are a direct, no-fluff travel assistant. You never write long paragraphs. "
        "You only provide exact names, best times to visit, must-try dishes, and clear Rupee costs in numbered one-line lists."
    ),
    tools=[search_tool],
    verbose=True
)

# 4. Give Strict Numbered One-Line Formatting Instructions
complete_plan_task = Task(
    description=(
        "Search online for {city} and list ONLY the following details in strict numbered one-line format (no descriptions or paragraphs):\n"
        "1. Places to Visit: Top 3 place names numbered 1 to 3, along with the single best time/season or time of day to visit each.\n"
        "2. Restaurants & Food: Top 3 restaurant names numbered 1 to 3, along with 1 must-try dish at each.\n"
        "3. Estimated Cost: A single one-line total estimated cost in INR (₹) for a 2-day trip."
    ),
    expected_output=(
        "Strictly follow this exact ultra-short numbered format with zero extra text:\n"
        "City: {city}\n\n"
        "Places to Visit in {city}:\n"
        "1. [Place 1 Name] - Best time to visit: [Best Time/Season]\n"
        "2. [Place 2 Name] - Best time to visit: [Best Time/Season]\n"
        "3. [Place 3 Name] - Best time to visit: [Best Time/Season]\n\n"
        "Restaurants & Must-Try Food in {city}:\n"
        "1. [Restaurant 1 Name] - Try: [Dish Name]\n"
        "2. [Restaurant 2 Name] - Try: [Dish Name]\n"
        "3. [Restaurant 3 Name] - Try: [Dish Name]\n\n"
        "Estimated Cost for {city}: ₹[Total Amount] for 2 days (Stay + Food + Travel)"
    ),
    agent=travel_planner
)

# 5. Assemble the Crew
travel_crew = Crew(
    agents=[travel_planner],
    tasks=[complete_plan_task],
    verbose=True
)

# 6. Get City from User & Kickoff
user_city = input("Enter the city name you want to visit: ")

print(f"\nFetching quick travel highlights for {user_city}...\n")
result = travel_crew.kickoff(inputs={"city": user_city})

print(f"\n================ QUICK TRAVEL SUMMARY: {user_city.upper()} ================\n")
print(result)