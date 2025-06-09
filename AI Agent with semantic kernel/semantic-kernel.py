import os
import asyncio
from pathlib import Path

# Add references



async def main():
    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    # Load the expnses data file
    script_dir = Path(__file__).parent
    file_path = script_dir / 'data.txt'
    with file_path.open('r') as file:
        data = file.read() + "\n"

    # Ask for a prompt
    user_prompt = input(f"Here is the expenses data in your file:\n\n{data}\n\nWhat would you like me to do with it?\n\n")
    
    # Run the async agent code
    await process_expenses_data (user_prompt, data)
    
async def process_expenses_data(prompt, expenses_data):

    # Get configuration settings


    # Connect to the Azure AI Foundry project

        
        # Define an Azure AI agent that sends an expense claim email


        # Create a semantic kernel agent


        # Use the agent to process the expenses data



# Create a Plugin for the email functionality




if __name__ == "__main__":
    asyncio.run(main())
