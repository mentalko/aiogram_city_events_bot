from typing import Dict, List


class User(Dict):
    """
        User structure
    """
    id: int
    username: str
    is_bot: bool
    language_code: str
    events: List[str]
    role: str