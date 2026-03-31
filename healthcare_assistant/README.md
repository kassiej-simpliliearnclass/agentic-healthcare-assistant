# Agentic Healthcare Assistant

This project is a simple healthcare assistant built with Python and Streamlit.

## Features

- Reviews patient history
- Plans tasks based on user request
- Books a mock appointment
- Summarizes treatment information

## Project Structure

- `data.py` - mock patient, doctor, and medical data
- `tools.py` - appointment booking and medical search functions
- `memory.py` - patient lookup and summary
- `planner.py` - task planning logic
- `agent.py` - main workflow
- `app.py` - Streamlit user interface

## How to Run

1. Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```
2. Run the app:
```bash
python3 -m streamlit run app.py
```
## Example Request

Book a nephrologist for my father and summarize the latest treatments.

## Notes

This is a starter version built for a healthcare assistant capstone project. It uses mock data and simple task planning.

## Example Output

User Input:
"Don’t book anything yet, but I do want to understand treatment options"

Planned Tasks:
- Search medical information

Result:
- Displays treatment summary without scheduling appointment