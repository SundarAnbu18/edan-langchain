from dotenv import load_dotenv
import os

load_dotenv()


def main():
    print("Hello from langchain-course!")
    print(os.getenv("OPENAI_API_KEY"))


main();
