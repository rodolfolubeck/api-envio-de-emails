# E-mail trigger service 

## Usage 

All responses will have the form

```json
{
  "data": "Mixed type holding the content of the response",
  "message": "Description of what happened"
}
```
Subsequent response definitions will only detail the exprected value of the `data field`

### List of all sent e-mails

**Definition**
`GET /sent`

**Response**
- `200 OK` on success
```json
[
  {
    "identifier": "1",
    "name": "Rodolfo Lubeck",
    "email": "rcflubeck@gmail.com",
    "sentDate": "27/05/2020"
  },
  {
    "identifier": "2",
    "name": "Rodolfo Lubeck",
    "email": "rodolfolubeck@live.com",
    "sentDate": "27/05/2020"
  }

]
```

## Send a new e-mail

**Definition**
`POST /send`

**Arguments**
 - `"identifier":int` a unique identifier of database sequence
 - `"name":string` name of the user who will receive the contact
 - `"email":string` contact e-mail of the user who will receive the contact
 - `"sendDate:date` date the email was sent
 
 **Response** 
 - `201 Created` on success
 
 ```json
{
  "identifier": "2",
  "name": "Rodolfo Freitas",
  "email": "rodolfolubeck@live.com",
  "sendDate": "27/05/2020"
}
```

## Lookup e-mail details
`GET /sent/int:<identifier>`

**Response**

- `404 Not Found` if the e-mail does not exist
- `200 OK` on success

```json

{
  "identifier": "2",
  "name": "Rodolfo Freitas",
  "email": "rodolfolubeck@live.com",
  "sendDate": "27/05/2020"
} 

```