import openai

openai.api_key = "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"


def gpt3_completion(
    prompt,
    engine="text-davinci-002",
    temp=0.7,
    top_p=1.0,
    tokens=400,
    freq_pen=0.0,
    pres_pen=0.0,
    stop=["<<END>>"],
):
    prompt = prompt.encode(encoding="ASCII", errors="ignore").decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop,
    )
    text = response["choices"][0]["text"].strip()
    return text


def summary(count, text):
    prompt_ = f"Give me summary of {count} words for the following content \n\n {text}"
    response_ = gpt3_completion(prompt_)
    return response_
