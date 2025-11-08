# AWS Serverless Email API with FastAPI & AWS Lambda

A production-ready, serverless email API service built with FastAPI and deployed on AWS Lambda. This service provides a simple HTTP endpoint for sending emails using SMTP, with built-in error handling and environment-based configuration.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Serverless](https://img.shields.io/badge/Serverless-3.x-FF4E8D?logo=serverless)](https://www.serverless.com/)

## Features

- **RESTful API** - Simple HTTP endpoint for sending emails
- **Serverless** - Deployed on AWS Lambda for infinite scalability
- **FastAPI** - High performance, easy-to-use API framework with automatic docs
- **Environment Variables** - Secure configuration management
- **Ethereal Email** - Built-in integration for testing
- **Comprehensive Error Handling** - Graceful handling of SMTP timeouts and failures
- **API Documentation** - Automatic OpenAPI documentation at `/docs`

## Quick Start

### Prerequisites

- Python 3.8+
- [Node.js](https://nodejs.org/) (for Serverless Framework)
- [AWS CLI](https://aws.amazon.com/cli/) configured with appropriate credentials
- [Serverless Framework](https://www.serverless.com/) (`npm install -g serverless`)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/aws-serverless-email-api.git
   cd aws-serverless-email-api
   ```

2. **Set up virtual environment and install dependencies**
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Install Serverless plugins
   npm install
   ```

3. **Configure environment variables**
   Create a `.env` file in the project root:
   ```env
   # For development with Ethereal Email (https://ethereal.email/)
   EMAIL=your_ethereal_email@example.com
   PASSWORD=your_ethereal_password
   
   # For production (AWS Lambda)
   # These will be set in AWS Lambda environment variables
   # EMAIL=your_production_email@example.com
   # PASSWORD=your_smtp_password
   ```

4. **Run locally**
   ```bash
   # Option 1: Using Serverless Offline
   serverless offline
   
   # Option 2: Directly with Uvicorn (faster for development)
   uvicorn app:app --reload
   ```

   The API will be available at `http://localhost:3000` (Serverless Offline) or `http://localhost:8000` (Uvicorn).

## API Documentation

Once running, access the interactive API documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Send Email

**Endpoint:** `POST /send-email`

**Request Body:**
```json
{
  "receiver_email": "recipient@example.com",
  "subject": "Test Email",
  "body_text": "This is a test email from the API."
}
```

**Success Response (200 OK):**
```json
{
  "message": "Email sent successfully"
}
```

**Error Responses:**
- `400 Bad Request`: Missing required fields
- `500 Internal Server Error`: SMTP connection or sending failed

## Deployment

### Prerequisites
- AWS Account with appropriate IAM permissions
- AWS CLI configured with credentials
- Serverless Framework installed globally (`npm install -g serverless`)

### Deploy to AWS

1. **Configure AWS Credentials**
   ```bash
   aws configure
   ```

2. **Deploy the service**
   ```bash
   serverless deploy
   ```

3. **Set environment variables in AWS Lambda**
   After deployment, set the following environment variables in your AWS Lambda function:
   - `EMAIL`: Your SMTP email
   - `PASSWORD`: Your SMTP password

## 🔧 Configuration

### Environment Variables

| Variable  | Description | Required | Default |
|-----------|-------------|----------|---------|
| `EMAIL` | SMTP username/email | Yes | - |
| `PASSWORD` | SMTP password | Yes | - |
| `SMTP_HOST` | SMTP server host | No | `smtp.ethereal.email` |
| `SMTP_PORT` | SMTP server port | No | `587` |

### serverless.yml

Key configurations in `serverless.yml`:
- Runtime: Python 3.10
- Memory: 512MB
- Timeout: 30 seconds
- Region: ap-south-1 (Mumbai)

## Testing

### Manual Testing

Using cURL:
```bash
curl -X POST "http://localhost:8000/send-email" \
  -H "Content-Type: application/json" \
  -d '{
    "receiver_email": "test@example.com",
    "subject": "Test Email",
    "body_text": "This is a test email from the API."
  }'
```

## Project Structure

```
aws-serverless-email-api/
├── .gitignore            # Git ignore file
├── README.md             # This file
├── app.py                # Main FastAPI application
├── package.json          # Node.js dependencies
├── requirements.txt      # Python dependencies
└── serverless.yml        # Serverless Framework configuration
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## API Usage

Send an email using the `/send-email` endpoint:

```bash
curl -X POST https://your-api-url/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "receiver_email": "recipient@example.com",
    "subject": "Test Email",
    "body_text": "This is a test email."
  }'
```

### Request Body Parameters

- `receiver_email` (required): Email address of the recipient
- `subject` (required): Subject line of the email
- `body_text` (required): Content of the email

### Response

Success:

```json
{
  "message": "Email sent successfully"
}
```

Error:

```json
{
  "message": "Error message",
  "error": "Detailed error description"
}
```

## Deployment

Deploy to AWS:

```bash
serverless deploy
```

After deployment, you'll receive an API endpoint URL that you can use to make requests.

## Error Handling

The API includes handling for:

- Missing required fields
- SMTP timeouts
- SMTP server errors
- Invalid credentials

## Dependencies

Key dependencies include:

- **FastAPI**: Web framework for building APIs.
- **Uvicorn**: ASGI server for local development.
- **Mangum**: AWS Lambda handler for ASGI applications.
- **python-dotenv**: Environment variable management.

For a complete list of dependencies, see `requirements.txt`.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Serverless Framework](https://www.serverless.com/) - Serverless deployment
- [Ethereal Email](https://ethereal.email/) - For testing email functionality

## License

This project is licensed under the MIT License.
