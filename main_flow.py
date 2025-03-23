from core.ai_processor_test import AIProcessorTest
from commands.open_app_command import OpenAppCommand
from commands.type_text_command import TypeTextCommand
from commands.wait_command import WaitCommand
from commands.windows_command import WindowsCommand

def main():
    ai = AIProcessorTest()  # Initialize AI Processor

    # Example test: Open Notepad, type "Hello, world!", wait for 2 seconds, then close it
    high_level_commands = [
        "Open Notepad",
        "Type Text",
        "Wait for 2 seconds",
        "Close Notepad"
    ]

    # Process each command in the sequence
    for high_level_command in high_level_commands:
        # Get detailed command sequence from AI
        command_sequence = ai.get_next_command(high_level_command)

        if not command_sequence:
            print(f"AI could not generate a command sequence for '{high_level_command}'.")
            return

        for command in command_sequence:
            action = command.split(":")[0]
            params = command.split(":")[1] if len(command.split(":")) > 1 else ""

            print(f"Executing: {action} with parameters: {params}")

            if action == "open_app":
                OpenAppCommand(params).execute_command()
            elif action == "wait":
                WaitCommand(int(params)).execute_command()
            elif action == "type_text":
                TypeTextCommand(params).execute_command()
            elif action == "close_window":
                WindowsCommand("close").execute_command()

            # Update AI memory after executing the command
            ai.update_context(screen_text="Notepad opened", last_command=action)

    print("Test flow completed.")

if __name__ == "__main__":
    main()
