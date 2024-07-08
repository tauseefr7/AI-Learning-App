import random

# List of toast messages paired with their icons
TOAST_MESSAGES = [
    ("Ready to test your YouTube knowledge?", "🎥"),
    ("Think you caught all the details? Let's find out!", "🔍"),
    ("It's quiz time! No spoilers allowed.", "⏳"),
    ("Popped in for a quiz? You're in the right place!", "🍿"),
    ("Another video, another quiz!", "🔄"),
    ("Video watched? Check. Quiz taken? Pending...", "✅"),
    ("Dive deeper into your YouTube content.", "🌊"),
    ("Up for a YouTube rewind in quiz form?", "⏪"),
    ("Let's decode your recent YouTube watch!", "🧩"),
    ("Transform your watch time into quiz time!", "🔄"),
    ("Here to validate your YouTube expertise?", "🔍")
]

def get_random_toast():
    """
    Returns a random toast message and icon.
    
    Selects a random pair from the predefined list of toast messages and icons.
    """
    return random.choice(TOAST_MESSAGES)
