# ✈️ CrewAI Travel & Budget Planner Agent

A beginner-friendly AI agent built with **CrewAI** that takes a city name from the user, searches the web in real time using **SerperDevTool**, and generates a crisp, one-line travel cheat sheet with top attractions, local restaurants, and a 2-day budget estimate in INR (`₹`).

---

## ✨ Features
* **Live Web Search:** Uses `SerperDevTool` (Google Search API) to fetch up-to-date tourist spots, restaurant names, and local pricing.
* **Strict One-Line Formatting:** Enforces clean, numbered lists with zero fluff or long paragraphs.
* **Complete Travel Summary:**
  1. Top 3 must-visit places along with the best time to visit each.
  2. Top 3 local restaurants with a must-try dish at each.
  3. Estimated 2-day trip budget in Indian Rupees (`₹`) covering stay, food, and travel.
* **Secure Key Management:** Loads API keys safely from a `.env` file using `python-dotenv`.

---

## 🛠️ Tech Stack & Libraries
* **Python 3.10+**
* **CrewAI & CrewAI Tools** (`crewai[tools]`)
* **Python-Dotenv** (`python-dotenv`)
* **OpenAI API** (LLM backbone)
* **Serper API** (Google Search tool)

---

## 🚀 Setup & Installation

### 1. Clone or Open the Project Folder
Navigate to your project directory in Command Prompt:
```cmd
cd C:\Development\CrewAI_Practice
