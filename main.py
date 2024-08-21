import gradio as gr

def translator(audio_file):
    pass

web = gr.Interface(
    fn=translator,
    inputs=gr.Audio(
        sources=["microphone"],
        type="filepath"
    ),
    outputs=[],
    title="Voice Translator",
    description="AI voice translator into multiple languages."
    )

web.launch()