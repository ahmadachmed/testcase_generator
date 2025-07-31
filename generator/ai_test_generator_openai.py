from openai import OpenAI

def generate_test_cases(api_key, raw_text):
    client = OpenAI(api_key=api_key)

    prompt = f"""
You are a QA assistant. Given the following product requirement document:

{raw_text[:3000]}

Generate a list of test cases in JSON format with the following fields:
- Title
- Description
- Preconditions
- Steps
- Expected Result
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response.choices[0].message.content
