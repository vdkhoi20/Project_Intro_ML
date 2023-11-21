
import gradio as gr


def create_Chatbot_tab():
    def echo(message, history):
        return message
    Chatbot_tab = gr.ChatInterface(fn=echo, examples=["hello", "hola", "merhaba"], title="Echo1 Bot")
    return Chatbot_tab