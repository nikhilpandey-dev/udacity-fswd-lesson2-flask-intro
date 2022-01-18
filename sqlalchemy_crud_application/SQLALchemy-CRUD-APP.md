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