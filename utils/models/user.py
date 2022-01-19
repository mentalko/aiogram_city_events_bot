from typing import Dict, List


class User(Dict):
    """
        User structure
    """
    id: int
    username: str
    events: List[str]