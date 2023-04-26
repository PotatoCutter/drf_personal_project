| **fuc**     | **Method** | **URL**                    | **req**                                                              | **res**  | **host**       | **desc** |
|-------------|------------|----------------------------|----------------------------------------------------------------------|----------|----------------|----------|
| signup      | POST       | users/signup/              | email, password, name, gender, age                                   | save     | localhost:8000 |          |
| login       | POST       | users/login/               | email, password                                                      | validate | localhost:8000 |          |
| logout      | POST       | users/logout/              | logout                                                               | logout   | localhost:8000 |          |
| user_update | PUT        | users/update/<int:user_id> | email, password, name, gender, age                                   | save     | localhost:8000 |          |
| user_delete | DELETE     | users/del/<int:user_id>    | user_id                                                              | delete   | localhost:8000 |          |
| todo_create | POST       | list/                      | id, title, is_complete, create_at, update_at, completion_at, user_id | save     | localhost:8000 |          |
| todo_view   | GET        | list/                      | id, title, is_complete, create_at, update_at, completion_at, user_id | data     | localhost:8000 |          |
| todo_update | PUT        | list/<int:todo_id>         | id, title, is_complete, create_at, update_at, completion_at, user_id | save     | localhost:8000 |          |
| todo_delete | DELETE     | list/<int:todo_id>         | id, title, is_complete, create_at, update_at, completion_at, user_id | delete   | localhost:8000 |          |