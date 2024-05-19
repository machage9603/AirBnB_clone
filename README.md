![hbnb](https://github.com/machage9603/AirBnB_clone/assets/139768288/0fea0a15-e99b-4029-aaf3-84122695c2fa)

# **Air BnB Clone structure overview**

![Structure](https://github.com/machage9603/AirBnB_clone/assets/139768288/4bbe8b1c-5258-4e35-8464-de6913bbdb1c)

# AirBnB_clone - Console that's in charge of managing the models in a common AirBnB application.

# Description of the project

The initial phase of this project entails simulating an Airbnb-like application by developing a control system for the backend modules utilized on our web platform. This is accomplished through the implementation of a JSON-based database system, employing object-oriented programming (OOP) principles, Python data serialization and deserialization techniques, and command parsing mechanisms. The outcome is a robust local database that can be dynamically modified via predefined commands, offering a versatile and efficient solution for data management.

# Prerequisites

Python3

```
sudo apt-get install python3
```

# Installation

To access the console use the following command:

```
git clone https://github.com/machage9603/AirBnB_clone.git; cd AirBnB_clone
```

# Run

Running the console use:

```
python3 console.py
```

or

```
./console.py
```

# Testing

To execute unit tests to confirm that your changes haven't modify the functionality use:

```
python3 -m unittest discover tests
```

## How to start it

### Interactive Mode

```
$ ./console.py
```

Now you are on interactive mode and you will see the prompt `(hbnb)`
input a command:

```
(hbnb) create User
```

the id of the created model will be visible in the standard output, if you do:

```
(hbnb) show User [id]
```

All the attributes of the created model will be in your screen.

use:

```
(hbnb) help
```

For a list of usable commands, to exit press Ctrl+D or type the command quit.

### Non-Interactive Mode

The console can also be used in non-interactive mode:

```
$ echo "create User" | ./console.py

$ echo "help" | ./console.py
```

The program will create a file called: `file.json` whenever you create a new model, it'll be store in the top folder.

## Examples

Executing help command.

![Help](https://github.com/daorejuela1/AirBnB_clone/blob/master/images/help.gif)

Getting help for a command

![Help update](https://github.com/daorejuela1/AirBnB_clone/blob/master/images/help%20update.gif)

Creating a new user, showing the ID and updating the fields

![Create & Update](https://github.com/daorejuela1/AirBnB_clone/blob/master/images/create%20user%20and%20update.gif)

Creating a new basemodel, counting basemodel, delete and count again

![Destroy](https://github.com/daorejuela1/AirBnB_clone/blob/master/images/destroy.gif)

## Author

- [Mike Machage](https://twitter.com/machage_)

## Acknowledgements

This project was majorly successful because of my technical mentors and my learning peers who are too many to mention.

Disclaimer: the work included in this project was completed as part of the curriculum for the ALX Africa Software Engineering program, which is based on the projects and materials provided by Holberton School.

## Credits

- [ALX](https://www.alxafrica.com/)
- [Holberton School](https://www.holbertonschool.com/)

## Contact

- mikemachage@gmail.com
