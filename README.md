# AirBnB Clone v2

A full-stack web application that replicates the core functionality of AirBnB. This version builds upon the initial console-based storage system by introducing MySQL database integration, Fabric deployment automation, and web framework implementation using Flask and Jinja2.

## Project Description

This project is the second iteration of an AirBnB clone, implementing a complete backend infrastructure with dual storage engines (file-based and database), a command-line interface for data management, and deployment automation tools. The system uses object-relational mapping (ORM) with SQLAlchemy to handle database operations and provides both development and testing environments.

## Features

- Command-line interpreter (console) for object management
- Dual storage engine support (FileStorage and DBStorage)
- MySQL database integration with SQLAlchemy ORM
- Object-relational mapping for all model classes
- Environment-based configuration system
- Fabric scripts for automated deployment
- Unit testing framework with comprehensive test coverage
- PEP8 compliant codebase
- RESTful architecture foundation

## Architecture

### Storage Engines

The application supports two storage backends that can be switched using environment variables:

#### FileStorage (Default)
- Serializes objects to JSON format
- Stores data in `file.json`
- Suitable for development and testing
- Persistent across sessions

#### DBStorage
- Uses MySQL database for data persistence
- Implements SQLAlchemy ORM
- Supports relational data modeling
- Production-ready storage solution

### Models

The application implements the following data models:

- **BaseModel**: Parent class providing common attributes and methods
  - `id`: Unique identifier (UUID)
  - `created_at`: Timestamp of creation
  - `updated_at`: Timestamp of last modification

- **User**: User account information
  - `email`: User email address
  - `password`: User password
  - `first_name`: User first name
  - `last_name`: User last name

- **State**: Geographic state/region
  - `name`: State name

- **City**: City within a state
  - `state_id`: Reference to State
  - `name`: City name

- **Amenity**: Property amenities
  - `name`: Amenity name

- **Place**: Property listings
  - `city_id`: Reference to City
  - `user_id`: Reference to User (owner)
  - `name`: Place name
  - `description`: Place description
  - `number_rooms`: Number of rooms
  - `number_bathrooms`: Number of bathrooms
  - `max_guest`: Maximum guest capacity
  - `price_by_night`: Nightly rate
  - `latitude`: Geographic latitude
  - `longitude`: Geographic longitude

- **Review**: User reviews
  - `place_id`: Reference to Place
  - `user_id`: Reference to User
  - `text`: Review content

## Installation

### Prerequisites

- Python 3.8.5 or higher
- MySQL 8.0 or higher
- pip (Python package manager)

### Clone Repository

```bash
git clone https://github.com/Jobealieu/alu-AirBnB_clone_v2.git
cd alu-AirBnB_clone_v2
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Database Setup

#### Development Database

```bash
cat setup_mysql_dev.sql | mysql -uroot -p
```

#### Test Database

```bash
cat setup_mysql_test.sql | mysql -uroot -p
```

## Configuration

The application uses environment variables for configuration:

| Variable | Description | Values |
|----------|-------------|---------|
| `HBNB_ENV` | Running environment | `dev`, `test`, `production` |
| `HBNB_MYSQL_USER` | MySQL username | Database user |
| `HBNB_MYSQL_PWD` | MySQL password | Database password |
| `HBNB_MYSQL_HOST` | MySQL hostname | `localhost`, IP address |
| `HBNB_MYSQL_DB` | Database name | `hbnb_dev_db`, `hbnb_test_db` |
| `HBNB_TYPE_STORAGE` | Storage engine type | `file`, `db` |

### Usage Examples

#### FileStorage Mode (Default)

```bash
./console.py
```

#### DBStorage Mode

```bash
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

## Console Usage

The console is a command-line interface for managing application objects.

### Starting the Console

#### Interactive Mode

```bash
$ ./console.py
(hbnb)
```

#### Non-Interactive Mode

```bash
$ echo "help" | ./console.py
```

### Available Commands

#### create
Creates a new instance of a class and saves it.

