from groq import Groq

def generate_test_cases(api_key, raw_text):
    client = Groq(api_key=api_key)

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "user",
                "content": f"""
Given this PRD document:

{raw_text[:3000]}

Generate a list of positive and negative test cases scenario in JSON with these following format:
- Title
- Description
- Preconditions
- Steps
- Expected Result
"""
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content
