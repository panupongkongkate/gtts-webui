import gradio as gr
from gtts import gTTS
import tempfile

# Define example phrases for each language
example_phrases = {
    "th": "สวัสดีครับ ยินดีต้อนรับ",
    "en": "Hello, welcome!",
    "fr": "Bonjour, bienvenue!",
    "de": "Hallo, willkommen!",
    "ja": "こんにちは、ようこそ！"
}

def text_to_speech(text, language):
    # Create a temporary audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        tts = gTTS(text=text, lang=language)
        tts.save(temp_audio.name)
        return temp_audio.name  # Return the path to the audio file

# Function to set example phrase based on language selection
def set_example_text(language):
    return example_phrases.get(language, "")

# Create the Gradio interface
with gr.Blocks() as iface:
    gr.Markdown("# gTTS WebUI")
    gr.Markdown("กรอกข้อความและเลือกภาษาที่ต้องการ จากนั้นคลิกเพื่อแปลงเป็นเสียง")
    
    # Input components
    language_dropdown = gr.Dropdown(
        choices=["th", "en", "fr", "de", "ja"],
        label="เลือกภาษา",
    )
    text_input = gr.Textbox(
        label="กรอกข้อความที่ต้องการให้แปลงเป็นเสียง",
        placeholder="ข้อความจะถูกเติมโดยอัตโนมัติเมื่อคุณเลือกภาษา"
    )
    
    # Update text input when language changes
    language_dropdown.change(
        fn=set_example_text,
        inputs=language_dropdown,
        outputs=text_input
    )
    
    # Output component
    output_audio = gr.Audio(label="พรีวิวเสียง")

    # Button to trigger text-to-speech
    convert_button = gr.Button("แปลงเป็นเสียง")
    convert_button.click(
        fn=text_to_speech,
        inputs=[text_input, language_dropdown],
        outputs=output_audio
    )

# Run the Gradio app
if __name__ == "__main__":
    iface.launch()
