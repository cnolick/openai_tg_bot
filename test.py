import openai
# Set the API key
openai.api_key = "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"
# Use the ChatGPT model to generate text
model_engine = "text-davinci-003"
prompt = "Напиши пожалуйста пример gitlab-ci по сборке flask приложения"
print("Q:"+prompt)
completion = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.7)
message = completion.choices[0].text
print("A:"+message)
