from typing import Any
from abc import ABC, abstractmethod
from organelle_segmenter_plugin.core.state import State
from organelle_segmenter_plugin.core.view import View
from qtpy.QtWidgets import QMessageBox
from organelle_segmenter_plugin.core._interfaces import IApplication, IRouter
from organelle_segmenter_plugin.core.viewer_abstraction import ViewerAbstraction


class Controller(ABC):
    def __init__(self, application: IApplication):
        if application is None:
            raise ValueError("application")
        self._application = application

    @abstractmethod
    def index(self):
        pass

    def cleanup(self):
        """
        Perform cleanup operations such as disconnecting events
        Override in child class if needed
        """
        pass

    @property
    def state(self) -> State:
        """
        Get the application State object
        """
        return self._application.state

    @property
    def router(self) -> IRouter:
        """
        Get the application Router
        """
        return self._application.router

    @property
    def viewer(self) -> ViewerAbstraction:
        """
        Get the Napari viewer (abstracted)
        """
        return self._application.viewer

    def load_view(self, view: View, model: Any = None):
        """
        Loads the given view
        :param: view: the View to load
        """
        return self._application.view_manager.load_view(view, model)

    def show_message_box(self, title: str, message: str):
        """
        Display a pop up message box
        :param: title: Message box title
        :param: message: message body to display
        """
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        return msg.exec()
