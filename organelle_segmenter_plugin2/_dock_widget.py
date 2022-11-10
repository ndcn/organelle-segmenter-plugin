# # Hook specifications: https://napari.org/docs/dev/plugins/hook_specifications.html
# from napari_plugin_engine import napari_hook_implementation

import napari

from organelle_segmenter_plugin2.core.application import Application
from qtpy.QtWidgets import QWidget, QVBoxLayout, QSizePolicy



"""
The class name here gets converted to title case and gets displayed as both the title 
of the plugin window and the title displayed in the app menu dropdown.
"""


class WorkflowEditorWidget(QWidget):  # pragma: no-cover
    def __init__(self, napari_viewer: napari.Viewer):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self._application = Application(napari_viewer, self.layout())
        self._application.router.workflow_selection()  # Initialize first screen


class BatchProcessingWidget(QWidget):
    def __init__(self, napari_viewer: napari.Viewer):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        self.setLayout(QVBoxLayout())
        self._application = Application(napari_viewer, self.layout())
        self._application.router.batch_processing()  # Initialize first screen


# @napari_hook_implementation
# def napari_experimental_provide_dock_widget() -> Union[WorkflowEditorWidget, BatchProcessingWidget]:  # pragma: no-cover
#     return [(WorkflowEditorWidget, {"name": "Workflow editor"}), (BatchProcessingWidget, {"name": "Batch processing"})]
