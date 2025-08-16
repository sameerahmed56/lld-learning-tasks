from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def on_click(self):
        pass


class MacButton(Button):

    def on_click(self):
        return "Mac button is clicked"


class WindowsButton(Button):

    def on_click(self):
        return "Windows button is clicked"


class Dialog(ABC):

    @abstractmethod
    def create_button(self):
        pass

    def render_button(self):
        button = self.create_button()
        return f"Dialog renders a button that says: '{button.on_click()}'"


class MacDialog(Dialog):

    def create_button(self):
        return MacButton()


class WindowsDialog(Dialog):

    def create_button(self):
        return WindowsButton()


def initialize_dialog(os_type: str) -> Dialog:
    if os_type == 'mac':
        return MacDialog()
    if os_type == 'windows':
        return WindowsDialog()

    raise ValueError('Not Supported OS Type')


mac_application_dialog = initialize_dialog('mac')
print(mac_application_dialog.render_button())

windows_application_dialog = initialize_dialog('windows')
print(windows_application_dialog.render_button())
