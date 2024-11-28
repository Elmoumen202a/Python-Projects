def welcome_message():
    print("Welcome to the Virtual Medical Examination Tool 🩺")
    print("Answer the following questions for a quick check-up.")

def collect_patient_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    symptoms = input("List your symptoms separated by commas: ").split(",")
    return {"name": name, "age": age, "symptoms": [s.strip().lower() for s in symptoms]}

def diagnose(symptoms):
    # Basic symptom-diagnosis mapping
    common_issues = {
        "fever": "You might have an infection. Stay hydrated and monitor your temperature.",
        "cough": "It could be a cold or allergy. If persistent, consider seeing a doctor.",
        "headache": "This may be due to stress or dehydration. Rest and drink water.",
    }
    advice = [common_issues.get(symptom, f"No specific advice for {symptom}. Please consult a doctor.") for symptom in symptoms]
    return advice

def main():
    welcome_message()
    patient_data = collect_patient_data()
    print(f"\nHello, {patient_data['name']}!")
    print("Analyzing your symptoms...")
    advice = diagnose(patient_data['symptoms'])
    print("\n--- Diagnosis ---")
    for symptom, suggestion in zip(patient_data['symptoms'], advice):
        print(f"- {symptom.capitalize()}: {suggestion}")

if __name__ == "__main__":
    main()
