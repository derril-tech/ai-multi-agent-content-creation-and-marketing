# Backend - AI Multi-Agent Content Creation & Marketing System

This is the backend API for the AI Multi-Agent Content Creation & Marketing System, built with FastAPI, SQLAlchemy 2.0, PostgreSQL, and Redis.

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- PostgreSQL 13+ with pgvector extension
- Redis 6+
- Docker (optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-multi-agent-content-creation-and-marketing/backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Set up database**
   ```bash
   # Create PostgreSQL database
   createdb ai_multi_agent
   
   # Run migrations (when implemented)
   alembic upgrade head
   ```

6. **Start the development server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

7. **Access the API**
   - API: [http://localhost:8000](http://localhost:8000)
   - Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Health check: [http://localhost:8000/health](http://localhost:8000/health)

## 📁 Project Structure

```
app/
├── main.py                 # FastAPI application entry point
├── core/                   # Core application modules
│   ├── config.py          # Configuration settings
│   ├── database.py        # Database connection and models
│   ├── redis.py           # Redis connection and caching
│   ├── logging.py         # Structured logging setup
│   ├── security.py        # Authentication and authorization
│   └── exceptions.py      # Custom exception handlers
├── api/                    # API endpoints and routers
│   └── v1/                # API version 1
│       ├── api.py         # Main API router
│       └── endpoints/     # Individual endpoint modules
├── models/                 # SQLAlchemy database models
├── schemas/                # Pydantic request/response schemas
├── services/               # Business logic services
├── agents/                 # AI agent implementations
└── utils/                  # Utility functions and helpers
```

## 🛠️ Available Scripts

- `uvicorn main:app --reload` - Start development server
- `pytest` - Run tests
- `pytest --cov=app` - Run tests with coverage
- `black .` - Format code
- `isort .` - Sort imports
- `flake8 .` - Lint code
- `mypy app/` - Type checking

## 🔧 Configuration

### Environment Variables

Copy `env.example` to `.env` and configure:

```env
# Application Settings
APP_NAME=AI Multi-Agent Content Creation & Marketing System
VERSION=1.0.0
DEBUG=false
ENVIRONMENT=development

# Database Settings
DATABASE_URL=postgresql+asyncpg://user:password@localhost/ai_multi_agent

# Redis Settings
REDIS_URL=redis://localhost:6379

# AI API Settings
OPENAI_API_KEY=your-openai-api-key
ANTHROPIC_API_KEY=your-anthropic-api-key

# Security Settings
SECRET_KEY=your-super-secret-key-change-in-production
```

### Database Setup

1. **Install PostgreSQL with pgvector**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install postgresql postgresql-contrib
   
   # macOS
   brew install postgresql
   ```

2. **Enable pgvector extension**
   ```sql
   CREATE EXTENSION IF NOT EXISTS vector;
   ```

3. **Create database**
   ```bash
   createdb ai_multi_agent
   ```

### Redis Setup

1. **Install Redis**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install redis-server
   
   # macOS
   brew install redis
   ```

2. **Start Redis**
   ```bash
   redis-server
   ```

## 🧪 Testing

The project uses pytest for testing:

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_auth.py

# Run tests in parallel
pytest -n auto
```

## 📦 Build and Deployment

### Development

```bash
# Start development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production

```bash
# Start production server
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker Deployment

```bash
# Build Docker image
docker build -t ai-multi-agent-backend .

# Run container
docker run -p 8000:8000 ai-multi-agent-backend
```

## 🔗 API Documentation

### Interactive Documentation

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### API Endpoints

#### Authentication
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login
- `POST /api/v1/auth/refresh` - Token refresh
- `POST /api/v1/auth/logout` - User logout

#### Content Management
- `GET /api/v1/content` - List content
- `POST /api/v1/content` - Create content
- `GET /api/v1/content/{id}` - Get content
- `PUT /api/v1/content/{id}` - Update content
- `DELETE /api/v1/content/{id}` - Delete content

#### AI Agents
- `POST /api/v1/agents/generate` - Generate content
- `GET /api/v1/agents/status/{job_id}` - Get generation status
- `GET /api/v1/agents/history` - Get generation history

#### Marketing
- `POST /api/v1/marketing/campaigns` - Create campaign
- `GET /api/v1/marketing/campaigns` - List campaigns
- `POST /api/v1/marketing/distribute` - Distribute content

#### Analytics
- `GET /api/v1/analytics/overview` - Get analytics overview
- `GET /api/v1/analytics/content/{id}` - Get content analytics

#### WebSocket
- `WS /api/v1/websocket` - Real-time communication

## 🤖 AI Integration

The backend integrates with multiple AI services:

### OpenAI GPT-4
- Content generation
- Text optimization
- SEO enhancement

### Anthropic Claude
- Advanced reasoning
- Compliance checking
- Content validation

### LangChain
- Agent orchestration
- Workflow management
- Tool integration

## 🔒 Security

- **Authentication**: JWT token-based authentication
- **Authorization**: Role-based access control (RBAC)
- **Rate Limiting**: Configurable rate limits per endpoint
- **CORS**: Cross-origin resource sharing configuration
- **Input Validation**: Pydantic schema validation
- **SQL Injection Protection**: SQLAlchemy ORM
- **XSS Protection**: Content sanitization

## 📊 Monitoring

### Health Checks

- `GET /health` - Basic health check
- `GET /health/detailed` - Detailed system status

### Metrics

- Prometheus metrics endpoint
- Custom business metrics
- Performance monitoring

### Logging

- Structured logging with structlog
- JSON format in production
- Configurable log levels

## 🐛 Troubleshooting

### Common Issues

1. **Database connection error**
   ```bash
   # Check PostgreSQL status
   sudo systemctl status postgresql
   
   # Check connection
   psql -h localhost -U postgres -d ai_multi_agent
   ```

2. **Redis connection error**
   ```bash
   # Check Redis status
   redis-cli ping
   
   # Start Redis if not running
   redis-server
   ```

3. **Import errors**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --force-reinstall
   ```

### Getting Help

- Check the [FastAPI documentation](https://fastapi.tiangolo.com/)
- Review the [SQLAlchemy documentation](https://docs.sqlalchemy.org/)
- Open an issue in the repository

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
