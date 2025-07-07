# This is a conceptual example, actual implementation depends on LLM API
import os
# import json
# import requests
import openai
from dotenv import load_dotenv
# from langfuse.decorators import observe
# from langfuse.openai import openai
# from langsmith import traceable

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def read_django_files(project_path):
    content = {}
    for root, _, files in os.walk(project_path):
        for file in files:
            if file.endswith(('.py', '.html')) and \
               any(keyword in root for keyword in ['models', 'views', 'templates']):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content[file_path] = f.read()
    return content

django_project_path = 'C:\\Users\\svive\\Django forms Project'
files_content = read_django_files(django_project_path)

prompt_parts = [
    "I am providing you with the code of a Django project. Please generate a comprehensive README file for this project.",
    "there are two projects first one is Form and other is Expense tracker, first create for Form project then create for expense tracker"
    "The README should include:",
    "- A brief overview of the project's purpose. generate my html pages screenshot add it into readme files, include emojis of in project explnations",
    "- Instructions for setting up and running the project locally (dependencies, database, server).",
    "- An explanation of the key features and functionalities.",
    "- A high-level overview of the project's directory structure.",
    "\n--- Django Project Code ---\n"
]

MAX_FILE_LENGTH = 2000

def build_prompt_from_files(files_content):
    prompt_parts = [
        "You are an expert in writing README files for Django projects.",
        "I will give you source code from multiple files. Summarize the purpose, features, and setup instructions.",
        "\n--- Django Code Files ---\n"
    ]

    for file_path, content in files_content.items():
        if len(content) > MAX_FILE_LENGTH:
            content = content[:MAX_FILE_LENGTH] + "\n# [Truncated for length]"
        prompt_parts.append(f"### File: {file_path}\n```python\n{content}\n```\n")

    return "\n".join(prompt_parts)


full_prompt = "\n".join(prompt_parts)
# print(full_prompt)

response = openai.chat.completions.create(
    model="gpt-3.5-turbo-16k",
    messages=[
        {"role": "system", "content": "You are a helpful assistant who writes documentation."},
        {"role": "user", "content": full_prompt}
    ],
    temperature=0.7,
    max_tokens=2048
)

# print(response)
readme_text = response.choices[0].message.content
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_text)

print("README.md generated.")

