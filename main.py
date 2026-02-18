# noinspection PyUnresolvedReferences
import sqlite3, sys
# noinspection PyUnresolvedReferences
#from PySide6.QtWidgets import QApplication
# noinspection PyUnresolvedReferences
#from TreeViewer.treeviewer import TreeViewer
# noinspection PyUnresolvedReferences
#from PySide6.QtGui import QFontDatabase
from backend import *
import datetime

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
                       dob = datetime.datetime(1954,8,22, 0,0,0),
                       first_name='Teofilo',
                       first_last='Berdeja',
                       second_last='Prieto',
                       pob = 'Mexico City')

    marisa = Person( sex='F',
                       dob = datetime.datetime(1958,3,25, 0,0,0),
                       first_name='Maria Luisa',
                       first_last='Suarez',
                       second_last='Abiega',
                       pob = 'Mexico City')

    isabel = Person( sex='F',
                       dob = datetime.datetime(1988,7,7, 0,0,0),
                       first_name='Isabel',
                       first_last='Berdeja',
                       second_last='Suarez',
                       pob = 'Mexico City')

    ines = Person( sex='F',
                       dob = datetime.datetime(1989,8,23, 0,0,0),
                       first_name='Ines',
                       first_last='Berdeja',
                       second_last='Suarez',
                       pob = 'Mexico City')

    belen = Person( sex='F',
                       dob = datetime.datetime(1991,5,15, 0,0,0),
                       first_name='Belen',
                       first_last='Berdeja',
                       second_last='Suarez',
                       pob = 'Mexico City')

    diego = Person(sex= 'M',
                       dob = datetime.datetime(1993,5,4,0,0,0),
                       first_name = 'Diego',
                       first_last='Berdeja',
                       second_last='Suarez',
                       pob = 'Mexico City' )

    ana = Person( sex='F',
                       dob = datetime.datetime(1994,9,3, 0,0,0),
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



    return mytree

########################################################### Experiments ################################################

mytree = exampletree()

for item in mytree.members():
    print(item)

if False:
    for item in mytree.members():
        print(item)

    mytree.save(overwrite=True)

    loadedtree = FamilyTree(file='database.db')

    for item in loadedtree.members():
        print(item)


    diego = tree.root()

    papa = tree.add_father(teofilo, diego)
    mama = tree.add_mother(marisa, diego)
    print(type(mama))
# tree.modify_relationship(mama,'spouse', papa)

#isa = tree.add_child(isabel, papa)
#tree.modify_relationship(isa,'child',mama)

    for item in tree.collectfamily():
        print(item)

    ana = Person(sex= 'M',
                 dob = datetime.datetime(1993,5,4,0,0,0), first_name = 'Ana', first_last='Berdeja', second_last='Suarez', pob = 'Mexico City' )



    tree = FamilyTree(root=diego)

    tree.add_member( person = papa, relationship = 'father', member = tree.root())




    tree.save(overwrite = True)

    printdatabase()


