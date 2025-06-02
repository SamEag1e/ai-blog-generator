import re


def inject_urls_to_post(post: str) -> str:
    # Extract all unique placeholders like {{AFF_LINK_1}}, {{AFF_LINK_2}}, etc.
    placeholders = sorted(set(re.findall(r"\{\{AFF_LINK_\d+\}\}", post)))

    # Replace each with a dummy URL based on its index
    for ph in placeholders:
        index_match = re.search(r"\d+", ph)
        index = index_match.group() if index_match else "0"
        dummy_url = f"https://dummyurl.com/track{index}"
        post = post.replace(ph, dummy_url)

    return post


def has_placeholder(updated_post: str) -> bool:
    unreplaced = re.findall(r"\{\{AFF_LINK_\d+\}\}", updated_post)

    if unreplaced:
        return True

    return False