**Syntax:**
```
create <ClassName>
create <ClassName> <param1>=<value1> <param2>=<value2> ...
```

**Examples:**
```bash
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8

(hbnb) create State name="California"
95a5abab-aa65-4861-9bc6-1da4a36069aa

(hbnb) create Place city_id="0001" user_id="0001" name="My_house" number_rooms=4 price_by_night=300
```

**Note:** Underscores in string values are replaced with spaces.

#### show
Displays the string representation of an instance.

**Syntax:**
```
show <ClassName> <id>
<ClassName>.show(<id>)
```

**Examples:**
```bash
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2024, 2, 18, 14, 21, 12, 96959), 'updated_at': datetime.datetime(2024, 2, 18, 14, 21, 12, 96971)}

(hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
```

#### destroy
Deletes an instance based on class name and ID.

**Syntax:**
```
destroy <ClassName> <id>
<ClassName>.destroy(<id>)
```

**Examples:**
```bash
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8

(hbnb) User.destroy("38f22813-2753-4d42-b37c-57a17f1e4f88")
```

#### all
Displays string representations of all instances or all instances of a specific class.

**Syntax:**
```
all
all <ClassName>
<ClassName>.all()
```

**Examples:**
```bash
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2024, 2, 18, 14, 47, 29, 134640), 'updated_at': datetime.datetime(2024, 2, 18, 14, 47, 29, 134660)}"]

(hbnb) User.all()

(hbnb) all
```

#### update
Updates an instance by adding or modifying attributes.

**Syntax:**
```
update <ClassName> <id> <attribute_name> "<attribute_value>"
<ClassName>.update(<id>, <attribute_name>, <attribute_value>)
<ClassName>.update(<id>, <dictionary>)
```

**Examples:**
```bash
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "Betty"

(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")

(hbnb) User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
```

**Protected Attributes:** `id`, `created_at`, `updated_at`, `__class__` cannot be modified.

#### count
Retrieves the number of instances of a class.

**Syntax:**
```
<ClassName>.count()
```

**Examples:**
```bash
(hbnb) User.count()
2
```

#### help
Displays help information for commands.

**Syntax:**
```
help
help <command>
```

