# 🌱 FamilyTree

> *FamilyTree is a passion project that doubles as a showcase of my programming skills.*

## 🎯 What does FamilyTree achieve?

- FamilyTree provides a functional data framework along with user-friendly command-line and graphic interfaces for the purposes of recording and manipulating the history of a collection of inter-related people.

- FamilyTree demonstrates several programing tools and principles that are relevant in the context of data analysis and manipulation, such as:
    - 🧑🏻‍💻 **OBJECT-ORIENTED PROGRAMMING**: Implementation of custom tools using adept combinations of Python's built-in functionality and a collection of custom classes and functions.
    - 💽 **SQL DATABASES**: Light-weight storage of persistent data in SQL databases.
    - ⟫⟫⟫ **ANALYSIS OF ALGORITHMS**: Favourable space-time trade-offs in the implementation of algorithms.
    - ⚜️ **STURDY SOFTWARE DESIGN**: Adhesion to best-practices and use of low over-head safeguards to preserve data integrity.
    - 🪟 **GRAPHICAL USER INTERFACE**: Light-weight and practical design of GUIs for custom packages.

- With FamilyTree, you can create, maintain, and vizualize a database that records any and all of:
  - 🧑‍🧑‍🧒‍🧒 your family history
  - 👑 the history of your favourite monarchic dynasty
  - 💬 the structure of a given language family
  - 🧐 the history of those schools of thought and religions that you find most fascinating


## ✍️ Why did I write this code?

> *My bread and butter is algebraic geometry and physics, where symbolic programing plays a supporting role but remains somewhat removed from the spotlight.*

> *In transitioning to a career in quantitative finance, I wish to implement and showcase my programming skills in a project that is personally fullfilling.*

> *I like history and I like to write code in my free time. This is a way to bring the two together!*


## 🚀 Usage

FamilyTree consists of four interacting classes that provide the basis for most functionality. Here we provide a brief summary of their use and implementation.

🚹 **Person class**
- Instances of this class are ligthweight and immutable. They provide the basis for the identity of a person and they implement a hash method. The necessary data can be input manually. In the absence of the provision of sufficient data upon initialization, a verbose mode is launched. Console and GUI modes are available.

👤 **_Member class**
- This class inherits from the Person class and is not user-accessible. _Member isntances are initialized and maintained by instances of the FamilyTree class.

🗓️ **Event class**
- Instances of this class, which are immutable, record spatial and temporal data associated to an event. Its application programming interface is designed to facilitate visualization in the GUI.

🌱 **FamilyTree class**:
- Instances of this class keep track of a collection of _Member and Event instances that describe the temporal and geographical history of a collection of actors. FamilyTree combines aspects of different tree-like and list-like abstract data types in order to achieve functionality while mainting a reasonable rate of memory and computing time expenditure.
    - It provides access to the data carried by _Member instances


- In order to add a _Member, the tree must be provided with a Person instance along with a relationship to a _Member instance that belongs to the FamilyTree. The FamilyTree instance then checks whether the introduction of the Person into the FamilyTree as a _Member compromises the integrity of the tree---for example, it checks whether the introduction of Daniel as a new father to Sam will result in Sam's father being left childless. If this is the case and the appropriate toggles are turned on, the old FamilyTree instance splices and creates separate instance of FamilyTree in such a way that no information is corrupted: if Daniel is endowed with a new father, a new FamilyTree instance containing Daniel's old father along with the latter's relatives is created.

- The FamilyTree class implements lazy-evaluation iterators that yield its contents.

- 

👤 **_Member class**
- This is a private class that is not to be accessed by the user. _Member instances are intialized by a FamilyTree instance

Person, _Member, and FamilyTree classes
Person is lightweight and provides immutable part that can be hashed
FamilyTree keeps track and preserves integrity of a collection of persons-> member
Access to info balances user friendly-ness, reasonable memory usage, and reasonable checks, such as checking membership
SQL storage: balancing flatness and loading it back into tree

GUI interface: provide more expidient access, and visuaize more than one tree

Future features: mapping, APIs, etc

*Show off what your software looks like in action! Try to limit it to one-liners if possible and don't delve into API specifics.*

```py
>>> import mypackage
>>> mypackage.do_stuff()
'Oh yeah!'
```


## ⬇️ Installation

Simple, understandable installation instructions!

```bash
pip install my-package
```

And be sure to specify any other minimum requirements like Python versions or operating systems.

*You may be inclined to add development instructions here, don't.*


## 💭 Feedback and Contributing

Add a link to the Discussions tab in your repo and invite users to open issues for bugs/feature requests.

This is also a great place to invite others to contribute in any ways that make sense for your project. Point people to your DEVELOPMENT and/or CONTRIBUTING guides if you have them.
