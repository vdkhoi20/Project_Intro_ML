import gradio as gr
def create_Recognition_Skin_Disease_tab():
    with gr.Blocks() as Recognition_Skin_Disease_Tab:
        def update(name):
            return f"Welcome to Gradio, {name}!"

        gr.Markdown("Start typing below and then click **Run** to see the output.")
        with gr.Row():
            inp = gr.Textbox(placeholder="What is your name?")
            out = gr.Textbox()
        btn = gr.Button("Run")
        btn.click(fn=update, inputs=inp, outputs=out)
    return Recognition_Skin_Disease_Tab