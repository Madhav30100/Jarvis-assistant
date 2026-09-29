from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

def ask_ai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful voice assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except:
        return "Sorry, I couldn't process that."