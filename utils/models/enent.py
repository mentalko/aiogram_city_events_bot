from typing import Dict, List

class Event(Dict):
    """
        Event structure
    """
    id: int
    title: str
    date: str
    place: str
    desctiption: str
    # tags: List[str]
    is_active: bool