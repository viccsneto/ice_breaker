from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    print("Hello, LangChain!")
    print("Using OPENAI_API_BASE as:", os.environ["OPENAI_API_BASE"])
