from abc import ABC, abstractmethod
from typing import List

# --- Observer/Listener Interface (Your Listener is perfect) ---


class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# --- Concrete Observer (Your EmailListener is perfect) ---


class EmailAlertObserver(Observer):
    def __init__(self, email: str):
        self.email = email

    def update(self, message: str):
        print(f"Sending email to {self.email} with message: '{message}'")

# --- Subject Interface (Optional but good practice) ---


class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

# --- Concrete Subject ---
# The YouTubeChannel directly manages its observers.


class YouTubeChannel(Subject):
    def __init__(self, name: str):
        self.name = name
        self._observers: List[Observer] = []
        self._latest_video_title = ""

    def subscribe(self, observer: Observer):
        print(f"'{observer.email}' has subscribed to '{self.name}'.")
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        print(f"'{observer.email}' has unsubscribed from '{self.name}'.")
        self._observers.remove(observer)

    def notify(self):
        print("Notifying all subscribers about the new video...")
        for observer in self._observers:
            observer.update(f"A new video was uploaded to '{self.name}': {self._latest_video_title}")

    def upload_video(self, title: str):
        print(f"\nUploading new video to '{self.name}': {title}")
        self._latest_video_title = title
        self.notify()


# --- Client Code ---
tech_channel = YouTubeChannel("TechWithTom")

# Create subscribers (observers)
subscriber1 = EmailAlertObserver("subscriber1@example.com")
subscriber2 = EmailAlertObserver("subscriber2@example.com")
subscriber3 = EmailAlertObserver("subscriber3@example.com")

# Subscribe them to the channel
tech_channel.subscribe(subscriber1)
tech_channel.subscribe(subscriber2)
tech_channel.subscribe(subscriber3)

# The channel uploads a video, which triggers notification to all subscribers
tech_channel.upload_video("Mastering the Observer Pattern")

# One person unsubscribes
tech_channel.unsubscribe(subscriber2)

# The channel uploads another video
tech_channel.upload_video("Advanced Python Design")
