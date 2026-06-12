import os
import subprocess
from datetime import datetime

class Jarvis:
    def __init__(self):
        self.name = "Jarvis"
    
    def speak(self, text):
        """Jarvis का response"""
        print(f"🤖 Jarvis: {text}\n")
    
    def listen(self):
        """User से input लो"""
        user_input = input("👤 You: ").strip()
        return user_input
    
    def greet(self):
        """शुरुआती स्वागत"""
        self.speak("Hello! I am Jarvis, your Linux assistant")
        self.speak("Type 'help' to see commands")
    
    def process_command(self, command):
        """Command को समझो और करो"""
        if not command:
            return True
        
        command = command.lower().strip()
        
        # Time
        if "time" in command:
            time = datetime.now().strftime("%H:%M:%S")
            self.speak(f"Current time is {time}")
        
        # Date
        elif "date" in command:
            date = datetime.now().strftime("%d-%m-%Y")
            self.speak(f"Today's date is {date}")
        
        # Files
        elif "files" in command or "list" in command:
            try:
                files = os.listdir('.')
                file_list = ", ".join(files)
                self.speak(f"Files are: {file_list}")
            except Exception as e:
                self.speak(f"Error: {e}")
        
        # Help
        elif "help" in command:
            self.speak("Commands: time, date, files, exit")
        
        # Exit
        elif "exit" in command or "bye" in command:
            self.speak("Goodbye!")
            return False
        
        else:
            self.speak(f"You said: {command}")
        
        return True
    
    def run(self):
        """Main loop"""
        self.greet()
        
        while True:
            command = self.listen()
            
            if not self.process_command(command):
                break

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
