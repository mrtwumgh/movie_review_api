# Movie Review API

A RESTful API built with Django and Django REST Framework that allows users to create and manage movie reviews. The API integrates with external movie database, TMDb to fetch movie details and supports features like user authentication, profiles, likes, and comments.

## Features

-   **User Authentication**: Secure user registration and login using token-based authentication.
-   **User Profiles**: Users have profiles with a bio and can view their own and others' profiles.
-   **Movie Reviews**: Users can create, read, update, and delete movie reviews.
-   **External API Integration**:
    -   **TMDb API**: Enables partial matching for movie titles.
-   **Likes System**: Users can like or unlike reviews.
-   **Comments**: Users can comment on reviews.

## Getting Started

### Prerequisites

-   **Python 3.8** or higher
-   **pip** (Python package installer)
-   **Git** (optional, for cloning the repository)

1. **Clone the Repository**
`git clone https://github.com/yourusername/movie-review-api.git
cd movie-review-api`
2. **Create a Virtual Environment**
`python -m venv venv`
3. **Activate the Virtual Environment**
-   On macOS and Linux:
    `source venv/bin/activate` 
    
-   On Windows:
    `venv\Scripts\activate`
4. **Install Dependencies**
`pip install -r requirements.txt`

### Environment Variables

Create a `.env` file in the root directory and add the following environment variables:
`SECRET_KEY=your-secret-key
OMDB_API_KEY=your-omdb-api-key
TMDB_API_KEY=your-tmdb-api-key` 

-   **SECRET_KEY**: Django secret key for cryptographic signing.
-   **TMDB_API_KEY**: API key for The Movie Database (TMDb) API.

### Database Migration

Apply database migrations:
`python manage.py makemigrations
python manage.py migrate` 

### Running the Server

Start the development server:
`python manage.py runserver` 

The API will be accessible at `http://127.0.0.1:8000/api`.

## API Documentation

### Authentication

The API uses token-based authentication. Obtain a token by logging in and include it in the `Authorization` header for protected endpoints.

**Obtain Auth Token**

-   **Endpoint**: `POST /api/login/`
    
-   **Request Body**:
- 
    `{
      "username": "test_user",
      "password": "test_password"
    }` 
    
-   **Response**:
    `{
      "token": "your-auth-token"
    }` 
    

Include the token in the header:
`Authorization: Token your-auth-token` 

### User Endpoints

#### Register

-   **Endpoint**: `POST /api/register/`
    
-   **Request Body**:
    `{
      "username": "test_name",
      "email": "test_email@test.com",
      "password": "test_password",
      "password2": "test_password"
    }` 
    

#### User Profile

-   **Get Profile**
    
    -   **Endpoint**: `GET /api/profile/`
        
    -   **Headers**: Requires authentication.
        
    -   **Response**:
        `{
          "id": 1,
          "username": "yourusername",
          "email": "youremail@example.com",
          "profile": {
	        "image": "default.jpg"
            "bio": "Your bio here"
          },
          "reviews": [
            // List of user's reviews
          ]
        }` 
        
-   **Update Profile**
    
    -   **Endpoint**: `PUT /api/profile/`
        
    -   **Headers**: Requires authentication.
        
    -   **Request Body**:
        `{
          "email": "newemail@example.com",
          "profile": {
            "image": "default.jpg"
            "bio": "Updated bio"
          }
        }` 
        

### Review Endpoints

#### Create Review

-   **Endpoint**: `POST /api/reviews/create/`
    
-   **Headers**: Requires authentication.
    
-   **Request Body**:
    `{
      "movie_title": "Inception",
      "review_content": "Amazing movie!",
      "rating": 5
    }` 
    
-   **Response**:
    `{
      "id": 1,
      "movie_title": "Inception",
      "review_content": "Amazing movie!",
      "rating": 5,
      "created_date": "2023-10-05T14:00:00Z",
      "total_likes": 0,
      "comments": [],
      "movie_details": {
        "title": "Inception",
        "year": "2010",
        "description": "A mind-bending thriller...",
        "genre": ["Action", "Science Fiction", "Adventure"],
        "country_of_origin": ["United States of America", "United Kingdom"]
      }
    }` 
    

#### List Reviews

-   **Endpoint**: `GET /api/reviews/`
-   **Response**: List of all reviews.

#### Retrieve Review

-   **Endpoint**: `GET /api/reviews/{id}/`
-   **Response**: Details of a specific review.

#### Update Review

-   **Endpoint**: `PUT /api/reviews/{id}/update/`
-   **Headers**: Requires authentication (owner only).

#### Delete Review

-   **Endpoint**: `DELETE /api/reviews/{id}/delete/`
-   **Headers**: Requires authentication (owner only).

### Like Endpoints

#### Like a Review

-   **Endpoint**: `POST /api/reviews/{id}/like/`
    
-   **Headers**: Requires authentication.
    
-   **Request Body**:
    `{
      "review": 1
    }` 
    

#### Unlike a Review

-   **Endpoint**: `DELETE /api/reviews/{id}/unlike/`
-   **Headers**: Requires authentication.

### Comment Endpoints

#### List/Create Comments

-   **Endpoint**: `GET /api/reviews/{review_id}/comments/`
    
-   **Endpoint**: `POST /api/reviews/{review_id}/comments/`
    
-   **Headers**: POST requires authentication.
    
-   **Request Body for POST**:
    `{
      "content": "Great review!"
    }` 
    

#### Retrieve/Update/Delete Comment

-   **Endpoint**: `GET /api/comments/{id}/`
-   **Endpoint**: `PUT /api/comments/{id}/update/`
-   **Endpoint**: `DELETE /api/comments/{id}/delete/`
-   **Headers**: Requires authentication (owner only for PUT and DELETE).


## Deployment

To deploy the API on platforms like **Heroku** or **PythonAnywhere**, follow these general steps:

1.  **Create an account** on your chosen platform.
    
2.  **Create a new application** in your dashboard.
    
3.  **Set environment variables** in the application's settings.
    
4.  **Deploy your code** using Git or any other deployment method provided by the platform.
    
5.  **Test your deployed API** by accessing the public URL provided by the platform.
    

----------

**Note**: These steps provide a high-level overview. For detailed instructions specific to each platform, refer to their official documentation.