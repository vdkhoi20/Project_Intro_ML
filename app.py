import gradio as gr
from gradio_app.Chatbot_tab import create_Chatbot_tab
from gradio_app.Generate_Image_Disease_tab import create_Generate_Image_Disease_tab
from gradio_app.X_Quang_tab import create_X_Quang_tab
from gradio_app.Recognition_Skin_Disease_tab import create_Recognition_Skin_Disease_tab



demo=gr.TabbedInterface([create_Chatbot_tab(),
                            create_Generate_Image_Disease_tab(),
                            create_X_Quang_tab(),
                            create_Recognition_Skin_Disease_tab()],
                        ["Health consulting assistant","Generate images of the disease","X-ray diagnosis","skin diseases recognition"])
demo.launch()
if __name__ == "__main__":
    demo.queue().launch(share=True)
