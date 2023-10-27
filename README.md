# Welcome to PETSHOP DATABASE

This repository, is a basic petshop database using python.

### How to use
To use this database you need have installed [python](https://www.python.org/downloads/) and [Oracle SQL Developer](https://www.oracle.com/database/sqldeveloper/technologies/download/).

#### Database
> 01 - Open SQLDeveloper app and create a new database, following the commands:
```sql
  CREATE DATABASE petshop;

  USE petshop;

  CREATE TABLE pets(
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pet_type VARCHAR(30),
    pet_name VARCHAR(30),
    pet_age INT
  );
```

#

#### Application
> 01 - Clone this repository
```sh
  git clone https://github.com/phtoselli/FIAP-petshop-database.git
```

> 02 - Enter on repository file
```sh
  cd FIAP-PETSHOP-DATABASE
```

> 03 - Install dependencies
```sh
  pip install cx_Oracle
  pip install pandas
```

> 04 - Run project
```sh
  python3 app.py
```

#

### Author

| [<img src="https://avatars.githubusercontent.com/u/73919445?s=115&u=586aabbeb18aef0f5b6e542c2922ab30bada0a33&v=4"><br><sub>@phtoselli</sub>](https://github.com/phtoselli) |
| :---: |
