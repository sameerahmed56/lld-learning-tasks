from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def compile(self):
        pass


class DrivingStrategy(RouteStrategy):

    def compile(self):
        return 'Driving strategy is running'


class WalkingStrategy(RouteStrategy):

    def compile(self):
        return 'Walking strategy is running'


class PublicTransportStrategy(RouteStrategy):

    def compile(self):
        return 'Public transport strategy is running'


class Navigator:

    def __init__(self, strategy: RouteStrategy):
        self.strategy = strategy

    def run_strategy(self):
        return self.strategy.compile()


driving_navigation = Navigator(PublicTransportStrategy())
print(driving_navigation.run_strategy())

walking_navigation = Navigator(WalkingStrategy())
print(walking_navigation.run_strategy())

public_transport_navigation = Navigator(PublicTransportStrategy())
print(public_transport_navigation.run_strategy())
