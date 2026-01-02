"""Google Search Agent definition for ADK Bidi-streaming demo."""

import os

from google.adk.agents import Agent
from google.adk.tools import google_search

# Default models for Live API with native audio support:
# - Gemini Live API: gemini-2.5-flash-native-audio-preview-12-2025
# - Vertex AI Live API: gemini-live-2.5-flash-native-audio
agent = Agent(
    name="google_search_agent",
    model=os.getenv(
<<<<<<< HEAD
        "DEMO_AGENT_MODEL", "gemini-live-2.5-flash-native-audio"
=======
        "DEMO_AGENT_MODEL", "gemini-2.5-flash-native-audio-preview-12-2025"
>>>>>>> 3d9fe35ce097760c5dceb7136a2c72802c3c6021
    ),
    tools=[google_search],
    instruction="You are a helpful assistant that can search the web.",
)
