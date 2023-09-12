# Person API Documentation

Documentation for the Person API with expected request and response examples.

## Table of Contents

- [Person API Documentation](#person-api-documentation)
  - [Table of Contents](#table-of-contents)
  - [Person Endpoints](#person-endpoints)
    - [Get All Persons](#get-all-persons)
    - [Create Person](#create-person)
    - [Get a Person By Name](#get-a-person-by-name)
    - [Update a Person's data](#update-a-persons-data)
    - [Delete a Person entry](#delete-a-person-entry)
  - [Setup On Local Server](#setup-on-local-server)
  - [Testing](#testing)

---

## Person Endpoints

### Get All Persons

Retrieve a list of all persons.

- **URL**: `/api`
- **Method**: `GET`
- **Request**: None
- **Response**:

  ```json
  {
    "persons": [
        {
            "id": 1,
            "name": "Charles Swaleh"
        },
        {
            "id": 2,
            "name": "Pauline Muigai"
        },
        {
            "id": 3,
            "name": "Janet Jackson"
        },
        {
            "id": 4,
            "name": "Jessica Alba"
        },
        {
            "id": 5,
            "name": "Judas Iscariot"
        }
    ]
  }
  ```

### Create Person

Create a new person entry.

- **URL**: `/api`
- **Method**: `POST`
- **Request**:

  ```json
  {
    "name": "Samantha Nawal"
  }
  ```

- **Response** (HTTP Status Code 201: Created)
```json
  {
    "id": 6,
    "name": "Samantha Nawal"
  }
```

### Get a Person By Name

Retrieve details of a person by name.

- **URL**: `/api/charles swaleh`
- **Method**: `GET`
- **Request**: None
- **Response**:

  ```json
  {
    "id": 1,
    "name": "Charles Swaleh"
  }
  ```

### Update a Person's data

Update the details of a specific person.

- **URL**: `/api/id` Where `:id` is the person's from the DB.
- **Method**: `PUT` or `PATCH`
- **Request**:

  ```json
  {
    "name": "Carol Radull"
  }
  ```
- **Response**:

  ```json
  {
    "id": 6,
    "name": "Carol Radull"
  }
  ```

### Delete a Person entry

Delete a person entry.

- **URL**: `/api/id`
- **Method**: `DELETE`
- **Request**: None
- **Response** (Success - HTTP Status Code 204 No Content):

## Setup On Local Server

1. Create a virtual environment:

   ```bash
   pip -m venv env
   ```

2. Start the virtual environment:

   ```bash
   source ./env/bin/activate
   ```

3. Clone this repository inside the folder with the virtual environment:

   ```bash
   git clone https://github.com/mashm3ll0w/hngx_stage_1
   ```

4. Change to the project directory:

   ```bash
   cd hngx_stage_1
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Create an `.env` file to hold your secrets (**Please change the SECRET_KEY**):

   ```bash
   echo "SECRET_KEY="0197320918cn09831c908n9023u4hc918-7918-4t791-4398v659"\nDEBUG=True\nALLOWED_HOSTS=['*']" > .env
   ```

7. Start the server:

   ```bash
   gunicorn stage_1.wsgi:application
   ```

## Testing

Testing is done using Django's native test toolkit. Run the tests using the command:

```bash
python manage.py test
```
