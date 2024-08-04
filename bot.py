import slack
import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path('.') / '.env'


print(f"Current Working Directory: {os.getcwd()}")


if not env_path.exists():
    print(f".env file not found at {env_path}")
else:
    print(f".env file found at {env_path}")
    with open(env_path) as f:
        print(f".env file content:\n{f.read()}")


load_dotenv(dotenv_path=env_path)


slack_token = os.getenv('SLACK_TOKEN')

print(f"SLACK_TOKEN: {slack_token}")


if not slack_token:
    raise ValueError("No SLACK_TOKEN provided. Please set it in the .env file.")


client = slack.WebClient(token=slack_token)

