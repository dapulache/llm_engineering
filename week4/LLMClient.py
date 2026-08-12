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
            "cheap": "gemini-2.5-flash-lite",
            "medium": "gemini-2.5-flash",
            "large": "gemini-2.5-pro"
        },
        "ollama": {
            # 🥇 Flagship — highest capability; use for the hardest reasoning,
            # complex agents, difficult coding, research, and tasks where quality
            # matters more than speed/cost.
            "flagship": "nemotron-3-ultra",

            # 🥈 XLarge — excellent high-end reasoning; use when you need strong
            # intelligence but don't necessarily need the absolute best model.
            "xlarge": "minimax-m3",

            # 🥉 Large — strong general-purpose model; excellent balance of
            # intelligence, reliability, and cost for demanding tasks.
            "large": "gpt-oss:120b",

            # Medium — good general-purpose model for everyday reasoning,
            # coding, writing, and analysis without using a large model.
            "medium": "gemma4:31b",

            # Fast — optimized for efficiency/speed; use for simpler tasks,
            # high-volume requests, classification, extraction, etc.
            "fast": "nemotron-3-nano:30b",

            # Cheap — lowest-cost option; use for simple tasks, quick answers,
            # lightweight transformations, and high-volume workloads.
            "cheap": "gpt-oss:20b",
        }
    }

    return MODELS[provider]