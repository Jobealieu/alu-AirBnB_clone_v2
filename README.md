# AirBnB Clone - Version 2

## Project Overview

This project is the second iteration of an AirBnB clone, representing a significant evolution from the initial version. It implements a full-stack backend system that manages property rental data through both file-based and database storage engines. The project focuses on building a robust data persistence layer with support for MySQL databases while maintaining backward compatibility with JSON file storage.

## Description

The AirBnB Clone v2 builds upon the foundation of the first version by introducing database storage capabilities alongside the existing file storage system. This version implements a command-line interface (console) for managing application objects, with the flexibility to switch between two distinct storage engines: FileStorage and DBStorage. The system handles various entities including users, states, cities, places, amenities, and reviews, making it possible to simulate the core functionality of a property rental platform.

## Key Features

- Dual storage engine architecture supporting both JSON file storage and MySQL database storage
- Object-Relational Mapping (ORM) using SQLAlchemy for database interactions
- Command-line interface for CRUD operations on all data models
- Persistent data storage across sessions
- Environment-based configuration for flexible deployment
- Comprehensive test suite ensuring code reliability
- Support for complex relationships between data models

## Architecture

### Storage Engines

The application supports two distinct storage modes:

**FileStorage Mode (Default)**

In this mode, the system serializes and deserializes Python objects to and from a JSON file. Every time the application initializes, it creates a FileStorage instance that loads existing data from `file.json`. All changes to objects are immediately persisted to this file.

**DBStorage Mode**

When configured for database storage, the application connects to a MySQL database using SQLAlchemy. This mode enables more robust data persistence with support for complex queries, transactions, and relational data integrity. The database connection parameters are provided through environment variables.

### Data Models

The system implements the following core models:

- **BaseModel**: The parent class providing common attributes and methods for all models
- **User**: Represents platform users with authentication details
- **State**: Geographical state entities
- **City**: City entities linked to states
- **Amenity**: Features and amenities available at properties
- **Place**: Property listings with detailed information
- **Review**: User reviews for properties

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/Jobealieu/alu-AirBnB_clone_v2.git
cd alu-AirBnB_clone_v2
```

### Prerequisites

- Python 3.4 or higher
- MySQL 5.7 or higher (for DBStorage mode)
- SQLAlchemy (install via pip)
- MySQLdb module (install via pip)

### Setting Up MySQL

For database storage mode, you need to set up MySQL databases. The repository includes setup scripts:

**Development Database:**
```bash
cat setup_mysql_dev.sql | mysql -uroot -p
```

**Test Database:**
```bash
cat setup_mysql_test.sql | mysql -uroot -p
```

These scripts create the necessary databases (`hbnb_dev_db` and `hbnb_test_db`) along with the required users and permissions.

## Usage

### Starting the Console

Run the console in FileStorage mode (default):

```bash
./console.py
```

Run the console in DBStorage mode:

```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

Once the console starts, you will see the prompt:

```
(hbnb)
```

### Environment Variables

The application behavior can be controlled through the following environment variables:

- `HBNB_ENV`: Running environment (`dev` or `test`)
- `HBNB_MYSQL_USER`: MySQL username
- `HBNB_MYSQL_PWD`: MySQL password
- `HBNB_MYSQL_HOST`: MySQL server hostname
- `HBNB_MYSQL_DB`: MySQL database name
- `HBNB_TYPE_STORAGE`: Storage type (`file` or `db`)

### Console Commands

The console supports the following commands:

**create**

Creates a new instance of a specified class and saves it. When using DBStorage, you can also provide attribute values:

```bash
(hbnb) create State name="California"
(hbnb) create City state_id="123" name="San_Francisco"
```

Note: Underscores in string values are replaced with spaces.

**show**

Displays the string representation of an instance based on class name and ID:

```bash
(hbnb) show User 1234-1234-1234
```

**destroy**

Deletes an instance based on class name and ID:

```bash
(hbnb) destroy Place 5678-5678-5678
```

