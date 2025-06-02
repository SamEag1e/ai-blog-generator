import re


def inject_urls_to_post(post: str) -> str:
    def replacer(match):
        placeholder = match.group(0)  # e.g., {{AFF_LINK_1}}
        index_match = re.search(r"\d+", placeholder)
        index = index_match.group() if index_match else "0"
        return f"https://dummyurl.com/track{index}"

    return re.sub(r"\{\{AFF_LINK_\d+\}\}", replacer, post)
