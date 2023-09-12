# HNGX - Person API

## Overview

A simple API with basic CRUD (Create, Read, Update, Delete) operations for managing a 'person' resource.

## Table of Contents

- [HNGX - Person API](#hngx---person-api)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
  - [Setup](#setup)
  - [Usage](#usage)
    - [Endpoints](#endpoints)
    - [Example Usage](#example-usage)
    - [Fetch All Persons](#fetch-all-persons)
    - [Fetch a Specific Person](#fetch-a-specific-person)
    - [Creating a new Person](#creating-a-new-person)
    - [Updating a Person's Data](#updating-a-persons-data)
    - [Delete a Person](#delete-a-person)
  - [Source Code](#source-code)

## Features

- Create a new person record using a name.
- Retrieve a list of all persons or a specific person.
- Update the details of an existing person.
- Delete a person entry from the database.

## Getting Started

Ensure you have [Python](https://www.python.org/) version 3.9.2 or above  installed.

## Setup

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

6. Start the server:

   ```bash
   ALLOWED_HOSTS="*" SECRET_KEY="your-secret-key" DEBUG=1 gunicorn stage_1.wsgi:application
   ```

## Usage

### Endpoints

- **GET /api** Retrieve a list of all persons.
- **GET /api/name** Retrieve details of a specific person by name.
- **POST /api** Create a new person record.
- **PUT/PATCH /api/id** Update the details of a specific person.
- **DELETE /api/id** Delete a person record.

### Example Usage

### Fetch All Persons

To retrieve a list of all persons, make a GET request to the following endpoint:

```bash
GET /api
```

### Fetch a Specific Person

To retrieve details of a specific person by their name, make a GET request to the following endpoint, replacing `:name` with the person's name:

```bash
GET /api/:name
```

### Creating a new Person

To create a new person record, make a POST request to the following endpoint:

```bash
POST /api
```

Set the `Content-Type` header to `application/json`, and include the person's information (name only) in the request body in JSON format, like this:

```json
{ "name": "John Jameson" }
```

### Updating a Person's Data

To update an existing person data record, make a PATCH/PUT request to the following endpoint:

```bash
PUT /api/id
```

Include the new person's name in the request body in JSON format, like the one below and also set the `Content-Type` header to `application/json`.

```json
{ "name": "Monkey D Luffey" }
```

### Delete a Person

To delete a person, make a DELETE request to the following endpoint:

```bash
DELETE /api/id
```

## Source Code

[Github Repo](https://github.com/mashm3ll0w/hngx_stage_1)
