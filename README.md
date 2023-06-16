# user-management-api

## Description

This is a simple user management API that allows you to create, read, update and delete users.

## DATABSE

The database used is TinyDB, a lightweight document oriented database.

### Collections | Tables

- users

#### User - Document | Row

doc_id: chat_id

```json
{
  "first_name": "string",
  "last_name": "string",
  "username": "string",
}
```

## API

### Endpoints

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | /users   | Get all users |
| GET    | /users/{chat_id} | Get user by chat_id |
| POST   | /users   | Create a new user |
| PUT    | /users/{chat_id} | Update user by chat_id |
| DELETE | /users/{chat_id} | Delete user by chat_id |