**Examples:**
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create
```

#### quit / EOF
Exits the console.

**Examples:**
```bash
(hbnb) quit
```

## Testing

The project includes comprehensive unit tests for all modules and classes.

### Running Tests

#### All Tests

```bash
python3 -m unittest discover tests
```

#### Specific Test Module

```bash
python3 -m unittest tests/test_models/test_base_model.py
```

#### With DBStorage

```bash
HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests
```

### Test Coverage

Tests are organized to mirror the project structure:

```
tests/
├── test_models/
│   ├── test_base_model.py
│   ├── test_user.py
│   ├── test_state.py
│   ├── test_city.py
│   ├── test_amenity.py
│   ├── test_place.py
│   ├── test_review.py
│   └── test_engine/
│       ├── test_file_storage.py
│       └── test_db_storage.py
└── test_console.py
```

## Code Style

The project follows PEP8 style guidelines (version 1.7.x).

### Checking Code Style

```bash
pycodestyle models/ tests/ console.py
```

## Project Structure

```
alu-AirBnB_clone_v2/
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── engine/
│       ├── __init__.py
│       ├── file_storage.py
│       └── db_storage.py
├── tests/
│   └── test_models/
│       └── test_engine/
├── console.py
├── setup_mysql_dev.sql
├── setup_mysql_test.sql
├── AUTHORS
└── README.md
```

## File Descriptions

### Core Files

- **console.py**: Command-line interpreter entry point
- **models/base_model.py**: BaseModel class with common attributes and methods
- **models/engine/file_storage.py**: JSON file-based storage engine
- **models/engine/db_storage.py**: MySQL database storage engine
- **setup_mysql_dev.sql**: Development database initialization script
- **setup_mysql_test.sql**: Test database initialization script

### Model Files

- **models/user.py**: User model class
- **models/state.py**: State model class
- **models/city.py**: City model class
- **models/amenity.py**: Amenity model class
- **models/place.py**: Place model class
- **models/review.py**: Review model class

## Database Schema

### States Table
- `id` (VARCHAR(60), PRIMARY KEY)
- `created_at` (DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP)
- `updated_at` (DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP)
- `name` (VARCHAR(128), NOT NULL)

### Cities Table
- `id` (VARCHAR(60), PRIMARY KEY)
- `created_at` (DATETIME, NOT NULL)
- `updated_at` (DATETIME, NOT NULL)
- `name` (VARCHAR(128), NOT NULL)
- `state_id` (VARCHAR(60), FOREIGN KEY REFERENCES states.id)

### Users Table
- `id` (VARCHAR(60), PRIMARY KEY)
- `created_at` (DATETIME, NOT NULL)
- `updated_at` (DATETIME, NOT NULL)
- `email` (VARCHAR(128), NOT NULL)
- `password` (VARCHAR(128), NOT NULL)
- `first_name` (VARCHAR(128))
- `last_name` (VARCHAR(128))

### Places Table
- `id` (VARCHAR(60), PRIMARY KEY)
- `created_at` (DATETIME, NOT NULL)
- `updated_at` (DATETIME, NOT NULL)
- `city_id` (VARCHAR(60), FOREIGN KEY REFERENCES cities.id)
- `user_id` (VARCHAR(60), FOREIGN KEY REFERENCES users.id)
- `name` (VARCHAR(128), NOT NULL)
- `description` (VARCHAR(1024))
- `number_rooms` (INT, DEFAULT 0)
- `number_bathrooms` (INT, DEFAULT 0)
- `max_guest` (INT, DEFAULT 0)
- `price_by_night` (INT, DEFAULT 0)
- `latitude` (FLOAT)
- `longitude` (FLOAT)

### Amenities Table
- `id` (VARCHAR(60), PRIMARY KEY)
- `created_at` (DATETIME, NOT NULL)
- `updated_at` (DATETIME, NOT NULL)
- `name` (VARCHAR(128), NOT NULL)

### Reviews Table
- `id` (VARCHAR(60), PRIMARY KEY)
- `created_at` (DATETIME, NOT NULL)
- `updated_at` (DATETIME, NOT NULL)
- `place_id` (VARCHAR(60), FOREIGN KEY REFERENCES places.id)
- `user_id` (VARCHAR(60), FOREIGN KEY REFERENCES users.id)
- `text` (VARCHAR(1024), NOT NULL)

### Place-Amenity Junction Table
- `place_id` (VARCHAR(60), FOREIGN KEY REFERENCES places.id)
- `amenity_id` (VARCHAR(60), FOREIGN KEY REFERENCES amenities.id)
- PRIMARY KEY(place_id, amenity_id)

## Technology Stack

- **Language**: Python 3.8.5+
- **Database**: MySQL 8.0
- **ORM**: SQLAlchemy
- **Testing**: unittest
- **Style**: PEP8 (pycodestyle)
- **Deployment**: Fabric

## Development Guidelines

### Adding New Models

1. Create model class inheriting from BaseModel
2. Define table name and column mappings using SQLAlchemy
3. Implement relationships with other models
4. Add corresponding unit tests
5. Update documentation

### Environment Setup Best Practices

- Use `.env` files for environment variables (not committed to repository)
- Maintain separate databases for development and testing
- Never commit database credentials
- Use consistent naming conventions

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError` when running console
**Solution**: Ensure all dependencies are installed and PYTHONPATH is set correctly

**Issue**: Database connection errors
**Solution**: Verify environment variables are set correctly and MySQL server is running

**Issue**: Tests failing with DBStorage
**Solution**: Ensure test database exists and user has proper permissions

**Issue**: `** class doesn't exist **` error
**Solution**: Verify class name spelling and capitalization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes following PEP8 guidelines
4. Write/update tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Author

ALIEU JOBE
