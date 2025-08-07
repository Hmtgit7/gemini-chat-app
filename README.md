# 🤖 Gemini Chat App

A modern, full-stack AI chat application powered by Google's Gemini AI. Built with React, Django, and Tailwind CSS.

![App Screenshot](public/screenshot.png)

## ✨ Features

### Frontend
- 🎨 Clean, modern UI with dark/light mode
- 💬 Real-time chat interface with message history
- 📱 Responsive design for all devices
- 🔄 Loading states and error handling
- 📝 Markdown support for messages
- 🎯 Code syntax highlighting
- 📅 Chat history organization (Today, Yesterday, Last 7 Days)

### Backend
- 🤖 Google Gemini AI integration
- 🔒 Secure API endpoints
- 💾 Chat history persistence
- 🔄 Real-time message streaming
- 🛡️ CORS and CSRF protection

## 🛠️ Tech Stack

### Frontend
- React + Vite
- TypeScript
- Tailwind CSS + Shadcn UI
- React Query
- React Router
- Axios

### Backend
- Django
- Django REST Framework
- Google Generative AI SDK
- SQLite (can be configured for PostgreSQL)
- Python 3.x

## 🚀 Getting Started

### Prerequisites
- Node.js (v16+)
- Python (3.8+)
- Google Gemini API Key

### Installation

1. Clone the repository
```bash
git clone https://github.com/Hmtgit7/gemini-chat-app.git
cd gemini-chat-app
```

2. Set up the backend
```bash
cd backend
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

3. Configure environment variables
```bash
# Copy example env files
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env

# Edit the .env files with your configurations
```

4. Set up the frontend
```bash
cd frontend
npm install
```

5. Start the development servers

Backend:
```bash
cd backend
python manage.py migrate
python manage.py runserver
```

Frontend:
```bash
cd frontend
npm run dev
```

Visit `http://localhost:5173` to see the app in action!

## 📸 Screenshots

[Add your screenshots here]

## 🧠 How It Works

1. User sends a message through the React frontend
2. Message is sent to Django backend via REST API
3. Backend processes the message using Google's Gemini AI
4. AI response is streamed back to the frontend
5. Response is displayed in a chat-style interface with markdown support

## 🔐 Environment Variables

### Backend (.env)
```
DEBUG=True
SECRET_KEY=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key-here
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

### Frontend (.env)
```
VITE_API_BASE_URL=http://127.0.0.1:8000
VITE_DEV_SERVER_PORT=5173
VITE_ENABLE_DARK_MODE=true
```

## 🛣️ Roadmap

- [ ] User authentication
- [ ] Chat export functionality
- [ ] Image generation support
- [ ] Voice input/output
- [ ] Multiple conversation contexts
- [ ] Custom AI model settings

## 👨‍💻 Author

**Hemant Gehlod**
- GitHub: [@Hmtgit7](https://github.com/Hmtgit7)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini AI for the powerful language model
- Shadcn UI for the beautiful components
- The open-source community for inspiration and tools

---

Made with ❤️ by [Hemant Gehlod](https://github.com/Hmtgit7)
