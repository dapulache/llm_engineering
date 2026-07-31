from openai import OpenAI
import os

def get_client(provider="ollama"):

    configs = {
        "openai": {
            "client": OpenAI(
                api_key=os.getenv("OPENAI_API_KEY")
            )
        },

        "ollama": {
            "client": OpenAI(
                base_url="https://ollama.com/v1",
                api_key=os.getenv("OLLAMA_API_KEY")
            )
        },

        "google": {
            "client": OpenAI(
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
                api_key=os.getenv("GOOGLE_API_KEY")
            )
        }

    }

    return configs[provider]


def get_models(provider="ollama"):
    MODELS = {
        "google": {
            "cheap": "google/gemini-2.5-flash-lite",
            "medium": "gemini-2.5-flash",
            "large": "gemini-2.5-pro"
        },
        "ollama": {
            "cheap": "gpt-oss:20b",
            "medium": "gemma4:31b",
            "large": "qwen3.5:397b"
        }
    }

    return MODELS[provider]