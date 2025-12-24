from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json
import os

# ✅ Locate the knowledge base file
file_path = os.path.join(os.getcwd(), "data", "legal_kb.json")

# ✅ Load the legal knowledge base safely
try:
    with open(file_path, "r", encoding="utf-8") as f:
        legal_data = json.load(f)
    print(f"✅ Loaded knowledge base with {len(legal_data.keys())} sections from {file_path}")
except Exception as e:
    print(f"⚠️ Error loading knowledge base: {e}")
    legal_data = {}

# -------------------------------------------------------------------------------------
# ACTION: Provide definitions
# -------------------------------------------------------------------------------------
class ActionProvideDefinition(Action):
    def name(self):
        return "action_provide_definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        user_message = tracker.latest_message.get('text', '').lower()

        if "definitions" not in legal_data:
            dispatcher.utter_message(text="Sorry, I couldn't access the legal definitions.")
            return []

        found = False
        for key, value in legal_data["definitions"].items():
            if key in user_message:
                dispatcher.utter_message(text=f"📘 Definition of {key}:\n{value}")
                found = True
                break

        if not found:
            dispatcher.utter_message(text=f"Sorry, I couldn’t find a definition for '{user_message}'.")
        return []

# -------------------------------------------------------------------------------------
# ACTION: Provide templates
# -------------------------------------------------------------------------------------
class ActionProvideTemplate(Action):
    def name(self):
        return "action_provide_template"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        user_message = tracker.latest_message.get('text', '').lower()

        if "templates" not in legal_data:
            dispatcher.utter_message(text="Sorry, I couldn't access the templates right now.")
            return []

        found = False
        for key, value in legal_data["templates"].items():
            if key in user_message:
                dispatcher.utter_message(text=f"📄 Template for {key}:\n\n{value}")
                found = True
                break

        if not found:
            dispatcher.utter_message(text=f"Sorry, I couldn’t find a relevant legal template for '{user_message}'.")
        return []
