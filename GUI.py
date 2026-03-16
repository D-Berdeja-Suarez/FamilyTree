from PySide6 import QtWidgets as qtw
from PySide6.QtCore import Signal
from PySide6.QtGui import QStandardItem, QFont, QColor
from UI.TreeViewer.treeviewer import Ui_treeviewer
from UI.WelcomeScreen.welcomescreen import Ui_welcomescreen
from UI.PersonInputScreen.personinputscreen import Ui_personinputscreen
from basics import FamilyTree as FamilyTree
from basics import Person as Person
from datetime import datetime

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

################################################# GUI Standard Entry Class #############################################
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

    ################################################### Public Methods #################################################
    def __init__(self):

        super().__init__()

        self.setupUi( self )

        self.pb_new.pressed.connect( self._new_pressed )

    ################################################### Private Methods ################################################
    def _new_pressed(self):

        self.input_window = PersonInputScreen()

        self.input_window.lab_contextual.setText('Please provide root\'s personal information:')

        self.input_window.show()

################################################### GUI PersonInputScreen Class ########################################
class PersonInputScreen(qtw.QMainWindow, Ui_personinputscreen):

    # Remember: signals must be declared as class variables, not instance variables.
    person_signal = Signal()

    ################################################### Public Methods #################################################
    def __init__(self):

        super().__init__()

        self.setupUi(self)

        # Flag to help us keep track of whether a warning message has been shown to the user.
        self._warning_label = None

        # We add the days of the year to the QtComboBox.
        for i in range(31):

            self.cb_day.addItem(str(i+1))

        # We do the same for the months of the year.
        for month in MONTHS:

            self.cb_month.addItem(month)

        # We connect signals to slots.
        self.pb_done.pressed.connect( self._done_pressed )
        self.pb_clear.pressed.connect( self.close )

    ############################################### Private Methods ####################################################

    def _done_pressed(self):
        """
        Collects personal information and returns a Person instance.
        :return: 0 if not enough information is provided; Person instance if collection is successful.
        """

        # We first collect whatever the user has provided as input, if anything.
        name = self.le_name.text()

        first_last = self.le_first_last.text()

        second_last = self.le_second_last.text()

        day = self.cb_day.currentIndex()+1

        month = self.cb_month.currentIndex()+1

        year = self.sp_year.value()

        if self.rb_male.isChecked():

            sex = 'M'

        else:

            sex = 'F'

        # If user hasn't provided enough information, we display a warning label.
        if name == '' or first_last == '' or (not self.rb_male.isChecked() and not self.rb_female.isChecked()):

            # If we haven't shown a warning label yet, we first have to create it.
            if self._warning_label is None:

                self._warning_label = qtw.QLabel(self.widget)

                self.widget.layout().addWidget(self._warning_label)

            self._warning_label.setText('Please provide a first name, first last name, and sex.')

            return 0

        # If the user hasn't provided a valid birthday, we display a warning label.
        try:

            birthday = datetime(year=year, month=month, day=day)

        except ValueError:

            # If we haven't shown a warning label yet, we first have to create it.
            if self._warning_label is None:

                self._warning_label = qtw.QLabel(self.widget)

                self.widget.layout().addWidget(self._warning_label)

            self._warning_label.setText('Please provide a valid birthday.')

            return 0

        # Should enough information be provided, we create a Person instance.
        person = Person(first_name = name, first_last=first_last, second_last=second_last,dob = birthday, sex=sex)

        # And emit a signal containing it.
        self.person_signal.emit( person )

        # Finally, we close the window.
        self.close()

        return 1