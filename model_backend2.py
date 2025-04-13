# model_backend.py

from chat_api import ask_chatgpt_for_analysis  # 👈 This imports the function we wrote together
from main import main

# main[0], main[1], main[2]

def run_model(query: str) -> tuple[str, str]:
    """
    This function receives a query string from the UI,
    builds the model output text (or fetches it from a database),
    and sends both to ChatGPT for analysis and plotting.
    """
    # ❗️Replace this with your real logic to extract information
    raw_output = main(query)
    model_output_text = [raw_output[0], raw_output[1], raw_output[2]]
    

    # Call ChatGPT to get the analysis
    analysis = ask_chatgpt_for_analysis(model_output_text, query)
    return analysis

'''def fetch_model_output(query: str) -> str:
    """
    Dummy function that returns example info based on the query.
    Replace this with your actual logic that fetches from your data.
    """
    example_data = {
        "StartupX": "StartupX raised CHF 5M in a Series A round led by Swisscom Ventures, focusing on climate tech.",
        "climate": "Several Swiss startups have raised funding in the climate tech space recently.",
        "trend": "The Swiss startup ecosystem saw a 25% growth in AI-based companies since 2023."
    }
    for key in example_data:
        if key.lower() in query.lower():
            return example_data[key]
    return "No specific data matched your query."'''