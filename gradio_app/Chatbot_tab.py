import gradio as gr
from openai import AsyncOpenAI

def create_Chatbot_tab():
    # def echo(message, history):
    #     return message

    client = AsyncOpenAI(
        api_key="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",
    )

    messages=[{"role": "system", "content": " You are a doctor and health assistant"
                                            "If user ask about any disease, tell them about that disease's information"
                                            " Must direct the conversation to medical and health topics when users ask about external issues and tell them that you can only advise on health-related issues"
                                            " Try to ask as much as information about disease symptom (give the patient some questions about that disease symptom) and give the patient some information about related disease and do some diagnose for them"}]
    async def respond(message,chatHistory):
        if message :
            messages.append(
                {"role": "user", "content": message},
            )
            completion = await client.chat.completions.create(model="gpt-3.5-turbo",
                                                          messages=messages, temperature = 0.5)
            answer = completion.choices[0].message.content
        return answer

    Chatbot_tab = gr.ChatInterface(fn=respond, examples=["Bệnh viêm phổi", "Chẩn đoán về COVID 19", "Nguồn gốc của đau dạ dày"], title="Trợ lý sức khỏe trực tuyến")
    return Chatbot_tab


#   OLD CODE FOR REVIEWING



    # async def respond(message,chatHistory):
    #     if message :
    #         messages.append(
    #             {"role": "user", "content": message},
    #         )
    #         completion = await client.chat.completions.create(model="gpt-3.5-turbo",
    #                                                       messages=messages, temperature = 0.8)
    #         answer = completion.choices[0].message.content
    #         chatHistory.append((message,answer))
    #     return "", chatHistory
    #
    # with gr.Blocks() as demo:
    #     chatbot = gr.Chatbot(height=300) #just to fit the notebook
    #     msg = gr.Textbox(label="Prompt")
    #     btn = gr.Button("Submit")
    #     clear = gr.ClearButton(components=[msg, chatbot], value="Clear console")
    #
    #     btn.click(respond, inputs=[msg, chatbot], outputs=[msg, chatbot])
    #     msg.submit(respond, inputs=[msg, chatbot], outputs=[msg, chatbot]) #Press enter to submit
    #
    # return demo