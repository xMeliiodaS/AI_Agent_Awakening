from core.ai_processor_test import AIProcessorTest
from commands.open_app_command import OpenAppCommand
from commands.type_text_command import TypeTextCommand
from commands.wait_command import WaitCommand
from commands.windows_command import WindowsCommand


def main():
    ai = AIProcessorTest()  # Initialize AI Processor

    # Example test: Open Notepad, type "Hello", then close it
    high_level_command = "Open Notepad"

    # Ask AI to break it down
    command_sequence = ai.get_next_command(high_level_command)

    if not command_sequence:
        print("AI could not generate a command sequence.")
        return

    for command in command_sequence:
        action = command["action"]
        params = command["params"]

        # Execute the corresponding command based on the action
        if action == "open_app":
            OpenAppCommand(params["app_name"]).execute_command()
        elif action == "wait":
            WaitCommand(params["seconds"]).execute_command()
        elif action == "type_text":
            TypeTextCommand(params["text"]).execute_command()
        elif action == "hotkey":
            WindowsCommand(params["keys"]).execute_command()

        # Update AI memory after executing the command
        ai.update_context(screen_text="Notepad opened", last_command=action)

    print("Test flow completed.")


if __name__ == "__main__":
    main()
