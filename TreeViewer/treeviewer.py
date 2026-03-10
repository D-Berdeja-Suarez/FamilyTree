from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6.QtGui import QStandardItem, QFont, QColor, QStandardItemModel
from TreeViewer.UI.treeviewer import Ui_mainwwin_treeviewer

################################################### GUI TreeViewer Class ###############################################
class TreeViewer(qtw.QMainWindow, Ui_mainwwin_treeviewer):
    """
        GUI window where trees may be displayed.
    """

    def __init__(self, tree):

        super().__init__()

        self.setupUi(self)

        self._tree = tree

        # Upon opening Tree Viewer, we display root's descendants.

        self._model = self._tree.model_descendants()

        self._update_display()

        #TODO Connect signals and slots.


    # noinspection PyMethodMayBeStatic
    ######################################################### Private Methods ##########################################
    def _update_display(self):

        # TODO Define.

        pass