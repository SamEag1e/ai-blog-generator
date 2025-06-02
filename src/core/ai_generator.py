from openai import OpenAI

from core.utils import inject_urls_to_post, has_placeholder


def generate_blog_post(keyword: str, api_key: str) -> str:
    if not api_key:
        raise ValueError("OPENAI API key is required")

    client = OpenAI(api_key=api_key)
    prompt = (
        f"Write a full blog post in **HTML format** about '{keyword}' for SEO purposes. "
        f"Structure it with a <h1> title, a short <p> intro paragraph, "
        "2-3 <h2> sections with their content, and embed 2-3 affiliate links using "
        "{{AFF_LINK_1}} and {{AFF_LINK_2}} as href values. "
        "Do not replace the placeholders — just include them as-is."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # gpt-4.1, gpt-4-turbo, ...
        messages=[
            {
                "role": "system",
                "content": "You are a helpful blogging assistant.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,  # Controls randomness / creativity
        max_tokens=800,  # Upper limit of response length
    )
    post = response.choices[0].message.content
    # Inject dummy URLs for all affiliate
    # placeholders (e.g., {{AFF_LINK_1}}) to simulate real links.
    updated_post = inject_urls_to_post(post)

    # Then verify no placeholders remain un-replaced —
    # if so, raise an error.
    if has_placeholder(updated_post):
        raise ValueError("Unreplaced affiliate link placeholder found in post")

    return updated_post


def generate_mock_blog_post(keyword: str) -> str:
    post = """
        <h1>Best {keyword} for 2025</h1>
        <p>Looking for top {keyword}? Here's a detailed guide on the
        best {keyword} options available this year.</p>
        <ul>
            <li><a href="{{{{AFF_LINK_1}}}}">Item 1</a></li>
            <li><a href="{{{{AFF_LINK_2}}}}">Item 2</a></li>
            <li><a href="{{{{AFF_LINK_3}}}}">Item 3</a></li>
        </ul>
        <p>Make sure to choose what fits your needs and budget!</p>
    """.format(
        keyword=keyword.capitalize()
    )

    return inject_urls_to_post(post)
