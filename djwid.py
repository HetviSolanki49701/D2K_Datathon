import openai
import fitz


# def contents(file):
#     doc = fitz.open(f"{file}.pdf")
#     # Abstract in page 0
#     h1 = ["Abstract", "When breast cancer", "Family health", "cited", "Summary"]
#     h2 = ['Contents', 'Keywords', 'cancer', 'Neoplasms', "What's new", 'Introduction']

#     for i in range(len(h1)):
#         if h1[i] in doc[0:2]


def getSummary(file):
    doc = fitz.open(f"{file}")
    openai.api_key = "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"

    summary_list = []

    for page in doc:
        text = page.get_text("text")
        prompt = "Give a summary of 100 words for: " + text
        resp = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=120,
            top_p=0.9,
            frequency_penalty=0.0,
            presence_penalty=1,
        )

        summary_list.append(resp["choices"][0]["text"])

    summary = " ".join(summary_list)

    prompt = "Give a summary of 500 words for: " + text
    resp = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=400,
        top_p=0.9,
        frequency_penalty=0.0,
        presence_penalty=1,
    )

    return resp["choices"][0]["text"]


# getSummary("6")
