from PySide6 import QtWidgets as qtw
from PySide6.QtGui import QStandardItem, QFont, QColor
from UI.TreeViewer.treeviewer import Ui_treeviewer
from UI.WelcomeScreen.welcomescreen import Ui_welcomescreen

################################################# GUI Standard Entry Class #################################################
class TreeNode(QStandardItem):
    """
        Customized QStandardItem for display in QTreeView.
    """
    def __init__(self, person, font_size = 12, height = 1, bold_font = False, color = None):
        super().__init__()

        # We store person.
        self._person = person

        # If no color is provided, we default to sex.
        if color is not None:

            fntcolor = color

        elif self._person.is_male():

            fntcolor = QColor(0,85,255)

        else:

            fntcolor = QColor(255,0,201)

        output = self._person.name()

        if self._person.first_surname() is not None:

            output += ' ' + self._person.first_surname()

        if self._person.second_surname() is not None:

            output += ' ' + self._person.second_surname()[0]

        output += ' (' + str(person.dob().year) + ' - ' + '*)'

        fnt = QFont('Avenir', font_size)

        fnt.setBold(bold_font)

        self.setEditable(False)

        self.setForeground(fntcolor)

        self.setFont(fnt)

        self.setText(output)

        self._height = height

    def person(self):

        return self._person

################################################### GUI TreeViewer Class ###############################################
class TreeViewer(qtw.QMainWindow, Ui_treeviewer):

    def __init__(self, tree):

        super().__init__()

        self.setupUi( self )

        # We keep track of the associated tree.
        self._tree = tree

        # Upon opening Tree Viewer, we model, keep track of, and display root's descendants, expanded.

        self._showing_descendants = True

        self._is_expanded = True

        self._model= self._tree.model_descendants()

        self.treeView.setModel(self._model)

        self.treeView.expandAll()

        # We connect slots to signals.

        self.treeView.doubleClicked.connect( self._update )

        self.pb_descendance.clicked.connect(self._descendants_pushed)

        self.pb_ascendance.clicked.connect(self._ascendants_pushed)

        self.pb_expand_all.clicked.connect(self._expand_all_pushed)

        self.pb_collapse_all.clicked.connect(self._collapse_all_pushed)


    # noinspection PyMethodMayBeStatic
    ######################################################### Private Methods ##########################################
    def _update( self, new_centre_index ):

        # doubleClicked signal yields a QModelIndex instance. We retrieve the associated item.

        new_centre = self._model.itemFromIndex(new_centre_index)

        # We move root to double-clicked item.

        self._tree.move_root( new_root = new_centre.person() )

        # We model descendants/ascendants, replace the old model, and update the view.

        if self._showing_descendants:

            self._model = self._tree.model_descendants()

        else:

            self._model = self._tree.model_ascendants()

        self.treeView.setModel(self._model)

        if self._is_expanded:

            self.treeView.expandAll()

        else:

            self.treeView.collapseAll()

    def _descendants_pushed(self):

        self._showing_descendants = True

        self._model = self._tree.model_descendants()

        self.treeView.setModel(self._model)

        if self._is_expanded:

            self.treeView.expandAll()

        else:

            self.treeView.collapseAll()

    def _ascendants_pushed(self):

        self._showing_descendants = False

        self._model = self._tree.model_ascendants()

        self.treeView.setModel(self._model)

        if self._is_expanded:

            self.treeView.expandAll()

        else:

            self.treeView.collapseAll()

    def _expand_all_pushed(self):

        self._is_expanded = True

        self.treeView.expandAll()

    def _collapse_all_pushed(self):

        self._is_expanded = False

        self.treeView.collapseAll()

################################################### GUI WelcomeScreen Class ############################################
class WelcomeScreen(qtw.QMainWindow, Ui_welcomescreen):

    def __init__(self):

        super().__init__()

        self.setupUi( self )
