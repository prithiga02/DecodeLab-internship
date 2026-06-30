def chatbot():
    print("Bot: Welcome to DecodeLabs! (Type 'bye' to exit)")
    
    while True:
        # INPUT: Sanitization (Convert to lowercase & remove spaces)
        user_input = input("You: ").lower().strip()
        
        # PROCESS: Logic Gates (Intent Matching)
        if user_input in ['hi', 'hello', 'hey']:
            print("Bot: Hello! How can I assist you today?")
            
        elif 'project' in user_input:
            print("Bot: Project 1 is a Rule-Based Chatbot using IPO model.")
            
        elif 'bye' in user_input or 'exit' in user_input:
            print("Bot: Goodbye! Have a great day.")
            break # OUTPUT: Closing the loop
            
        else:
            # Fallback response
            print("Bot: I am still learning. Could you please rephrase?")

if __name__ == "__main__":
    chatbot()