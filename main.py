# noinspection PyUnresolvedReferences
import sqlite3, sys
from PySide6.QtWidgets import QApplication
# noinspection PyUnresolvedReferences
#from PySide6.QtWidgets import QApplication
# noinspection PyUnresolvedReferences
#from TreeViewer.treeviewer import TreeViewer
#from PySide6.QtGui import QFontDatabase
from basics import WelcomeScreen, FamilyTree, Person, TreeViewer, PersonInputScreen
from datetime import datetime

########################################################### printdatabase ##############################################
def printdatabase():
    conn = sqlite3.connect('database.db')

    cur = conn.cursor()

    cur.execute('''
        SELECT * FROM people
    ''')

    for entry in cur.fetchall():
        print(entry)

    conn.close()

########################################################### exampletree ################################################
def exampletree():

    teofilo = Person( sex='M',
                       dob = datetime(1954,8,22, 0,0,0),
                       first_name='Teofilo',
                       first_last='Berdeja',
                       second_last='Prieto',
                       pob = 'Mexico City')

    marisa = Person( sex='F',
                       dob = datetime(1958,3,25, 0,0,0),
                       first_name='Maria Luisa',
                       first_last='Suarez',
                       second_last='Abiega',
                       pob = 'Mexico City')

    isabel = Person( sex='F',
                       dob = datetime(1988,7,7, 0,0,0),
                       first_name='Isabel',
                       first_last='Berdeja',
                       second_last='Suarez',
                       pob = 'Mexico City')

    ines = Person( sex='F',
                       dob = datetime(1989,8,23, 0,0,0),
                       first_name='Ines',
                       first_last='Berdeja',
                       second_last='Suarez',
                       pob = 'Mexico City')

    belen = Person( sex='F',
                       dob = datetime(1991,5,15, 0,0,0),
                       first_name='Belen',
                       first_last='Berdeja',
                       second_last='Suarez',
                       pob = 'Mexico City')

    diego = Person(sex= 'M',
                       dob = datetime(1993,5,4,0,0,0),
                       first_name = 'Diego',
                       first_last='Berdeja',
                       second_last='Suarez',
                       pob = 'Mexico City' )

    ana = Person( sex='F',
                       dob = datetime(1994,9,3, 0,0,0),
                       first_name='Ana',
                       first_last='Berdeja',
                       second_last='Suarez',
                       pob = 'Mexico City')

    mytree = FamilyTree(root= diego)

    mytree.add_member(person= teofilo, relationship= 'father', member = diego)
    mytree.add_member(person=marisa, relationship='mother', member=diego)
    mytree.modify_relationship(subject_member=teofilo, relationship='spouse', object_member=marisa)

    mytree.add_member(person=isabel, relationship='child', member=teofilo)
    mytree.modify_relationship(subject_member=isabel, relationship='child', object_member=marisa)

    mytree.add_member(person=ines, relationship='child', member=teofilo)
    mytree.modify_relationship(subject_member=ines, relationship='child', object_member=marisa)

    mytree.add_member(person=belen, relationship='child', member=teofilo)
    mytree.modify_relationship(subject_member=belen, relationship='child', object_member=marisa)

    mytree.add_member(person=ana, relationship='child', member=teofilo)
    mytree.modify_relationship(subject_member=ana, relationship='child', object_member=marisa)

    return mytree

########################################################### Tree Viewer App ############################################
def viewer( tree ):

    application = QApplication(sys.argv)

    tree_viewer = TreeViewer(tree)

    tree_viewer.show()

    sys.exit(application.exec_())

########################################################### Tree Viewer App ############################################
def welcome( ):

    application = QApplication(sys.argv)

    welcome_screen = WelcomeScreen()

    welcome_screen.show()

    sys.exit(application.exec_())

########################################################### Person Input App ###########################################
def inputperson( ):

    application = QApplication(sys.argv)

    input_screen = PersonInputScreen()

    input_screen.show()

    sys.exit(application.exec_())

########################################################### Experiments ################################################

welcome()

if False:
    mytree = exampletree()

    diego = mytree.root()

    teofilo = mytree.father(diego)

    personinputscreen = inputperson()