import gradio as gr
import os
import requests
from io import BytesIO
import numpy as np
from PIL import Image
from deep_translator import GoogleTranslator
eng2vn=GoogleTranslator(source='english', target='vietnamese')
def convert_json_to_human_readable(response):
  result_str=f"Error: {response.status_code}"
  if response.status_code == 200:
      json_data = response.json()

      # Extract information from the JSON data
      request_id = json_data.get('request_id', '')
      image_quality = json_data['data'].get('image_quality', '')
      body_part = json_data['data'].get('body_part', '')
      image_type = json_data['data'].get('image_type', '')
      results = json_data['data'].get('results_english', {})
      results = sorted(results.items(), key=lambda x: x[1], reverse=True)

      error_code = json_data.get('error_code', '')
      log_id = json_data.get('log_id', '')

      # Create a human-readable string
      result_str = f'''
      Kết Quả Phân Tích:
      - Bộ phận cơ thể : {body_part}

      Phần Trăm Nguy Cơ Mắc Các Bệnh Như Sau:
      {",".join([f"{eng2vn.translate(condition)} ({score*100:.2f}%)" for condition, score in results])}'''
  return result_str
def update(input_img):
    # Define the API endpoint and headers
    url = "https://detect-skin-disease.p.rapidapi.com/facebody/analysis/detect-skin-disease"
    headers = {
        "X-RapidAPI-Key": "e4530f9ad1msh77bd93b41ac4530p13639ejsnc7f426bb18b9",
        "X-RapidAPI-Host": "detect-skin-disease.p.rapidapi.com"
    }
    # Convert NumPy image to a file-like object
    img = Image.fromarray(input_img.astype(np.uint8))
    img_bytes_io = BytesIO()
    img.save(img_bytes_io, format="PNG")
    img_bytes_io.seek(0)
    # Prepare the image file for the API call
    files = {"image": ("image.png", img_bytes_io, "image/png")}

    # Make the API call
    response = requests.post(url, headers=headers, files=files)

    return convert_json_to_human_readable(response)
def create_Recognition_Skin_Disease_tab():
    with gr.Blocks() as Recognition_Skin_Disease_Tab:
        gr.Markdown("Tải Ảnh Lên và Click vào **Run** để xem chẩn đoán về bệnh ngoài da.")
        with gr.Row():
            inp_image = gr.Image(label="Hình Ảnh Bệnh Ngoài Da", value=os.path.join(os.path.dirname(__file__), "image_skin_disease.jpg"), interactive=True, height=512, width=512)
        with gr.Row(): 
            out = gr.Textbox(label = "Kết Quả Chẩn Đoản")
        btn = gr.Button("Run")
        btn.click(fn=update, inputs=inp_image, outputs=out)
    return Recognition_Skin_Disease_Tab
