from typing import Dict, List

import httpx


# --- MOCK IMPLEMENTATION ---
def get_keyword_data_mock(keyword: str) -> Dict[str, str | List[str]]:
    return {
        "keyword": keyword,
        "mocked": True,
        "search_volume": "12,000",
        "competition": "Medium",
        "cpc": "$1.45",
        "keyword_difficulty": "63 / 100",
        "related_keywords": [
            f"best {keyword} 2025",
            f"cheap {keyword} deals",
            f"{keyword} comparison",
        ],
    }


# --- PLACEHOLDER FOR REAL IMPLEMENTATION ---
def get_keyword_data_real(
    keyword: str, api_key: str
) -> Dict[str, str | List[str]]:
    raise NotImplementedError(
        "Real keyword data fetching not implemented yet."
    )

    if not api_key:  # pylint: disable=W0101
        raise ValueError("SEO_DATA_API_KEY is required")

    url = "https://some-keyword-api.com/search"
    params = {
        "api_key": api_key,
        "keyword": keyword,
        "country": "us",
        "language": "en",
    }

    response = httpx.get(url, params=params)
    response.raise_for_status()

    return response.json()
