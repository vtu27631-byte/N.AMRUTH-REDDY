# Install OpenAI SDK
# pip install openai

import openai

# Set your API key
openai.api_key = "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"

# Create a chat completion request
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Give me 3 ideas that I could build using OpenAI APIs"}
    ]
)

# Print the response from the model
print(completion.choices[0].message['content'])
