import os
import bisect                      # Oredered lists.

# noinspection PyUnresolvedReferences
import matplotlib, numpy           # Maths and plots.
# noinspection PyUnresolvedReferences
import mpl_toolkits.basemap, basemap  # Map plotting.
import sqlite3 # Databases.
from pandas.io.common import file_exists
# noinspection PyUnresolvedReferences
from datetime import datetime, timedelta

########################################################### Person Class ###############################################
class Person:
    """
    Instances of this class keep track of a person's natal information. They are immutable. They are analogues of positions
    in the positional list ADT.
    """

    __slots__ = ( '_name', '_first_last', '_second_last', '_sex', '_dob', '_pob')

    ################################################################ Public Methods ####################################
    def __init__(self, sex = None, dob = None, first_name = None, first_last = None, second_last = None, pob = None):

        # If not enough data is provided, we launch input prompt.
        if sex is None or dob is None or first_name is None or ( second_last is None and first_last is None):

            self._input_data()

        else:

            self._name = first_name

            self._first_last = first_last

            self._second_last= second_last

            self._sex = sex

            if not isinstance(dob, datetime): raise ValueError('Must provide a datetime object for dob.')

            self._dob = dob

            self._pob = pob



    def __str__(self): # Returns name in string format.

        response = self._name

        if self._first_last: response += ' ' + self._first_last

        if self._second_last: response += ' ' + self._second_last

        return response


    # Hash depends on immutable parameters.
    def __hash__(self):

        return hash( (self._name, self._first_last, self._second_last, self._sex, self._dob, self._pob) )

    # We compare people through their dobs.
    def __lt__(self, other):

        if not isinstance(other, Person):

            return NotImplemented

        else:

            return self.dob() < other.dob()

    def name(self): return self._name

    def first_surname(self): return self._first_last

    def second_surname(self): return self._second_last

    def dob(self): return self._dob

    def pob(self): return self._pob

    def sex(self): return self._sex

    def is_male(self): return self.sex() == 'M'

    ############################################################ Private Utilities  ####################################
    def _input_data(self):

        self._name = input('Please enter first name:\n')

        self._first_last = input('Please enter first surname:\n')

        self._second_last = input('Please enter second surname:\n')

        self._sex = input('Please enter sex (M/F):\n')

        if input('Would you like to specify time of day of birth? (Y/N):\n') == 'Y':

            self._dob = datetime( year = int(input('Please input birth year:\n')),
                                  month = int(input('Please input birth month:\n')),
                                  day = int(input('Please input birth day:\n')),
                                  hour = int(input('Please input birth hour:\n')),
                                  minute = int(input('Please input birth minute:\n')))

        else:

            self._dob = datetime(year=int(input('Please input birth year:\n')),
                                 month=int(input('Please input birth month:\n')),
                                 day=int(input('Please input birth day:\n')),)

############################################################ Event Class ###############################################
class Event:
    """
    Instances of this class keep track of what, when, where, and a note on the event. Designed to be immutable.
    """

    __slots__ = ('_title', '_date', '_place', '_note') # Slots prevents creation of dict and saves some space.

    ############################################################ Public Methods ########################################

    def __init__(self, title, date, place = None, note = None):


        if title is None or date is None or place is None:

            self._input_data()

        else:

            self._title = title

            # Date must be datetime object.
            if not isinstance(date, datetime): raise ValueError('Must provide a datetime object for date.')

            self._date = date

            self._place = place  # Inmutable, for hashing purposes.

            self._note = note

    # Events should be compared according to their dates.
    def __lt__(self, other):
        if not isinstance(other, Event):

            return NotImplemented

        else:

            return self.when() < other.when()

    def __eq__(self, other): # Events should be conisdered equal if at most they only differ in the note.

        if not isinstance(other, Event):

            return NotImplemented

        else:

            return self.when() == other.when() and self.where() == other.where() and self.what() == other.what()

    def __hash__(self): return hash( (self.what(), self.when(), self.where()) )

    def __str__(self): return self.what()

    def what(self): return self._title

    def when(self): return self._date

    def where(self): return self._place

    def notes(self): return self._note

    ############################################################ Private Methods #######################################
    def _input_data(self):

        self._title = input('Please enter title:\n')

        if input('Would you like to specify a time? (Y/N):\n') == 'Y':

            self._date = datetime( year = int(input('Please input year:\n')),
                                   month = int(input('Please input month:\n')),
                                   day = int(input('Please input day:\n')),
                                   hour = int(input('Please input hour:\n')),
                                   minute = int(input('Please input minute:\n')))

        else:

            self._date = datetime(year=int(input('Please input birth year:\n')),
                                 month=int(input('Please input birth month:\n')),
                                 day=int(input('Please input birth day:\n')),)

        self._place = input('Please enter a location:\n')

        self._note = input('Please enter a note:\n')

