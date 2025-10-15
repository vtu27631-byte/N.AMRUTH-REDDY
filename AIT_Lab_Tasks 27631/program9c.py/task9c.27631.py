import openai
import gradio as gr

# Set your API key
openai.api_key = "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"

# Initialize conversation with system message
messages = [
    {"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation."}
]

# Define chatbot function
def CustomChatGPT(user_input):
    # Add user message
    messages.append({"role": "user", "content": user_input})
    
    # Get response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    
    # Add assistant response
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    
    return ChatGPT_reply

# Create Gradio interface
demo = gr.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="INTELLIGENT CHATBOT"
)

# Launch the interface with sharing enabled
demo.launch(share=True)
