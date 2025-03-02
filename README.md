# Egyptian National ID Validator API

## Description

This project is a Django-based API that validates Egyptian National IDs and extracts relevant information from them. The API checks the validity of the ID, extracts details such as birth date, governorate, gender, serial number, and check digit, and implements rate limiting. Additionally, API key authentication is used for secure access. The project also includes GitHub Actions for CI/CD and unit tests to ensure the reliability of the implementation.

## Cloning the Project

To get started, clone the repository using the following command:

```sh
git clone https://github.com/MichelRaouf/id-validator
cd national_id_api
```

## Running the Server

Start the development server with:

```sh
python manage.py runserver
```

## Testing the API in Postman

To test the API, send a `POST` request to:

```
http://127.0.0.1:8000/api/validate/
```

### Headers:

```
Content-Type: application/json
Authorization: Api-Key 2vmQFr3c.5kvn2NqfFhNNVstqvh0rvy6nSvHo2edI
```

### Request Body:

```json
{
  "national_id": "30010251200571"
}
```

### Example Response:

```json
{
  "birth_date": "2000-10-25",
  "governorate": "Dakahlia",
  "gender": "Male",
  "serial_number": "0057",
  "check_digit": "1"
}
```

## Additional Features

- Implemented API key authentication for secure access.
- Added rate limiting to prevent excessive requests.
- Configured GitHub Actions for continuous integration and testing.
- Developed unit tests to ensure API correctness and stability.
