# FastAPI Activity Management API

## Overview
This FastAPI project provides a simple activity management API with versioned endpoints. It supports creating, retrieving, updating, and deleting activities while enforcing authentication via an API key.

## Features
- **API Key Authentication**: Secure access using an API key.
- **Versioned API**: Supports `/apiv1` and `/apiv2` endpoints.
- **CRUD Operations**: Perform Create, Read, Update, and Delete actions on activities.
- **Environment Variables**: Uses `.env` file for API key security.
- **Health Check**: Provides a `/health` endpoint to verify API status.

## Installation
### Prerequisites
- Python 3.7+
- FastAPI
- Uvicorn
- Requests
- Python-dotenv

### Setup
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API key:
   ```sh
   LAB4_API_KEY=your_secret_api_key
   ```

5. Run the FastAPI application:
   ```sh
   uvicorn main:app --reload
   ```

## API Authentication
All endpoints require authentication using an API key, which must be provided in the `DI-KEY` header.

Example:
```sh
curl -H "DI-KEY: your_secret_api_key" http://127.0.0.1:8000/apiv1/activities/1
```

## Endpoints
### General Endpoints
| Method | Endpoint    | Description                        |
|--------|------------|------------------------------------|
| GET    | `/`        | API welcome message               |
| GET    | `/health`  | API health check                  |

### Versioned Endpoints
#### API v1 (`/apiv1`)
| Method | Endpoint                  | Description                        |
|--------|----------------------------|------------------------------------|
| GET    | `/activities/{activity_id}` | Retrieve a specific activity      |
| POST   | `/activities/`              | Create a new activity             |
| PATCH  | `/activities/{activity_id}` | Update an existing activity       |
| DELETE | `/activities/{activity_id}` | Delete an activity                |

#### API v2 (`/apiv2`)
| Method | Endpoint                  | Description                        |
|--------|----------------------------|------------------------------------|
| GET    | `/activities/{activity_id}` | Retrieve a specific activity (v2) |
| POST   | `/activities/`              | Create a new activity (v2)        |
| PATCH  | `/activities/{activity_id}` | Update an existing activity (v2)  |
| DELETE | `/activities/{activity_id}` | Delete an activity (v2)           |

## Example Requests
### Create an Activity (POST)
```sh
curl -X POST "http://127.0.0.1:8000/apiv1/activities/" \
     -H "Content-Type: application/json" \
     -H "DI-KEY: your_secret_api_key" \
     -d '{"name": "Complete Lab 4", "details": "Finish the assigned lab work", "is_done": false}'
```

### Retrieve an Activity (GET)
```sh
curl -X GET "http://127.0.0.1:8000/apiv1/activities/1" \
     -H "DI-KEY: your_secret_api_key"
```

### Update an Activity (PATCH)
```sh
curl -X PATCH "http://127.0.0.1:8000/apiv1/activities/1" \
     -H "Content-Type: application/json" \
     -H "DI-KEY: your_secret_api_key" \
     -d '{"is_done": true}'
```

### Delete an Activity (DELETE)
```sh
curl -X DELETE "http://127.0.0.1:8000/apiv1/activities/1" \
     -H "DI-KEY: your_secret_api_key"
```

## License
This project is open-source and available under the MIT License.