**all**

Prints string representations of all instances, optionally filtered by class name:

```bash
(hbnb) all
(hbnb) all State
```

**update**

Updates an instance by adding or modifying an attribute:

```bash
(hbnb) update User 1234-1234-1234 email "user@example.com"
```

**quit or EOF**

Exits the console:

```bash
(hbnb) quit
```

**help**

Displays help information for commands:

```bash
(hbnb) help
(hbnb) help create
```

### Usage Examples

Here are some practical examples of using the console:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) create User
f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a
(hbnb) show User f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a
[User] (f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a) {'id': 'f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a', 'created_at': datetime.datetime(2024, 2, 8, 10, 30, 45), 'updated_at': datetime.datetime(2024, 2, 8, 10, 30, 45)}
(hbnb) all User
["[User] (f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a) {'id': 'f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a', 'created_at': datetime.datetime(2024, 2, 8, 10, 30, 45), 'updated_at': datetime.datetime(2024, 2, 8, 10, 30, 45)}"]
(hbnb) update User f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a first_name "John"
(hbnb) show User f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a
[User] (f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a) {'id': 'f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a', 'created_at': datetime.datetime(2024, 2, 8, 10, 30, 45), 'updated_at': datetime.datetime(2024, 2, 8, 10, 32, 12), 'first_name': 'John'}
(hbnb) destroy User f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a
(hbnb) show User f9d6a1e2-3c4b-5d6e-7f8a-9b0c1d2e3f4a
** no instance found **
(hbnb) quit
```

## Testing

The project includes a comprehensive test suite located in the `tests` directory. Tests cover both FileStorage and DBStorage implementations, ensuring that the application functions correctly regardless of the storage backend.

Run tests using:

```bash
python3 -m unittest discover tests
```

For testing with the database storage:

```bash
HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests
```

## Project Structure

```
alu-AirBnB_clone_v2/
├── console.py                 # Command-line interface entry point
├── models/                    # Data models directory
│   ├── __init__.py           # Package initializer and storage instantiation
│   ├── base_model.py         # BaseModel class definition
│   ├── user.py               # User model
│   ├── state.py              # State model
│   ├── city.py               # City model
│   ├── amenity.py            # Amenity model
│   ├── place.py              # Place model
│   ├── review.py             # Review model
│   └── engine/               # Storage engines
│       ├── file_storage.py   # JSON file storage implementation
│       └── db_storage.py     # MySQL database storage implementation
├── tests/                     # Unit tests
├── setup_mysql_dev.sql       # Development database setup script
├── setup_mysql_test.sql      # Test database setup script
├── AUTHORS                    # List of contributors
└── README.md                  # This file
```

## Technical Details

### FileStorage Implementation

The FileStorage engine uses Python's JSON module to serialize objects to a file. Each object is converted to a dictionary representation before being written to `file.json`. On subsequent runs, the file is read and objects are reconstructed from their dictionary representations.

### DBStorage Implementation

The DBStorage engine leverages SQLAlchemy's ORM capabilities to map Python objects to database tables. Each model class includes SQLAlchemy column definitions and relationship mappings. The engine handles session management, ensuring that changes are properly committed to the database and transactions are handled correctly.

### Object Relationships

The data models implement various relationships:

- A State can have multiple Cities
- A City belongs to one State
- A Place can have multiple Reviews and Amenities
- A User can have multiple Places and Reviews

These relationships are maintained through foreign keys in DBStorage mode and through attribute references in FileStorage mode.

## Development Notes

This project represents an academic exercise in building a full-stack application with multiple data persistence strategies. It demonstrates important software engineering concepts including:

- Abstraction through storage engine interfaces
- Object-oriented design principles
- Database design and ORM usage
- Environment-based configuration
- Test-driven development

The dual storage approach allows for easy comparison between file-based and database-based persistence, making it an excellent learning tool for understanding different data storage paradigms.

## Authors

Alieu Jobe
