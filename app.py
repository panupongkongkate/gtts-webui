import gradio as gr
from gtts import gTTS
import tempfile

def text_to_speech(text, language):
    # สร้างไฟล์เสียงชั่วคราว
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        tts = gTTS(text=text, lang=language)
        tts.save(temp_audio.name)
        return temp_audio.name  # ส่งคืนพาธไฟล์เสียง

# สร้าง UI ของ Gradio โดยปิดการใช้งานปุ่ม Flag
iface = gr.Interface(
    fn=text_to_speech,
    inputs=[
        gr.Textbox(label="กรอกข้อความที่ต้องการให้แปลงเป็นเสียง"),
        gr.Dropdown(choices=["th", "en", "fr", "de", "ja"], label="เลือกภาษา"),
    ],
    outputs=gr.Audio(label="พรีวิวเสียง"),
    title="gTTS WebUI",
    description="กรอกข้อความและเลือกภาษาที่ต้องการ จากนั้นคลิกเพื่อแปลงเป็นเสียง",
    live=False,
    # allow_flagging="never"  # ปิดการใช้งานปุ่ม Flag
)

# เรียกใช้แอป Gradio
if __name__ == "__main__":
    iface.launch()
