# Concept: 0x00. AirBnB clone - The console

[Airbnb](airbnb.com) is an online marketplace and hospitality service platform that allows people to rent out their properties or spare rooms to travellers.The idea behind Airbnb is to provide an alternative accommodation option for travellers, allowing them to stay in unique places and experience local culture. Hosts can list their properties on the platform, including apartments, houses, villas, or even individual rooms within their own homes.

Travellers can search for available accommodations based on their destination, dates of travel, and specific preferences. They can view detailed listings with descriptions, photos, amenities, and reviews from previous guests. The booking process is done through the Airbnb platform, which provides a secure payment system and messaging system for communication between hosts and guests.

## Project Description

In this part of the project, we create the console. This is a command-line interface that allows us to make actions such as creating a user, place or city, updating the attributes of a place, deleting, Do operations on objects (count, compute stats, etc…) and Retrieve an object from a file, a database etc…, etc. The cli enables us mirror the actions in the Airbnb website, without necessarily having a front-end interface.

We first create a BaseModel class that creates most of the functionality. Most of the other classes reperesenting the Airbnb inherit from this BaseModel.

### The command interpreter

The command interpreter takes commands from a user either interactively (a command at a time from a user), or non-interactively (from a script, redirects, etc), and processes those commands giving output.

### Usage

How to start the interpreter:
First we clone this repo:

    $ git clone https://github.com/aliceada96/AirBnB_clone.git
    $

Then we cd into AirBnb directory:

    $ cd AirBnB
    $

We can start the command interpreter interactively:

    $ ./console.py
    (hbnb)

To exit the console we can use the command `quit` or `ctrl + D`

    (hbnb) quit
    $

To get the available list of commands we can enter 'help' onto the cli.

    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb) 

We can get more information on a command e.g.,

    (hbnb) help count
    Print number of objects from class.
    (hbnb)

We can create an instance of a class, for example:

    (hbnb) create BaseModel
    78914fe9-c46d-4c9a-bfb9-fc1d32e3b765
    (hbnb)

Inspect an instance of a class:

    (hbnb) show BaseModel 78914fe9-c46d-4c9a-bfb9-fc1d32e3b765
    {'id': '78914fe9-c46d-4c9a-bfb9-fc1d32e3b765', 'created_at': '2023-08-14T20:44:13.700108', 'updated_at': '2023-08-14T20:44:13.700108', '__class__': 'BaseModel'}
    (hbnb)

Update an instance of a class with various attributes:

    (hbnb) update BaseModel 78914fe9-c46d-4c9a-bfb9-fc1d32e3b765 name Nairobi
    (hbnb) show BaseModel 78914fe9-c46d-4c9a-bfb9-fc1d32e3b765
    {'id': '78914fe9-c46d-4c9a-bfb9-fc1d32e3b765', 'created_at': '2023-08-14T20:44:13.700108', 'updated_at': '2023-08-14T20:44:13.700108', '__class__': 'BaseModel', 'name': 'Nairobi'}
    (hbnb)

Delete an instance of a class:

    (hbnb) destroy BaseModel 78914fe9-c46d-4c9a-bfb9-fc1d32e3b765
    (hbnb) show BaseModel 78914fe9-c46d-4c9a-bfb9-fc1d32e3b765
    ** no instance found **
    (hbnb)

## The project is structured as follows

**Module: console.py**
This module implements a simple command interpreter for the AirBnB program. It provides a command-line interface for interacting with the program's objects and data.

**Class: HBNBCommand**
This class extends the cmd.Cmd module to create a command-line interface for interacting with the AirBnB objects. It provides various commands for creating, showing, updating, and deleting objects. The command prompt is (hbnb).

**Methods:**

`do_quit(self, arg):` Quit command to exit the program.
`do_EOF(self, arg):` Quit command to exit the program.
`emptyline(self):` Overrides the default behavior of the empty line.
`do_create(self, arg):` Creates an object based on the specified class.
`do_show(self, args):` Displays the string representation of an instance.
`do_destroy(self, args):` Deletes an instance based on class name and id.
`do_all(self, args):` Displays string representations of all instances.
`do_count(self, args):` Prints the number of objects from a specific class.
`do_update(self, args):` Updates the attributes of an instance.
`default(self, line: str):` Called when the command prefix is not recognized.

**Module: models/init.py**
This module initializes the FileStorage instance called storage which handles serialization and deserialization of objects.

**Module: models/amenity.py**
This module defines the Amenity class which inherits from BaseModel. It represents an amenity for an accommodation.

**Module: models/base_model.py**
This module defines the BaseModel class, which serves as the base class for all other models. It provides methods for creating, saving, updating, and representing model instances.

**Module: models/city.py**
This module defines the City class, which inherits from BaseModel. It represents a city associated with a state.

**Module: models/engine/init.py**
This module is empty and serves as an initialization for the engine package.

**Module: models/engine/file_storage.py**
This module defines the FileStorage class, which handles the serialization and deserialization of objects to/from a JSON file.

**Module: models/place.py**
This module defines the Place class, which inherits from BaseModel. It represents an accommodation or place for rent.

**Module: models/review.py**
This module defines the Review class, which inherits from BaseModel. It represents a review for a specific accommodation.

**Module: models/state.py**
This module defines the State class, which inherits from BaseModel. It represents a state or region.

**Module: models/user.py**
This module defines the User class, which inherits from BaseModel. It represents a user of the AirBnB program.

**Module: tests/init.py**
An empty module, likely intended for tests.

**Module: tests/test_console.py**
A test module for testing the functionality of the HBNBCommand class in the console.py module.

**Module: tests/test_models/init.py**
An empty module, likely intended for tests related to models.

**Module: tests/test_models/test_amenity.py**
A test module for testing the functionality of the Amenity class.

**Module: tests/test_models/test_base_model.py**
A test module for testing the functionality of the BaseModel class.

**Module: tests/test_models/test_city.py**
A test module for testing the functionality of the City class.

**Module: tests/test_models/test_engine/init.py**
An empty module, likely intended for tests related to the engine package.

**Module: tests/test_models/test_engine/test_file_storage.py**
A test module for testing the functionality of the FileStorage class.

**Module: tests/test_models/test_place.py**
A test module for testing the functionality of the Place class.

**Module: tests/test_models/test_review.py**
A test module for testing the functionality of the Review class.

**Module: tests/test_models/test_state.py**
A test module for testing the functionality of the State class.

**Module: tests/test_models/test_user.py**
A test module for testing the functionality of the User class.

AUTHORS:
[Alice Ada](www.github.com/aliceada96),
[Gabriel Wachira](www.github.com/Wachira-G)
