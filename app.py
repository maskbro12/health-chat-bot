import streamlit as st
from transformers import pipeline

# Load a more advanced model for better accuracy
hatbot = pipeline("text-generation", model="facebook/opt-1.3b")

def HealthCareAssistant(user_input):
    """Enhance query handling with more precise responses."""
    user_input = user_input.lower()
    
    if "symptom" in user_input:
        return "It looks like you're experiencing symptoms. Please provide more details so I can guide you better. However, for a proper diagnosis, consult a healthcare professional."
    elif "appointment" in user_input:
        return "Would you like to book an appointment with a specialist? I can help you find the nearest available doctor."
    elif "medication" in user_input:
        return "Always take prescribed medications as directed. Do you need dosage details or reminders?"
    elif "covid" in user_input:
        return "COVID-19 guidelines: Wear a mask, maintain social distancing, and stay updated with vaccinations. Do you have specific symptoms or need testing information?"
    elif "emergency" in user_input:
        return "If this is a medical emergency, please call emergency services immediately. Would you like emergency contact numbers?"
    
    else:
        response = hatbot(user_input, max_length=500, num_return_sequences=1)
        return response[0]['generated_text']

def main():
    st.title("🩺 AI-Powered Healthcare Assistant Chatbot")
    st.write("Ask me any health-related question, and I'll assist you with reliable information!")
    
    user_input = st.text_input("Your Question:")
    
    if st.button("Ask"):  
        if user_input:
            st.write("**User:**", user_input)
            with st.spinner("Processing..."):
                response = HealthCareAssistant(user_input) 
            st.write("**Healthcare Assistant:**", response)
        else:
            st.warning("Please enter a question before clicking Ask.")

if __name__ == "__main__":
    main()
