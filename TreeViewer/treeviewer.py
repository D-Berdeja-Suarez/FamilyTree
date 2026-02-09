from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6.QtGui import QStandardItem, QFont, QColor, QStandardItemModel
from TreeViewer.UI.treeviewer import Ui_mainwwin_treeviewer

class TreeEntry(QStandardItem):
    """
        Customized QStandardItem for display in QTreeView.
    """
    def __init__(self, person, font_size = 12, height = 1, bold_font = False, color = None):
        super().__init__()

        if color is not None:
            fntcolor = color
        elif person.is_male():
            fntcolor = QColor(0,85,255)
        else:
            fntcolor = QColor(255,0,201)

        output = person.name()[0]

        if person.first_surname() is not None:

            output += ' ' + person.first_surname()

        if person.second_surname() is not None:

            output += ' ' + person.second_surname()[0]

        output += ' (' + str(person.dob().year) + '-' + ')'

        fnt = QFont('Avenir', font_size)
        fnt.setBold(bold_font)

        self.setEditable(False)
        self.setForeground(fntcolor)
        self.setFont(fnt)
        self.setText(output)

        self._height = height

################################################### GUI TreeViewer Class ###############################################
class TreeViewer(qtw.QMainWindow, Ui_mainwwin_treeviewer):
    """
        GUI window where trees may be displayed.
    """

    def __init__(self, tree):

        super().__init__()

        self.setupUi(self)

        self._tree = tree

        # We instantiate an empty Item model to store our entries.
        self._model = QStandardItemModel()

        # Upon opening Tree Viewer, we display Root's ascendency.
        self._updatemodel( self._tree.root() )



    # noinspection PyMethodMayBeStatic
    ######################################################### Private Methods ##########################################
    def _updatemodel(self, _position, height = 1,start = True):
        """
        Updates _model such that QTreeView displays starting_position's ancestry.
        :param starting_position: _Member instance.
        :return:
        """

        # If the iteration is starting, we display the item in bold.
        if start:

            root = TreeEntry(person = starting_position, bold_font = True, height = height)

            self._model = QStandardItemModel()

