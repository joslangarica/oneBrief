import openai

def generate_content(prompt, api_key, conversation_history=None):
    try:
        messages = [
            {"role": "system", "content": "You are a senior web developer, expert in Bootstrap and web content creation"},
            {"role": "user", "content": prompt}]
        if conversation_history:
            messages = conversation_history + messages

        response = openai.ChatCompletion.create(
            model="gpt-4",
            #model="gpt-3.5-turbo",
            messages=messages,
            temperature=1,
            api_key=api_key
        )
        return response.choices[0]["message"]["content"]
    except Exception as e:
        print(f"Error while generating content: {e}")
        return None