from abc import ABC, abstractmethod


class IPDFConverter(ABC):
    @staticmethod
    @abstractmethod
    async def convert(path: str) -> str:
        """Convert a PDF file to a PNG image."""
        ...