################################################# PruningException Class ###############################################
class DisconnectionException(Exception):
    """
    Custom exception class to handle disconnected trees.
    """
    def __init__(self, disconnected_member, msg= '' ):
        super().__init__( self, msg)
        self._disconnected_member = disconnected_member

############################################################### Family Tree Class ######################################
class FamilyTree:

    ########################################################### Nested _Member Class ####################################
    class _Member:
        """
        Instances of this class keep track of a person's basic information as well as their history. These are the nodes
        of the tree.
        """

        ############################################################ Public Methods ####################################
        def __init__(self, person = None, sex = None, dob = None, first_name = None, first_last = None,
                     second_last = None, pob=None, father=None, mother=None, children=None, spouse=None):
            """
            Underlying Person instance handles the case in which insufficient data is provided.
            :param person: Person instance.
            :param sex: char.
            :param dob:
            :param first_name:
            :param first_last:
            :param second_last:
            :param pob:
            :param father: _Member instance.
            :param mother: _Member instance.
            :param children: List of _Member instances.
            :param spouse: _Member instance.
            """

            # A Person instance may be provided as a basis for the _Member.
            if person is None:

                # This iniialization handles the case in which insufficient data is provided.
                self.person = Person(sex=sex, dob=dob, first_name=first_name, first_last=first_last,
                                     second_last=second_last, pob=pob)

                # List of events sorted according to time. We add birthday upon init.
                self._history = [Event(title='Birth', date=dob, place=pob)]

            elif not isinstance(person, Person):

                raise TypeError('person must be an instance of Person.')

            else:

                self.person = person

                self._history = [Event(title='Birth', date=person.dob(), place=person.pob())]

            # Father, mother, and spouse are _Member instances.
            self._father = father

            self._mother = mother

            self._spouse = spouse

            if children is None:

                self._children = list()

            else:

                self._children = children

        # Hash function depends on immutable characteristics.
        def __hash__(self):

            return hash( self.person )

        def add_event( self, event ):  # Sorts an event into _history.

            if isinstance(event, Event):

                bisect.insort_right(self._history, event)  # We use bisect for efficiency.

            else:

                raise TypeError('Event must be an Event object.')

        def tell_history(self):  # Returns a time-ordered iteration of history events.

            for item in self._history:

                yield item

        # The following methods are public because they are accessed by FamilyTree instances. Since _Member is a
        # private class, these methods are not accessible by a user. Therefore, they do not check for valid membership.

        def add_child(self, new_child, is_relative = False ):

            # We use bisect for efficiency.
            bisect.insort_right( self._children, new_child )

            # We make sure relatives are consistently connected.
            if not is_relative: new_child.replace_father(self, is_relative = True)

            return new_child

        def remove_child(self, child, is_relative = False):

            self._children.remove( child )

            if not is_relative: child.remove_parent(self, is_relative = True)

            return child

        def remove_parent(self, parent, is_relative = False):

            if parent is self.father():

                self.replace_father( new_father = None, is_relative = is_relative )

            if parent is self.mother():

                self.replace_mother(new_mother=None, is_relative = is_relative)

        def replace_father(self, new_father, is_relative = False ):

            # Failsafe in case of redundancy.
            if new_father is self._father:

                return new_father

            # We record old father.
            old_father = self._father

            # We connect new father.
            self._father = new_father

            # If relationship operation was initiated by this function...
            if new_father is not None and not is_relative:
                # We call its counterpart, specifying we initiated the function.
                new_father.add_child( self, is_relative=True )

            if old_father is not None:
                old_father.remove_child( self, is_relative=True )

            return old_father

        def replace_mother(self, new_mother, is_relative = False ):

            # Failsafe in case of redundancy.
            if new_mother is self._mother:
                return new_mother

            # We record old mother.
            old_mother = self._mother

            # We connect new mother.
            self._mother = new_mother

            # If relationship operation was initiated by this function...
            if new_mother is not None and not is_relative:

                # We call its counterpart, specifying we initiated the function.
                new_mother.add_child(self, is_relative=True)

            if old_mother is not None:

                old_mother.remove_child( self, is_relative=True )

            return old_mother

        def replace_spouse(self, new_spouse, is_relative = False ):
            """
            Turns Person into _Member, makes appropriate connections to self, and checks whether old spouse is not
            disconnected from _root.
            """

            # Failsafe in case of redundancy.
            if new_spouse is self._spouse:
                return new_spouse

            # We record old spouse.
            old_spouse = self._spouse

            # We connect new spouse.
            self._spouse = new_spouse

            # If relationship operation was initiated by this function...
            if new_spouse is not None and not is_relative:

                # We call its counterpart, specifying we initiated the function.
                new_spouse.replace_spouse(self, is_relative=True)

            return old_spouse

        def spouse(self):

            return self._spouse

        def father(self):

            return self._father

        def mother(self):

            return self._mother

        def children(self):

            return self._children

    ########################################################## Public Methods ##########################################
    def __init__( self, root = None, file = None, sprout = None):
        """
          Keeps track and maintains integrity of a collection of _Member objects.
          :param root: Person instance.
          :param file: .db
          :param sprout: _Member instance belonging to another FamilyTree instance. For cutting purposes.
        """

        # This is a set of _Member instances.
        self._members = set()

        # Both tree, root are provided.
        if file is not None and root is not None:

            raise ValueError('Exactly one of root, file must be provided.')

        # Tree is empty and database is provided.
        elif file is not None and root is None:

            self.load(file)

        # Only root is provided.
        elif file is None and root is not None:

            self._root = self._Member( person=root )

            self._members.add( self._root )

        # Sprout is _Member of another FamilyTree, provided as root. For cutting purposes.
        elif sprout is not None:

            self._root = sprout

            self._members.add( sprout )

        # Nothing is provided
        else:

            print('Please provide Tree Root\'s personal information.\n')

            self._root = self._Member()

            self._members.add( self._root )

    def __len__(self):

        return len(self._members)

    def members(self):

        for member in self._members: yield member.person

    def validate(self, person):

        if person in self.members():

            return True

        else:

            return False

    def save( self, filename = 'database.db', overwrite = False ):

        if file_exists(filename) and not overwrite:

            raise ValueError('File already exists.')

        if file_exists(filename):

            os.remove(filename)

        conn = sqlite3.connect(filename)

        cursor = conn.cursor()

        # We iterate over each person in the tree and prepare the date for entry into the database.

        save_data = []

        i = 0  # person_id counter.

        for member in self._members:

            # We collect natal info. Last entry records Root.
            entry = [i, member.person.name(), member.person.first_surname(), member.person.second_surname(),
                     member.person.sex(), member.person.dob(), member.person.pob(), None, None, None,
                     member.person == self._root]

            # We look for spouse and parents.
            j = 0  # relative_id counter

            for potential_relative in self._members:

                # If potential relative is candidate's father...
                if member.father() is potential_relative: entry[7] = j

                # If potential relative is candidate's mother...
                if member.mother() is potential_relative: entry[8] = j

                # If potential relative is candidate's spouse...
                if member.spouse() is potential_relative: entry[9] = j

                # We increase the relative_id counter.
                j += 1

            # We append the entry and increase the person_id counter.
            save_data.append( entry )

            i += 1

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS people (
                            person_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            fathers_name TEXT,
                            mothers_name TEXT,
                            sex CHAR(1) NOT NULL,
                            dob DATETIME NOT NULL,
                            pob TEXT,
                            father INTEGER,
                            mother INTEGER,
                            spouse INTEGER,
                            is_root BOOLEAN NOT NULL DEFAULT FALSE,
                            foreign key (father) references people (person_id), 
                            foreign key (mother) references people (person_id),
                            foreign key (spouse) references people (person_id)
                            )""")

        cursor.executemany("""INSERT INTO people VALUES(?,?,?,?,?,?,?,?,?,?,?)""", save_data)

        conn.commit()

        conn.close()

    def load( self, filename = 'database.db' ):

        # If file doesn't exist...
        if not file_exists( filename ): raise ValueError( 'File ' + filename + ' does not exist.' )

        # We open a connection and set up a cursor...
        conn = sqlite3.connect( filename )

        cursor = conn.cursor()

        # We fetch everyone and add them to a list of _Member objects, along with their personal id.
        # The people set will help us establish relationships.
        people = set()

        for entry in cursor.execute('SELECT * FROM people').fetchall():

            member = FamilyTree._Member(first_name=entry[1], first_last=entry[2],
                                        second_last=entry[3], sex=entry[4], dob=entry[5], pob=entry[6])

            # We detect and set _root. The 10th column is True only for _root.
            if entry[10]:

                self._root = member

            # We add member to members' list and to people set.
            self._members.add( member )

            people.add((entry[0], member))

        # We establish parentage and marriage.
        for parent_key, potential_parent in people:

            if potential_parent.person.is_male():

                # father column stores key of father.
                response_parent = cursor.execute("""  SELECT person_id FROM people WHERE father = ? """,
                                                 (parent_key,)).fetchall()

            else:

                response_parent = cursor.execute("""  SELECT person_id FROM people WHERE mother = ? """,
                                                 parent_key).fetchall()

            response_spouse = cursor.execute("""  SELECT person_id FROM people WHERE spouse = ? """,
                                             (parent_key,)).fetchall()


            conn.close()

            for candidate_key, candidate in people:

                # We add the candidate to the FamilyTree's members' list.
                self._members.add( candidate )

                # We establish male parentage. Note that replacing candidate's parent automatically adds candidate as parent's child.
                if candidate_key in response_parent and potential_parent.person.is_male():

                    candidate.replace_father(potential_parent)

                # We establish female parentage.
                elif candidate_key in response_parent and not potential_parent.person.sex().is_male():

                    candidate.replace_mother(potential_parent)

                # We establish marriages. Naturally, there will be a two-fold redundant call per marriage in tree.
                # Failsafes that mitigate this effect have been put in place.
                if candidate_key in response_spouse:

                    candidate.replace_spouse(potential_parent)

    def modify_relationship( self, subject_member, relationship, object_member, cut = False ):
        """
        subject member is relationship of object member.
        If cut is set to True and this function disconnects tree, compliment of root will be stored in new .db and returned.
            Otherwise, a DisconnectionError is raised.
        :param subject_member:
        :param relationship:
        :param object_member:
        :param cut:
        :return:
        """

        if not self.validate(subject_member):

            raise ValueError( str(subject_member) + ' is not a member of this tree.')

        if not self.validate(object_member):

            raise ValueError(str(object_member) + ' is not a member of this tree.')

        if relationship == 'father':

            # We disconnect _M <-> old father.
            oldfather = object_member.replace_father( subject_member )

            # If old father is disconnected...
            if oldfather is not None and oldfather not in self.collectfamily():

                # If we are allowed to cut the tree...
                if cut:

                    return self._cut(new_root=oldfather)

                # If we are not allowed to cut...
                else:

                    # We reconnect _M <-> old father.
                    object_member.replace_father( oldfather )

                    raise DisconnectionException( disconnected_member=oldfather )

            return oldfather


        if relationship == 'mother':

            oldmother = object_member.replace_mother(subject_member)

            if oldmother is not None and oldmother not in self.collectfamily():

                # If we are allowed to cut the tree...
                if cut:

                    return self._cut(new_root=oldmother)

                # If we are not allowed to cut...
                else:

                    object_member.replace_father(oldmother)

                    raise DisconnectionException(disconnected_member=oldmother)

            return oldmother

        if relationship == 'spouse':

            oldspouse = object_member.replace_spouse(subject_member)

            if oldspouse is not None and oldspouse not in self.collectfamily():

                # If we are allowed to cut the tree...
                if cut:

                    return self._cut(new_root=oldspouse)

                # If we are not allowed to cut...
                else:

                    object_member.replace_father(oldspouse)

                    raise DisconnectionException(disconnected_member=oldspouse)

            return oldspouse

        if relationship == 'child':

            if not object_member.is_male():

                oldmother = subject_member.replace_mother( new_mother = object_member )

                if oldmother is not None and oldmother not in self.collectfamily():
                    # If we are allowed to cut the tree...
                    if cut:

                        return self._cut(new_root=oldmother)

                    # If we are not allowed to cut...
                    else:

                        subject_member.replace_father(oldmother)

                        raise DisconnectionException(disconnected_member=oldmother)

                return oldmother

            else:

                oldfather = subject_member.replace_father( new_father = object_member)

                if oldfather is not None and oldfather not in self.collectfamily():
                    # If we are allowed to cut the tree...
                    if cut:

                        return self._cut(new_root=oldfather)

                    # If we are not allowed to cut...
                    else:

                        subject_member.replace_father(oldfather)

                        raise DisconnectionException(disconnected_member=oldfather)

                return oldfather

        else:

            raise ValueError(str(relationship) + ' is not a valid relationship.')

    def add_member( self, person, relationship, member, cut = False ):
        """
        person is relationship of member.
        Incorporates Person instance into Tree as a _Member instance. Checks whether tree is disconnected as a result.
        """

        if not self.validate(member):

            raise ValueError( str(member) + ' is not a member of this tree.')

        potential_member = self._Member( person = person )

        if relationship == 'father':

            # We replace member's father.
            oldfather = member.replace_father( potential_member )

            # We check whether old father is disconnected as a result. If so, we raise an error.
            if oldfather is not None and oldfather not in self.collectfamily():

                # If we are allowed to cut the tree...
                if cut:

                    return self._cut(new_root=oldfather)

                # If we are not allowed to cut...
                else:

                    member.replace_father(oldfather)

                    raise DisconnectionException(disconnected_member=oldfather)

            # If Person is added without disconnecting tree, we add it to _members.

            self._members.add( potential_member )

            return oldfather

        if relationship == 'mother':

            # We replace member's mother.

            oldmother = member.replace_mother(potential_member)

            # We check whether old father is disconnected as a result. If so, we raise an error.

            if oldmother is not None and oldmother not in self.collectfamily():

                # If we are allowed to cut the tree...

                if cut:

                    return self._cut(new_root=oldmother)


                # If we are not allowed to cut...

                else:

                    member.replace_mother(oldmother)

                    raise DisconnectionException(disconnected_member=oldmother)

            # If Person is added without disconnecting tree, we add it to _members.

            self._members.add(potential_member)

            return oldmother

        if relationship == 'spouse':

            # We replace member's father.

            oldspouse = member.replace_spouse(potential_member)

            # We check whether old father is disconnected as a result. If so, we raise an error.

            if oldspouse is not None and oldspouse not in self.collectfamily():

                # If we are allowed to cut the tree...

                if cut:

                    return self._cut(new_root=oldspouse)


                # If we are not allowed to cut...

                else:

                    member.replace_spouse(oldspouse)

                    raise DisconnectionException(disconnected_member=oldspouse)

            # If Person is added without disconnecting tree, we add it to _members.

            self._members.add(potential_member)

            return oldspouse

        if relationship == 'child':

            if not potential_member.person.is_male():

                oldmother = potential_member.replace_mother(new_mother=member)

                if oldmother is not None and oldmother not in self.collectfamily():

                    # If we are allowed to cut the tree...

                    if cut:

                        return self._cut(new_root=oldmother)


                    # If we are not allowed to cut...

                    else:

                        potential_member.replace_father(oldmother)

                        raise DisconnectionException(disconnected_member=oldmother)

                return oldmother


            else:

                oldfather = potential_member.replace_father(new_father=member)

                if oldfather is not None and oldfather not in self.collectfamily():

                    # If we are allowed to cut the tree...

                    if cut:

                        return self._cut(new_root=oldfather)


                    # If we are not allowed to cut...

                    else:

                        potential_member.replace_father(oldfather)

                        raise DisconnectionException(disconnected_member=oldfather)

                return oldfather

        else:
            raise ValueError(relationship + ' is not a valid relationship.')

    def add_father(self, newfather, member):
        return self.add_member(person=newfather, relationship='father', member=member)

    def add_mother(self, newmother, member):
        return self.add_member(person=newmother, relationship='mother', member=member)

    def add_parent(self, newparent, member):

        if newparent.is_male():
            return self.add_father( newfather=newparent, member=member )
        else:
            return self.add_mother( newmother=newparent, member=member )

    def add_spouse(self, newspouse, member):
        return self.add_member(person=newspouse, relationship='spouse', member=member)

    def add_child(self, newchild, member):
        return self.add_member(person=newchild, relationship='child', member=member)

    def root(self):
        return self._root

    def ancestors(self, starting_position = None):
        """
        Collection tool. Yields an iteration of _Members that are ancestors of starting position.
        Starting position defaults to root.
        """

        if starting_position is None: starting_position = self.root()

        yield from self._ascendance( current_position = starting_position,  )

    def descendants(self, starting_position = None):
        """
        Collection tool. Yields an iteration of _Members that are descendants of starting position.
        Starting position defaults to root.
        """

        if starting_position is None: starting_position = self.root()

        yield from self._descendance( current_position=starting_position )

    # noinspection PyMethodMayBeStatic

    def siblings( self, person ):
        """Produces an iteration of siblings, without person."""

        # We initialize an empty set to avoid duplicates.
        siblings = set()

        # We yield father's children.
        if person.father() is not None and len(person.father().children()) != 0:
            for child in person.father().children():
                if child not in siblings:
                    siblings.add(child)
                    yield child

        # We yield mother's children.
        if person.mother() and len(person.father().children()) != 0:
            for child in person.mother().children():
                if child not in siblings:
                    siblings.add(child)
                    yield child

        try:
            siblings.remove(person)
        except KeyError:
            print('fart')

    def collectfamily(self, starting_position = None):
        """
            Collection tool. Yields an iteration of _Members that are reachable from starting position.
            Starting position defaults to root.
        """

        if starting_position is None:
            starting_position = self.root()
        elif starting_position not in self._members:
            raise ValueError(str(starting_position) + ' is not a member of this tree.')

        yield from self._collectall( current_position = starting_position, count = None )

    ########################################################## Private Utilities #######################################

    # Creates database template. Overwrites existing file.
    # noinspection PyMethodMayBeStatic
    def _dbtemplate(self, filename='database.db'):
        if file_exists(filename): os.remove(filename)

        conn = sqlite3.connect(filename)

        cursor = conn.cursor()

        # people is a table that records family members and their parentage and spousal relationships.
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS people (
                    person_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    fathers_name TEXT,
                    mothers_name TEXT,
                    sex CHAR(1) NOT NULL,
                    dob DATETIME NOT NULL,
                    pob TEXT,
                    father INTEGER,
                    mother INTEGER,
                    spouse INTEGER,
                    root BOOLEAN NOT NULL,
                    foreign key (father) references people (person_id), 
                    foreign key (mother) references people (person_id),
                    foreign key (spouse) references people (person_id)
                    )""")
        # Foreign keys are references from other tables; in this case the source is the same table.

        cursor.execute("""   
                                CREATE TABLE events (
                                    event_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    title TEXT NOT NULL,
                                    place TEXT,
                                    date DATE,
                                    time TIME)
                                """)

        # participants is a table that records who was present at each event.
        cursor.execute("""   
                                CREATE TABLE IF NOT EXISTS participants (
                                    person INTEGER NOT NULL,
                                    event INTEGER NOT NULL,
                                    PRIMARY KEY (person, event),
                                    FOREIGN KEY (person) REFERENCES people (person_id), 
                                    FOREIGN KEY (event) REFERENCES events (event_id))
                                """)

        conn.commit()

        conn.close()

    def _cut(self, new_root):
        """
        Internal utility that creates a new FamilyTree instance when an operation results in disconnection.
        :param new_root: _Member belonging to disconnected component of FamilyTree.
        :return:
        """
        # We create a new FamilyTree instance, using new_root as a sprout.
        newtree = FamilyTree( sprout = new_root )

        # We iterate over each of the _Members in the disconnected component....
        for member in self._collectall(current_position = new_root):

            # add them to the new tree...
            newtree._members.add( member )

            # and remove them from the old one...
            self._members.remove( member )

        # Finally, we save the disconnected component and return it.
        newtree.save(filename = 'splinter_' + str(datetime.today().day) + str(datetime.today().minute) + \
                    str(datetime.today().microsecond), overwrite = True)

        return newtree

    def _collectall( self , current_position , count = None):

        """
        Internal utility. Collects _Members of FamilyTree by visiting all of current_position's family iteratively.
        :param current_position:
        :param count:
        :return:
        """

        if count is None: count = set()

        if current_position not in count and current_position in self._members:

            yield current_position

            count.add( current_position )

            if current_position.spouse() is not None:

                yield from self._collectall( current_position = current_position.spouse(), count = count )

            if current_position.mother() is not None:

                yield from self._collectall( current_position = current_position.mother(), count = count )

            if current_position.father() is not None:

                yield from self._collectall(current_position=current_position.father(), count=count)

            for child in current_position.children():

                yield from self._collectall( current_position = child, count = count )

    def _ascendance( self, current_position, is_spouse = False, count = None , start = True):
        """Produces an iteration of starting position's parents, their spouses, and their parents"""

        # Keeps track of items that have already been yielded.
        if count is None: count = set()

        # If we haven't yielded current position
        if current_position not in count:

            if not start:

                yield current_position

                # We add it to count.
                count.add(current_position)

                # We repeat with person's spouse, while preventing double-backing...
                if current_position.spouse() is not None and not is_spouse:
                    yield from self._ascendance(current_position.spouse(), is_spouse=True, start=False, count=count)

            # and repeat with their father...
            if current_position.father() is not None:
                yield from self._ascendance(current_position.father(), start = False, count = count)

            # and repeat with their mother...
            if current_position.mother() is not None:
                yield from self._ascendance(current_position.mother(), start = False, count = count)

    def _descendance( self, current_position, is_spouse = False, star2t = True, count = None ):
        """Produces an iteration of starting position's children, their spouses, and their children."""

        # Keeps track of items that have already been yielded.
        if count is None: count = set()

        # If we haven't yielded current position
        if current_position not in count:

            if not start:

                yield current_position

                # We add it to count.
                count.add(current_position)

                # We recur on person's spouse, while preventing double-backing...
                if current_position.spouse() is not None and not is_spouse and not start:
                    yield from self._descendance(current_position.spouse(), is_spouse=True, start=False, count=count)

            # We recur on each child.
            for child in current_position.children():
                yield from self._descendance(child, start=False, count=count)