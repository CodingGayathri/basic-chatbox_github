def chatbox():
    print("Chatbox: Hello! I'm your friendly chatbot. Type 'exit' to end the conversation.")
    
    while True:
        # Take user input
        user_input = input("You: ").strip().lower()

        # Check for exit condition
        if user_input == 'exit':
            print("Chatbox: Goodbye! Have a great day!")
            break

        # Predefined responses
        elif 'hi' in user_input or 'hello' in user_input:
            print("Chatbox: Hi there! How can I assist you today?")
        elif 'name' in user_input:
            print("Chatbox: I'm your friendly chatbot.")
        elif 'how are you' in user_input:
            print("Chatbox: I'm just a program, but I'm functioning well! How about you?")
        elif 'time' in user_input:
            print("Chatbox: I'm not sure about the time, but it's always a good time to chat!")
        else:
            print("Chatbox: I'm sorry, I don't understand that. Can you ask something else?")

# Run the chatbox
if __name__ == "__main__":
    chatbox()