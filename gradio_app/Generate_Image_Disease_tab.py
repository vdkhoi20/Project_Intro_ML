import gradio as gr
def create_Generate_Image_Disease_tab():
    with gr.Blocks() as Generate_Image_Disease_Tab:
        def update(name):
            return f"Welcome to Gradio, {name}!"

        gr.Markdown("Start typing below and then click **Run** to see the output.")
        with gr.Row():
            inp = gr.Textbox(placeholder="What is your name?")
            out = gr.Textbox()
        btn = gr.Button("Run")
        btn.click(fn=update, inputs=inp, outputs=out)
    return Generate_Image_Disease_Tab