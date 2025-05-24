import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'  # Set your OpenAI API key here or via env var

def ai_advice(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"AI API error: {e}"

def get_ai_vuln_advice(vuln_name):
    prompt = f"Explain the impact and exploitation method of the vulnerability: {vuln_name}."
    return ai_advice(prompt)
