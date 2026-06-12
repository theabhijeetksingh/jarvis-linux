from datetime import datetime

def format_output(text, speaker="Jarvis"):
    return f"🤖 {speaker}: {text}"

def get_current_time():
    now = datetime.now()
    day_name = now.strftime("%A")
    time_str = now.strftime("%I:%M %p")
    date_str = now.strftime("%B %d, %Y")
    return f"It is {time_str} on {day_name}, {date_str}"
