from dataclasses import dataclass


@dataclass
class News:
    title: str
    content: str
    source: str
    time: str
