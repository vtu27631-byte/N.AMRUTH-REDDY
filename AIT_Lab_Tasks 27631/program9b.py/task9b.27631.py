import openai

# Set your API key
openai.api_key = "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"

# Initialize messages
messages = []

# Ask user for type of chatbot
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type your query (type 'quit' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Exiting chat...")
        break

    # Add user message
    messages.append({"role": "user", "content": user_input})

    # Get response from OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]

    # Add assistant response
    messages.append({"role": "assistant", "content": reply})

    print("Assistant:", reply, "\n")
