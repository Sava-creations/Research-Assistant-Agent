def main():
    client = Groq(
        api_key = os.environ.get("GROQ_API_KEY"),
    )
