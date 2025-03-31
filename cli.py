"""Command-line interface for the Chatbot application."""

import config

def run_cli(process_fn, llm, tools):
    """Run the command-line interface."""
    print("Chatbot for Telerik UI Components for Blazor")
    print(f"Available tools: {', '.join(config.TOOLS)}")
    print(f"Type '{config.EXIT_COMMANDS}' to exit")
    print("-" * 40)
    
    history = []
    
    while True:
        # Get user input
        user_input = input(config.CLI_PROMPT).strip()
        
        # Check if user wants to exit
        if user_input.lower() in config.EXIT_COMMANDS:
            print("Goodbye!")
            break

        # Check if user wants to debug
        if user_input.lower() in config.DEBUG_COMMANDS:
            for message in history:
                print(message)
            
            continue
            
        # Skip empty inputs
        if not user_input:
            continue
            
        try:
            # Process the query
            response = process_fn(llm, tools, user_input, history)
            
            # Update history
            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": response})
            
            # Print the response
            print("\n" + response + "\n")
            
        except Exception as e:
            print(config.ERROR_GENERAL.format(str(e)))