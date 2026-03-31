import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Healthcare Assistant", layout="wide")

st.title("Agentic Healthcare Assistant")
st.write("This assistant can review patient history, plan tasks, book appointments, and summarize treatment information.")

st.info("Try a request like: Book a nephrologist for my father and summarize the latest treatments.")

user_input = st.text_area("Enter your request:", "")

task_labels = {
    "book_appointment": "Book appointment",
    "search_medical_info": "Search medical information"
}

if st.button("Run Assistant"):
    if not user_input.strip():
        st.warning("Please enter a request first.")
    else:
        response = run_agent(user_input)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Patient Summary")
            st.write(response["patient_summary"])

            st.subheader("Planned Tasks")
            for task in response["tasks"]:
                st.write(f"- {task_labels.get(task, task)}")

        with col2:
            st.subheader("Results")
            for item in response["results"]:
                st.markdown(f"### {item['task']}")

                if item["task"] == "Appointment Booking":
                    booking = item["output"]
                    if booking["success"]:
                        st.success(
                            f"Appointment booked with {booking['doctor']} "
                            f"({booking['specialty']}) at {booking['slot']}."
                        )
                    else:
                        st.error(booking["message"])

                elif item["task"] == "Medical Information Search":
                    st.write("Latest treatment summary:")
                    for line in item["output"]:
                        st.write(f"- {line}")