# user-content-service-fastapi
Production-ready RESTful backend built with FastAPI, PostgreSQL, JWT authentication, and Alembic migrations, supporting secure user management, post creation, and voting functionality.


# Production-Ready REST API with FastAPI

This project is a production-ready RESTful API built using FastAPI. It provides user authentication, post management, and a voting system, backed by a PostgreSQL database and deployed on Render.

## Features

- User authentication using JWT tokens  
- Secure login system with OAuth2 password flow  
- CRUD operations for posts  
- Voting system (like/unlike posts)  
- PostgreSQL database integration using SQLAlchemy  
- Database migrations using Alembic  
- Environment-based configuration using Pydantic Settings  
- Deployed on cloud using Render  

## Tech Stack

- Backend: FastAPI  
- Database: PostgreSQL  
- ORM: SQLAlchemy  
- Migrations: Alembic  
- Authentication: JWT (JSON Web Tokens)  
- Deployment: Render  

## Project Structure

```
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── oauth2.py
├── utils.py
├── routers/
│   ├── auth.py
│   ├── users.py
│   ├── posts.py
│   └── vote.py
```

## API Endpoints

### Authentication
- POST /login  

### Users
- POST /users  
- GET /users/{id}  

### Posts
- GET /posts/  
- GET /posts/{id}  
- POST /posts/  
- PUT /posts/{id}  
- DELETE /posts/{id}  

### Voting
- POST /vote  

## Running Locally

1. Clone the repository  
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Create virtual environment  
```
python -m venv env
env\Scripts\activate
```

3. Install dependencies  
```
pip install -r requirements.txt
```

4. Set environment variables in `.env`  
```
DATABASE_URL=your_local_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run the application  
```
uvicorn app.main:app --reload
```

## Deployment

The application is deployed on Render with a managed PostgreSQL database.

Live API documentation:  
https://your-app-name.onrender.com/docs

## Future Improvements

- Add frontend interface (React or Next.js)  
- Implement pagination and filtering  
- Add unit and integration tests  
- Dockerize the application  
- Add rate limiting and caching  

## Author

Sujal Didwaniya
