import os
from dotenv import load_dotenv
import requests


class InputData:
    def __init__(self, day):
        load_dotenv()
        self.session_token = os.environ.get("SESSION_TOKEN")
        self.url = f"https://adventofcode.com/2024/day/{day}/input"
        self.load_data()

    def load_data(self):
        obj = requests.Session()
        response = obj.request(
            "get",
            self.url,
            cookies={
                "session": self.session_token,
            },
        )
        self.input_data = response.text.split("\n")
        self.input_data = [i for i in self.input_data if i != ""]
