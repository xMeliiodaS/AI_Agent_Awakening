import json
import os

# Paths to JSON files
CONTEXT_MEMORY_PATH = "core/ai_data/context_memory.json"
COMMAND_TEMPLATES_PATH = "core/ai_data/command_templates.json"
ERROR_RESPONSES_PATH = "core/ai_data/error_responses.json"


class AIProcessorTest:
    def __init__(self):
        print(os.getcwd())
        self.context_memory = self.load_json(CONTEXT_MEMORY_PATH)
        self.command_templates = self.load_json(COMMAND_TEMPLATES_PATH)
        self.error_responses = self.load_json(ERROR_RESPONSES_PATH)

    @staticmethod
    def load_json(path):
        """ Load JSON data from a file. """
        if not os.path.exists(path):
            return {}
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def save_json(path, data):
        """ Save JSON data to a file. """
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def update_context(self, screen_text, last_command):
        """ Update AI's context memory with new state. """
        self.context_memory["previous_commands"].append(last_command)
        self.context_memory["last_screen_text"] = screen_text

        # Save updates
        self.save_json(CONTEXT_MEMORY_PATH, self.context_memory)

    def get_next_command(self, high_level_command):
        """ Convert a high-level command into detailed steps. """
        return self.command_templates.get(high_level_command, [])
