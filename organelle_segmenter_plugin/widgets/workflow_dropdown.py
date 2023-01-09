from typing import List

# from aicssegmentation.workflow import WorkflowDefinition
from infer_subc_2d.workflow import WorkflowDefinition


from qtpy.QtWidgets import (
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QWidget,
)

from qtpy.QtGui import QIcon, QPixmap, QImage
from qtpy import QtCore
from qtpy.QtCore import Signal

from organelle_segmenter_plugin.widgets.form import Form, FormRow
from organelle_segmenter_plugin._style import PAGE_CONTENT_WIDTH, Style

# # JAH
# from qtpy.QtGui import QStandardItem, QStandardItemModel
# from organelle_segmenter_plugin.util.ui_utils import UiUtils


class WorkflowDropDown(QWidget):

    """
    A widget containing buttons for workflows. ()

    Params:
        workflow_defs (List[WorkflowDefinition]): List of
            workflow definitions to display as buttons
    """

    workflowSelected = Signal(str)  # signal: emitted when a workflow is selected

    def __init__(self, workflows: List[WorkflowDefinition] = None):
        super().__init__()
        self._workflow_definitions = workflows

        if workflows is not None:
            self.load_workflows(workflows)

    @property
    def workflow_definitions(self) -> List[WorkflowDefinition]:
        return self._workflow_definitions

    def load_workflows(self, workflows: List[WorkflowDefinition]):
        """
        Load given Workflow definitions and rebuild the grid
        """
        if workflows is None:
            raise ValueError("workflows")

        self._workflow_definitions = workflows

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)  # reset setLayout

        self._workflows = workflows

        ## LABELS + BUTTONS
        self._add_labels()
        self._add_buttons(workflows)  # ACTUALLY MAKE A DROPDOWN

    def _add_labels(self):
        """
        Add widgets and set the layout for the Step 3 instructions and the workflow buttons
        """
        self.step_3_label = QLabel("3.")
        self.step_3_label.setAlignment(QtCore.Qt.AlignTop)
        self.step_3_instructions = QLabel("Choose your worfklow .....")
        self.step_3_instructions.setWordWrap(True)

        step_3 = QWidget()
        step_3.setLayout(Form([FormRow(self.step_3_label, self.step_3_instructions)], (0, 0, 11, 0)))

        self.step_3_instructions.setObjectName("step3InstructionsDisabled")
        self.layout().addWidget(step_3)

        # Row of text labeling the columns of workflow images
        self.column_labels = QWidget()
        column_layout = QHBoxLayout()
        column_layout.setContentsMargins(11, 11, 11, 0)
        self.column_labels.setLayout(column_layout)

        image_input_label = QLabel("prebuilt workflows")
        image_input_label.setAlignment(QtCore.Qt.AlignCenter)
        # segmentation_output_label = QLabel("right column")
        # segmentation_output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.column_labels.layout().addWidget(image_input_label)
        # self.column_labels.layout().addWidget(segmentation_output_label)

        self.column_labels.setFixedWidth(PAGE_CONTENT_WIDTH)
        self.column_labels.setObjectName("columnLabelsDisabled")
        self.layout().addWidget(self.column_labels, alignment=QtCore.Qt.AlignCenter)

    def _add_buttons(self, workflows: List[WorkflowDefinition]):
        """
        Add all buttons given a List of WorkflowDefinitions
        """

        # layout = QHBoxLayout()
        # layout.setSpacing(5)
        for workflow in workflows:
            button = QPushButton(workflow.name)
            # button.setFixedWidth(240)
            button.setToolTip(workflow.name)
            button.setEnabled(False)
            button.setObjectName(workflow.name)
            button.clicked.connect(self._workflow_button_clicked)
            self.layout().addWidget(button)
        #     layout.addWidget(button)

        # self._layout.addLayout(layout)

    def setEnabled(self, enabled: bool) -> None:
        super().setEnabled(enabled)
        if enabled:
            self.column_labels.setObjectName("columnLabels")
            self.step_3_instructions.setObjectName("step3Instructions")
            self.setStyleSheet(Style.get_stylesheet("main.qss"))

            self._enable_buttons()
        else:
            self.column_labels.setObjectName("columnLabelsDisabled")
            self.step_3_instructions.setObjectName("step3InstructionsDisabled")
            self.setStyleSheet(Style.get_stylesheet("main.qss"))

            self._disable_buttons()

    def _enable_buttons(self):
        """
        Enable all buttons in the widget
        """
        for button in self.findChildren(QPushButton):
            button.setEnabled(True)

    def _disable_buttons(self):
        """
        Disable all buttons in the widget
        """
        for button in self.findChildren(QPushButton):
            button.setDisabled(True)

    def _workflow_button_clicked(self, checked: bool):
        """
        Handle click of a workflow thumbnail button
        """
        self.workflowSelected.emit(self.sender().objectName())
