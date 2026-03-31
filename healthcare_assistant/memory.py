from data import patients


def get_patient(patient_id: str):
    return patients.get(patient_id)


def get_patient_summary(patient_id: str):
    patient = get_patient(patient_id)

    if not patient:
        return "Patient not found."

    history_text = "; ".join(patient["history"])
    conditions_text = ", ".join(patient["conditions"])

    return (
        f"Name: {patient['name']}. "
        f"Age: {patient['age']}. "
        f"Conditions: {conditions_text}. "
        f"History: {history_text}."
    )