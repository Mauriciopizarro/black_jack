from abc import abstractmethod, ABC
from typing import Dict


class AuthProvider(ABC):

    @abstractmethod
    def get_user_data(self, token: str) -> Dict:
        pass
