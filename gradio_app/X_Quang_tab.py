import gradio as gr
from PIL import Image
from ultralyticsplus import YOLO, postprocess_classify_output
import os
model = YOLO('keremberke/yolov8m-chest-xray-classification')
model.overrides['conf'] = 0.25

def update_X_Quang(image):
    results = model.predict(image)
    print(results)
    processed_result = postprocess_classify_output(model, result=results[0])
    normal = processed_result['NORMAL']
    pneumonia = processed_result['PNEUMONIA']
    if (normal > pneumonia):
        result = "Không có bệnh viêm phổi"
        score = round(normal*100)
    else:
        result = "Có bệnh viêm phổi"
        score = round(pneumonia*100)
    return result + " với độ chính xác là: " + str(score) + "%"

def create_X_Quang_tab():
    with gr.Blocks() as X_Quang_tab:
        with gr.Row():
            inp = gr.Image(label="Ảnh X-Quang chuẩn đoán viêm phổi",value=os.path.join(os.path.dirname(__file__), "image_X_Quang.jpg"), interactive=True, height=512, width=512)
        with gr.Row():
            out = gr.Text(label="Kết quả X-Quang viêm phổi")
        btn = gr.Button("Chạy")
        btn.click(fn=update_X_Quang, inputs=inp, outputs=out)
    return X_Quang_tab
