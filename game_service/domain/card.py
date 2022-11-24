from typing import Optional, ClassVar
from pydantic import BaseModel


class Card(BaseModel):
    value: Optional[int] = None
    symbol: Optional[str] = None

    def dict(self, *args, **kwargs):
        card_dict = super(Card, self).dict()
        card_dict["type"] = self.__class__.__name__
        return card_dict


class NumberCard(Card):
    def __init__(self, value):
        super(NumberCard, self).__init__(value=value, symbol=str(value))


class LetterCard(Card):
    def __init__(self, symbol):
        super(LetterCard, self).__init__(value=10, symbol=str(symbol))


class As(Card):
    value: int = 1
    special_value: ClassVar[int] = 10
    symbol: str = 'A'
