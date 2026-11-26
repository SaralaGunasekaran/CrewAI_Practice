# ✈️ CrewAI Travel & Budget Planner Agent

A beginner-friendly AI agent built with **CrewAI** and OpenAI's **`gpt-4.1-mini`** model that takes a city name from the user and generates a crisp, numbered one-line travel cheat sheet with top attractions, local restaurants, and a 2-day budget estimate in INR (`₹`).

---

## ✨ Features
* **Powered by `gpt-4.1-mini`:** Uses CrewAI's `LLM` integration with OpenAI's `gpt-4.1-mini` chat model for fast, accurate travel recommendations.
* **Strict One-Line Numbered Formatting:** Enforces clean, numbered lists (`1.`, `2.`, `3.`) with zero fluff or long paragraphs.
* **Complete Travel Summary:**
  1. Top 3 must-visit places along with the single best time/season to visit each.
  2. Top 3 local restaurants with a must-try dish at each.
  3. Estimated 2-day trip budget in Indian Rupees (`₹`) covering stay, food, and travel.
* **Secure Key Management:** Loads your OpenAI API key safely from a `.env` file using `python-dotenv`.

---

## 🛠️ Tech Stack & Libraries
* **Python 3.10+**
* **CrewAI** (`crewai`)
* **Python-Dotenv** (`python-dotenv`)
* **OpenAI API** (`openai/gpt-4.1-mini`)

---

## 🚀 Setup & Installation

### 1. Open the Project Folder
Navigate to your project directory in Command Prompt:
```cmd
cd C:\Development\CrewAI_Practice

