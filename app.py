from voice import listen_speech, speak_text
from ai import generate_reply


def main():
    print("Riverwood AI Voice Agent Started \n")
    speak_text("Namaste! Welcome to Riverwood. Would you like to continue in Hindi or English?")

    
    lang_choice = listen_speech().lower()
    # if "hindi" in lang_choice:
    #     lang = "hi"
    #     speak_text("Namaste Sir! Aaj subah kaise hain? Main aapki madad kaise kar sakti hoon?")
    # else:
    #     lang = "en"
    #     speak_text("Good morning! Hope you had a great weekend. How can I help you today?")

    if not lang_choice:
        speak_text("Sorry, I couldn't hear that. You can type your preferred language — Hindi or English.")
        lang_choice = input("Type your language (Hindi/English): ").lower().strip()

    
    lang_choice = lang_choice.lower().strip()

    
    if "hindi" in lang_choice or "हिन्दी" in lang_choice or "हिंदी" in lang_choice:
        lang = "hi"
        speak_text("नमस्ते सर! आज सुबह कैसे हैं? मैं आपकी किस प्रकार मदद कर सकती हूँ?")
    elif "english" in lang_choice or "eng" in lang_choice:
        lang = "en"
        speak_text("Good morning! Hope you're doing great today. How can I assist you?")
    else:
        print("Sorry, I can only perform in Hindi or English. Please type your choice again.")
        speak_text("Sorry, I can only perform in Hindi or English. Please type your choice again.")
        lang_choice = input("Type your language (Hindi/English): ").lower().strip()

        if "hindi" in lang_choice or "हिन्दी" in lang_choice or "हिंदी" in lang_choice:
            lang = "hi"
            speak_text("नमस्ते सर! आज सुबह कैसे हैं? मैं आपकी किस प्रकार मदद कर सकती हूँ?")
        else:
            lang = "en"
            speak_text("Okay, I'll continue in English. How can I assist you today?")


    
    while True:
        user_input = listen_speech()

        if not user_input:
            speak_text("Sorry, I couldn’t hear that. You can type your response here.")
            typed_input = input("Type your message (or 'exit' to stop): ").strip()
            user_input = typed_input 

        if any(word in user_input.lower() for word in ["stop", "bye", "exit", "thank you", "no update", "not now", "quit"]):
            if lang == "hi":
                speak_text("ठीक है सर! आपसे बात करके अच्छा लगा। फिर मिलते हैं, धन्यवाद।")
            else:
                speak_text("Alright! It was lovely talking to you. Take care and see you soon!")
            print("Exiting Riverwood. Goodbye!")
            break

        reply = generate_reply(user_input, lang)
        if reply.lower().startswith(("ai:", "riverwood:", "assistant:")):
            reply = reply.split(":", 1)[-1].strip()
        speak_text(reply)


if __name__ == "__main__":
    main()

