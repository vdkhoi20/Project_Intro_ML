import gradio as gr
from diffusers import DiffusionPipeline
import torch
from torchvision.transforms import ToPILImage
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
            images = pipe(prompt=prompt_en).images[0]

            return images

        gr.Markdown("Start typing below and then click **Run** to see the output.")
        with gr.Row():
            inp = gr.Textbox(placeholder="Description")
            out = gr.Image()
        btn = gr.Button("Run")
        btn.click(fn=generate, inputs=inp, outputs=out)
    return Generate_Image_Disease_Tab
