from abc import ABC, abstractmethod

class VisualizationBase(ABC):

    @abstractmethod
    def build(self):
        pass

    @abstractmethod
    def to_html(self):
        pass
