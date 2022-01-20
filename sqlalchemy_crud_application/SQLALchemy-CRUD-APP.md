- [Lesson 5: Building a  CRUD Application with SQLAlchemy](#lesson-5-building-a--crud-application-with-sqlalchemy)
  - [Model View Controller](#model-view-controller)
    - [layers](#layers)
    - [MVC In Nutshell](#mvc-in-nutshell)
    - [MVC Diagram](#mvc-diagram)
  - [Handling User input](#handling-user-input)
  - [Getting User Data in Flask - part 1](#getting-user-data-in-flask---part-1)
    - [URL query parameter](#url-query-parameter)
    - [Form data](#form-data)
    - [Note defaults](#note-defaults)
    - [JSON](#json)
    - [Getting HTML form submission to get the data](#getting-html-form-submission-to-get-the-data)
    - [Form methods `POST` vs `GET`](#form-methods-post-vs-get)
      - [The POST submission](#the-post-submission)
      - [The GET submission](#the-get-submission)
  - [Getting User Data in Flask -Part 2](#getting-user-data-in-flask--part-2)
  - [Using AJAX to send data to flask](#using-ajax-to-send-data-to-flask)
- [Lesson 6: Migrations](#lesson-6-migrations)
  - [Introduction (Migrations Part 1)](#introduction-migrations-part-1)
    - [Upgrades and rollback](#upgrades-and-rollback)
  - [Migrations - Part 2](#migrations---part-2)
    - [Migrations command line scripts](#migrations-command-line-scripts)
    - [Steps to get migrations going](#steps-to-get-migrations-going)
***
# Lesson 5: Building a  CRUD Application with SQLAlchemy
![CRUD to Database Mapping](./images/crud_db_sqlalchemy_mapping.png)
<center>CRUD to Database to SQLAchemy Mapping</center>

## Model View Controller
- MVC stands for Model-View-Controller, a common pattern for architecting web applications.
- Describe the 3 layers of the application we are developing.

### layers
|Layer| Description|
|:---:|:----------:|
|**Models**|manage data and business logic for us. What happens inside models and database, capturing logical relationships and properties across the web app objects.|
|**Views**|handles display and representation logic. What the user sees (HTML, CSS, JS from the user's perspective)|
|Controllers|routes commands to the models and views, containing control logic. Control how commands are sent to models and views, and how models and views wound up interacting with each other.|

### MVC In Nutshell
- The Model Layer: Manages data and business logic. Database query falls under the models part of MVC.
- The Views Layer: Handles display and representation logic
- The Controllers Layer: Routes commands to models and views

### MVC Diagram
![Model-View-Controller Diagram](./images/mvc_diagram.png)
<center>Model-View-Controller Diagram</center>

## Handling User input
![MVC and User Input](./images/mvc-handling-user-input.png)
<center>MVC and User Input</center>

![MVC and Flask Todo Web App](./images/user_input_mvc_flask.png)
<center>MVC and Flask Todo Web App</center>

## Getting User Data in Flask - part 1

There are three methods of getting user data  from a view to a controller.
1. URL Query parameters
2. Forms
3. JSON

![Three methods of getting user data in Flask](./images/3-methods-of-getting-user-data-flask.png)
<center>Three methods of getting user data in Flask</center>

### URL query parameter
- URL query parameters are listed as key-value pairs at the end of a URL, preceding a "?" question mark. E.g. `www.example.com/hello?my_key=my_value`

### Form data
- `request.form.get('<name>')` reads the `value` from a form input control (text input, number input, password input, etc) by the `name` attribute on the input HTML element.

### Note defaults
- `request.args.get`, `request.form.get` both accept an optional second parameter, e.g., `request.args.get('foo', 'my default')`, set to a default value, in case the result is empty.

### JSON
- `request.data` retrieves JSON as a string. Then we'd take that string and turn in into python constructs by calling `json.loads` on the `request.data` string to turn in into lists and dictionaries in Python.

### Getting HTML form submission to get the data
- forms take an `action`(name of the route) and `method`(route method) to submit data to our server.
- The `name` attribute on a form control element is the key used to retrieve data from `request.get(<key>)`.
- All forms either define a submit button, or allow the user to hit ENTER on an input to submit the form.

### Form methods `POST` vs `GET`
- The way form data traverses from the client to server differs based on whether we are using a GET or a POST method on the form.

#### The POST submission
- On submit, we send off an HTTP POST request to the route `/create` with a **request body**
- The request body stringifies the key-value pairs of fields from the form (as part of the `name` attribute) along with their values.

#### The GET submission
- Sends off a GET request with **URL query parameters** that appends the form data to the URL.
- Ideal for smaller form submission

> POSTs are ideal for longer form submissions, since URL query parameters can only be so long compared to request bodies (max 2048 characters). Moreover, forms can only send POST and GET requests, and nothing else.

## Getting User Data in Flask -Part 2

## Using AJAX to send data to flask
- Data requests are either synchronous or async (asynchronous)
- Async data requests are requests that get sent to the server and back to the client without a page refresh.
- Async requests (AJAX requests) use one of two methods:
  1. XMLHttpRequest
  2. Fetch (modern way)
***

# Lesson 6: Migrations

## Introduction (Migrations Part 1)
- Migrations deal with how we manage modifications to our data schema, over time.
- Mistakes to our database schema are very expensive to make. The entire app can go down, so we want to
  - quickly roll back changes, and 
  - test changes before we make them
- A migration is a file that keeps track of changes to our database schema(structure of our database)
  - Offers version controls our schema

### Upgrades and rollback
- Migrations stack together in order to form the latest version of our database schema
- We can upgrade our database schema by applying migrations
- We can roll back our database schema to a former version by reverting migrations that we applied.

> Doing a `git commit` for a Git version control system on files is similar to `applying a migration (a schema upgrade)` for a version control system (using migrations) on our data schema.

## Migrations - Part 2

Migrations
- encapsulate a set of changes to our database schema, made over time.
- are uniquely named
- are uniquely stored as *local files* in our project repo, e.g., a `migrations/` folder
- There should be a 1 - 1 mapping between the changes made to our database, and the *migration files* that exist in our migrations/folder.
- Our migrations file set up the tables for our database.
- All changes made to our db should exist physically as part of migration file in our repository.

### Migrations command line scripts

There are generally 3 scripts needed, for
- **migrate**: creating a migration script template to fill out; generating a migrations file based on changes to be made
- **upgrade**: applying migrations that hadb't been applied yet ("upgrading" our database)
- **downgrade**: rolling back applied migrations that were problematic ("downgrading" our database)

### Steps to get migrations going
1. Initiliaze the migration repository structure for storing migrations
2. Create a migration script (using Flask-Migrate)
3. (Manually) Run the migration script (using Flask-Script)



