from voice import speak_text
speak_text("Namaste Sir! Good morning. Kal humne site ka flooring complete kar liya tha.")


# test_env.py
# import os
# from dotenv import load_dotenv
# from elevenlabs import ElevenLabs

# # Load environment variables
# load_dotenv()

# key = os.getenv("ELEVENLABS_API_KEY")
# print("🔑 Loaded key:", key[:8], "...")

# # Initialize client
# client = ElevenLabs(api_key=key)

# try:
#     # ✅ Check if your account and voice access work
#     voices = client.voices.get_all()
#     print("✅ ElevenLabs connected successfully!")
#     print(f"🎙️ Total Voices Available: {len(voices.voices)}")

#     # List a few voices
#     for v in voices.voices[:3]:
#         print(f" - {v.voice_id}: {v.name}")

# except Exception as e:
#     print("❌ Error:", e)
