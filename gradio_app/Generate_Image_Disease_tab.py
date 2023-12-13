import gradio as gr
from diffusers import DiffusionPipeline
import torch
from deep_translator import GoogleTranslator

# Load the pretrained model
pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
pipe.to("cuda") # if using torch < 2.0

def create_Generate_Image_Disease_tab():
    with gr.Blocks(theme='abidlabs/dracula_revamped') as Generate_Image_Disease_Tab:
        def generate(prompt):
            # Translate the prompt from Vietnamese to English
            prompt_en = GoogleTranslator(source='vietnamese', target='english').translate(prompt)

            # Generate images from the model
            images = pipe(prompt=prompt_en, num_inference_steps=25).images[0]

            return images

        gr.Markdown("Vui lòng điền vào ô trống và nhấn **Chạy** để hiển thị ra kết quả.")
        with gr.Row():
            out = gr.Image()
        with gr.Row():  
            inp = gr.Textbox(placeholder="Loại bệnh bạn muốn hiển thị")
        btn = gr.Button("Chạy")
        btn.click(fn=generate, inputs=inp, outputs=out)
    return Generate_Image_Disease_Tab
