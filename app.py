import os
import smtplib
from email.mime.text import MIMEText
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)
print("Environment variables loaded:")
print(f"EMAIL: {os.getenv('EMAIL')}")
print(f"PASSWORD: {'*' * len(os.getenv('PASSWORD', ''))}")  # Password hidden for security

app = FastAPI(
    title="Email API",
    description="A simple API for sending emails",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    receiver_email: str
    subject: str
    body_text: str

@app.post("/send-email")
async def send_email(email: EmailRequest):
    try:
        print(f"Received request to send email to: {email.receiver_email}")
        
        # Get sender email and password from environment variables
        sender_email = os.getenv("EMAIL")
        sender_password = os.getenv("PASSWORD")
        
        print(f"Sender email: {sender_email}")
        print(f"Using SMTP server: smtp.ethereal.email:587")
        
        if not all([sender_email, sender_password]):
            error_msg = "Email service not configured. Please set EMAIL and PASSWORD environment variables."
            print(f"Error: {error_msg}")
            raise HTTPException(status_code=500, detail=error_msg)

        # Create message
        msg = MIMEText(email.body_text)
        msg["Subject"] = email.subject
        msg["From"] = sender_email
        msg["To"] = email.receiver_email

        print("Attempting to connect to SMTP server...")
        # Send email using Ethereal Email for testing
        with smtplib.SMTP("smtp.ethereal.email", 587, timeout=10) as server:
            print("Connected to SMTP server, starting TLS...")
            server.starttls()
            print("TLS started, attempting to log in...")
            server.login(sender_email, sender_password)
            print("Login successful, sending message...")
            server.send_message(msg)
            print("Message sent successfully")

        return {"message": "Email sent successfully"}

    except smtplib.SMTPException as e:
        error_msg = f"SMTP Error: {str(e)}"
        print(f"Error: {error_msg}")
        raise HTTPException(status_code=500, detail=error_msg)
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(f"Error: {error_msg}")
        raise HTTPException(status_code=500, detail=error_msg)

# Lambda handler for AWS deployment
def handler(event, context):
    from mangum import Mangum
    handler = Mangum(app)
    return handler(event, context)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
