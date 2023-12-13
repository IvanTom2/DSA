from abc import ABC, abstractmethod


class ListInterface(ABC):
    @abstractmethod
    def push(self, value: int):
        """Push value back in container"""
        pass

    @abstractmethod
    def insert(self, value: int, index: int):
        """Insert value in position"""
        pass

    @abstractmethod
    def pop(self):
        """Pop back and retrieve value"""
        pass

    @abstractmethod
    def remove(self, index: int):
        """Remove and retrieve value by position"""
        pass

    @abstractmethod
    def remove_value(self, value: int, n: int = 1):
        """Remove and retrive n values by value"""
        pass

    @abstractmethod
    def get(self, index: int):
        """Get value by position"""
        pass

    @abstractmethod
    def merge(self, other_array):
        """Append in back another container"""
        pass

    @abstractmethod
    def replace(self, value: int, index: int):
        """Replace value by index"""
        pass

    @abstractmethod
    def find(self, value: int):
        """Retrieve index of first value"""
        pass

    @abstractmethod
    def reverse(self):
        """Reverse container"""
        pass

    @abstractmethod
    def to_list(self) -> list[int]:
        """Reverse container"""
        pass
