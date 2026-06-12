from jarvis.utils import get_current_time, format_output
from config import DEFAULT_RESPONSES

class Jarvis:
    def __init__(self, mode="text", debug=False):
        self.mode = mode
    
    def greet(self):
        print(format_output(DEFAULT_RESPONSES["greeting"]))
    
    def run(self):
        self.greet()
        while True:
            try:
                user_input = input("\n🎤 You: ").strip()
                if not user_input:
                    continue
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print(format_output(DEFAULT_RESPONSES["farewell"]))
                    break
                response = self.process_command(user_input)
                print(format_output(response))
            except KeyboardInterrupt:
                print(format_output(DEFAULT_RESPONSES["farewell"]))
                break
    
    def process_command(self, user_input):
        user_lower = user_input.lower()
        if "time" in user_lower or "date" in user_lower:
            return get_current_time()
        if "joke" in user_lower:
            return "Why do programmers prefer dark mode? Because light attracts bugs!"
        return "That's interesting! Tell me more."
