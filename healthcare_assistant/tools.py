from data import doctors, medical_knowledge


def find_doctor_by_specialty(specialty: str):
    for doctor in doctors:
        if doctor["specialty"].lower() == specialty.lower():
            return doctor
    return None


def book_appointment(specialty: str):
    doctor = find_doctor_by_specialty(specialty)
    if not doctor:
        return {"success": False, "message": "No doctor found for that specialty."}

    if not doctor["slots"]:
        return {"success": False, "message": "No slots available."}

    slot = doctor["slots"].pop(0)

    return {
        "success": True,
        "doctor": doctor["name"],
        "specialty": doctor["specialty"],
        "slot": slot
    }


def search_medical_info(condition: str):
    results = medical_knowledge.get(condition.lower(), [])
    if not results:
        return ["No medical information found."]
    return results