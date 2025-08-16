from abc import ABC, abstractmethod


class Listener(ABC):

    @abstractmethod
    def update(self, data: str):
        pass


class EmailListener(Listener):

    def __init__(self, email: str):
        self.email = email

    def update(self, data):
        print(f'Sending email with name {data} to {self.email}')


class NotifierManager:

    listeners: dict[str: list[Listener]] = dict()

    def notify(self, event_type: str, data: str):
        event_type_listener = self.listeners.setdefault(event_type, [])
        for listener in event_type_listener:
            listener.update(data)

    def subscribe(self, event_type: str, listener: Listener):
        event_type_listener = self.listeners.setdefault(event_type, [])
        event_type_listener.append(listener)

    def unsubscribe(self, event_type: str, listener: Listener):
        event_type_listener = self.listeners.setdefault(event_type, [])
        event_type_listener.remove(listener)


class YoutubeChannel:
    event_notifier = NotifierManager()

    def subscribe_channel(self, name: str):
        self.event_notifier.notify('subscribe', name)
        print(f'{name} subscribed to channel')

    def unsubscribe_channel(self, name: str):
        self.event_notifier.notify('unsubscribe', name)
        print(f'{name} unsubscribe_channel to channel')


my_youtube_channel = YoutubeChannel()

email_listener = EmailListener('test@gmail.com')
my_youtube_channel.event_notifier.subscribe('subscribe', email_listener)
my_youtube_channel.subscribe_channel('John Doe')
