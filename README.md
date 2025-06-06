# HomeCooker project
![](logo.png)

### Contents

* [Description](https://github.com/MarcoANT9/Homecooker#description)
* [Files](https://github.com/MarcoANT9/Homecooker#repository-contents)
* [How to Install](https://github.com/MarcoANT9/Homecooker#how-to-install)
* [Example Usage](https://github.com/MarcoANT9/Homecooker#example-usage)
* [Landing Page](https://github.com/MarcoANT9/Homecooker#landing-page)
* [Authors](https://github.com/MarcoANT9/Homecooker#authors)
---

### Description
Home Cooker is a website that aims to provide its customers with the experience of cooking from home,
With a selection of delicious recipes made by chefs or experts in the kitchen,
allowing users the possibility to interact.
Using the methodology, the Restful API, Flask, Python, MysqlAlchemy, and Mysql.
![](index-chef.png)

---
### Repository contents
HomeCooker - Final project files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|console.py | Command line interpreter. |
|logo.png | Logo image. |
|api/ | Contains all configuration of the RestFul API. |
|landing-page/ | Contains files for the landing page. |
|models/ | Contains the definition of all the models used in the project. |
|MySQL_setup/ | Contains configuration files for the database and the developer user. |
|web_flask /| Contains files and configuration for the website. |
|tests/ | Contains unittests for the project. |
|README.md | Readme file. |
|AUTHORS | Author's file. |

---

### How to Install
Clone the repository below:
```bash
git clone https://github.com/MarcoANT9/Homecooker.git
```
---
### Example Usage

#### Interactive Mode:
```
Console activation -> ./console in the root directory.

Console commands:
Documented commands (type help <topic>):
========================================
EOF  all,  creat,e  destroy  help,  qui,t  show,  update
```

| **Function** | **Funcionality** | **Format** | **Example** |
| -------------- | ----------------- | ----------------- | ----------------- |
|EOF | Exit the program. | EOF | EOF 
|all | Prints all string representations of all instances, based or not on the class name. | all <class_name - optional> | all user
|create | Creates a new instance of BaseModel, saves, and prints the id. | create <class_name> (arguments) | create user email=example@example.com user_type=1 password=password_example
|destroy | Deletes an instance based on the class name and id. | destroy <class_name> <element.id> | destroy user user.id
|help | Help function. | help <command - optional> | help
|quit | Exit the program. | quit | quit
|show | Prints the string representation of an instance based on the class name and id. | show <class_name> <element.id> | show user user.id
|update | Updates an instance based on the class name and id by adding or updating an attribute. | update <class_name> <element.id> attribute=value
---

#### Non-interactive Mode to create a user:
```
echo 'create User email="<user_email>" last_name="<user_last_name>" first_name="<user_first_name>" website="<user_website>" nickname="<user_nickname>" user_type=<user_type> password="<user_password>"' | HMCR_MYSQL_USER=[MySQL_USER] HMCR_MYSQL_PWD=[MySQL_USER_PASSWORD] HMCR_MYSQL_HOST=[MySQL_USER_HOST] HMCR_MYSQL_DB=[MySQL_DATABASE] HMCR_TYPE_STORAGE=[STORAGE_TYPE] ./console.py
```

|   **Varible**   |   **Description**   |
| -------------- | --------------------- |
|email | This is the user email; mandatory. |
|last_name | User last name. |
|first_name | User first name. |
|website | User website or YouTube channel. |
|user_type | User type number, chef or general user; mandatory (1 = chef | 0 = common user) |
|password | User password; mandatory |
---

#### Non-interactive Mode to create recipe:
```
echo 'create Recipe user_id="<chef_id>" name="<recipe_name>" text="<recipe_procedure>" review=<recipe_review> ingredients="<recipe_ingredients>"' | HMCR_MYSQL_USER=[MySQL_USER] HMCR_MYSQL_PWD=[MySQL_USER_PASSWORD] HMCR_MYSQL_HOST=[MySQL_USER_HOST] HMCR_MYSQL_DB=[MySQL_DATABASE] HMCR_TYPE_STORAGE=[STORAGE_TYPE] ./console.py
```
|   **Varible**   |   **Description**   |
| -------------- | --------------------- |
|user_id | User ID from the database. |
|name | Recipe name; mandatory. |
|text | Recipe procedure; mandatory. |
|review | This is a number (1-5). |
|ingredients | Recipe ingredients; mandatory. |
---

#### Non-interactive Mode to create a review:
```

echo 'create Review user_id="<user_id>" recipe_id="<recipe_id>" text="<review_text>" rating=<recipe_rating>' | HMCR_MYSQL_USER=[MySQL_USER] HMCR_MYSQL_PWD=[MySQL_USER_PASSWORD] HMCR_MYSQL_HOST=[MySQL_USER_HOST] HMCR_MYSQL_DB=[MySQL_DATABASE] HMCR_TYPE_STORAGE=[STORAGE_TYPE] ./console.py
```

|   **Varible**   |   **Description**   |
| -------------- | --------------------- |
|user_id | User ID from the database. |
|recipe_id | Recipe id from the database. |
|text | Recipe comments; mandatory. |
|rating | Recipe rating - number (1-5); mandatory. |

---
### Landing Page
Link: [About](https://marcoant9.github.io/Homecooker/landingpage/about.html)

---
### Authors
#### Marco Antonio Niño
- Github: [MarcoANT9](https://github.com/MarcoANT9)
- Twitter: [@MarcoAnt9127](https://twitter.com/MarcoAnt9127)

#### Jesús Acevedo Cano
- Github: [Jesus-Acevedo-Cano](https://github.com/Jesus-Acevedo-Cano)
- Twitter: [@JessAcevedoCan1](https://twitter.com/JessAcevedoCan1)

#### Joan Sebastian García
- Github: [SleepyCrow](https://github.com/sleepy-crow)
- Twitter: [@Garcianoahh](https://twitter.com/Garcianoahh)

#### Luz Sánchez Bolaños
- Github: [zulsb](https://github.com/zulsb)
- Twitter: [@LuzSanchezB](https://twitter.com/LuzSanchezB)

Cohort 10
Colombia - Cali - 2020
