from planner import plan_tasks
from memory import get_patient_summary, get_patient
from tools import book_appointment, search_medical_info


def run_agent(user_input: str, patient_id: str = "father_001"):
    tasks = plan_tasks(user_input)
    patient = get_patient(patient_id)

    if not patient:
        return {
            "patient_summary": "Patient not found.",
            "tasks": [],
            "results": []
        }

    patient_summary = get_patient_summary(patient_id)
    results = []

    for task in tasks:
        if task == "book_appointment":
            booking_result = book_appointment("nephrologist")
            results.append({
                "task": "Appointment Booking",
                "output": booking_result
            })

        elif task == "search_medical_info":
            condition = patient["conditions"][0]
            info = search_medical_info(condition)
            results.append({
                "task": "Medical Information Search",
                "output": info
            })

    return {
        "patient_summary": patient_summary,
        "tasks": tasks,
        "results": results
    }