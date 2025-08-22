# API Specification - AI Multi-Agent Content Creation & Marketing System

This document provides comprehensive API documentation for the AI Multi-Agent Content Creation & Marketing System, including all endpoints, request/response schemas, and examples.

## 🔗 Base URL

- **Development**: `http://localhost:8000`
- **Production**: `https://api.ai-multi-agent.com`

## 📋 API Versioning

All endpoints are versioned under `/api/v1/`

## 🔐 Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the token in the Authorization header:

```
Authorization: Bearer <your-jwt-token>
```

## 📊 Response Format

All API responses follow this standard format:

```json
{
  "success": true,
  "data": {
    // Response data
  },
  "message": "Operation completed successfully",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

Error responses:

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": {
      "field": "email",
      "issue": "Invalid email format"
    }
  },
  "timestamp": "2024-01-15T10:30:00Z"
}
```

## 🔑 Authentication Endpoints

### POST `/api/v1/auth/register`

Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123",
  "first_name": "John",
  "last_name": "Doe",
  "company": "Acme Corp",
  "role": "marketer"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": "user_123",
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "company": "Acme Corp",
      "role": "marketer",
      "created_at": "2024-01-15T10:30:00Z"
    },
    "tokens": {
      "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "expires_in": 1800
    }
  },
  "message": "User registered successfully"
}
```

### POST `/api/v1/auth/login`

Authenticate user and receive access tokens.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "user": {
      "id": "user_123",
      "email": "user@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "company": "Acme Corp",
      "role": "marketer"
    },
    "tokens": {
      "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "expires_in": 1800
    }
  },
  "message": "Login successful"
}
```

### POST `/api/v1/auth/refresh`

Refresh access token using refresh token.

**Request Body:**
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "expires_in": 1800
  },
  "message": "Token refreshed successfully"
}
```

### POST `/api/v1/auth/logout`

Logout user and invalidate tokens.

**Response:**
```json
{
  "success": true,
  "message": "Logout successful"
}
```

## 📝 Content Management Endpoints

### GET `/api/v1/content`

Get paginated list of content items.

**Query Parameters:**
- `page` (int): Page number (default: 1)
- `limit` (int): Items per page (default: 20)
- `status` (string): Filter by status (draft, published, archived)
- `type` (string): Filter by content type (blog, social, email)
- `search` (string): Search in title and content

**Response:**
```json
{
  "success": true,
  "data": {
    "content": [
      {
        "id": "content_123",
        "title": "10 AI Marketing Strategies",
        "type": "blog",
        "status": "published",
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-15T11:00:00Z",
        "author": {
          "id": "user_123",
          "name": "John Doe"
        }
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 150,
      "pages": 8
    }
  }
}
```

### POST `/api/v1/content`

Create new content item.

**Request Body:**
```json
{
  "title": "AI-Powered Content Creation Guide",
  "type": "blog",
  "brief": "Create a comprehensive guide on AI-powered content creation",
  "target_audience": "marketers and content creators",
  "tone": "professional",
  "style": "informative",
  "keywords": ["AI", "content creation", "marketing"],
  "word_count": 1500
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "content": {
      "id": "content_456",
      "title": "AI-Powered Content Creation Guide",
      "type": "blog",
      "status": "draft",
      "brief": "Create a comprehensive guide on AI-powered content creation",
      "target_audience": "marketers and content creators",
      "tone": "professional",
      "style": "informative",
      "keywords": ["AI", "content creation", "marketing"],
      "word_count": 1500,
      "created_at": "2024-01-15T12:00:00Z",
      "author": {
        "id": "user_123",
        "name": "John Doe"
      }
    }
  },
  "message": "Content created successfully"
}
```

### GET `/api/v1/content/{content_id}`

Get specific content item by ID.

**Response:**
```json
{
  "success": true,
  "data": {
    "content": {
      "id": "content_123",
      "title": "10 AI Marketing Strategies",
      "type": "blog",
      "status": "published",
      "content": "Full content text here...",
      "brief": "Original brief",
      "target_audience": "marketers",
      "tone": "professional",
      "style": "informative",
      "keywords": ["AI", "marketing"],
      "word_count": 1500,
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T11:00:00Z",
      "author": {
        "id": "user_123",
        "name": "John Doe"
      },
      "versions": [
        {
          "id": "version_1",
          "content": "Previous version content",
          "created_at": "2024-01-15T10:30:00Z"
        }
      ]
    }
  }
}
```

### PUT `/api/v1/content/{content_id}`

Update content item.

**Request Body:**
```json
{
  "title": "Updated AI Marketing Strategies",
  "content": "Updated content text...",
  "status": "published"
}
```

### DELETE `/api/v1/content/{content_id}`

Delete content item.

**Response:**
```json
{
  "success": true,
  "message": "Content deleted successfully"
}
```

## 🤖 AI Agent Endpoints

### POST `/api/v1/agents/generate`

Generate content using AI agents.

**Request Body:**
```json
{
  "content_id": "content_123",
  "agents": ["ideation", "writer", "optimizer"],
  "options": {
    "tone": "professional",
    "style": "informative",
    "include_seo": true,
    "include_hashtags": true
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "job_id": "job_789",
    "status": "processing",
    "estimated_completion": "2024-01-15T12:05:00Z",
    "agents": [
      {
        "name": "ideation",
        "status": "completed",
        "progress": 100
      },
      {
        "name": "writer",
        "status": "processing",
        "progress": 65
      },
      {
        "name": "optimizer",
        "status": "pending",
        "progress": 0
      }
    ]
  },
  "message": "Content generation started"
}
```

### GET `/api/v1/agents/status/{job_id}`

Get status of content generation job.

**Response:**
```json
{
  "success": true,
  "data": {
    "job_id": "job_789",
    "status": "completed",
    "progress": 100,
    "result": {
      "content": "Generated content text...",
      "seo_optimized": true,
      "hashtags": ["#AI", "#Marketing"],
      "word_count": 1500,
      "readability_score": 85
    },
    "agents": [
      {
        "name": "ideation",
        "status": "completed",
        "progress": 100,
        "output": "Content ideas and outline"
      },
      {
        "name": "writer",
        "status": "completed",
        "progress": 100,
        "output": "Draft content"
      },
      {
        "name": "optimizer",
        "status": "completed",
        "progress": 100,
        "output": "SEO optimized content"
      }
    ]
  }
}
```

### GET `/api/v1/agents/history`

Get history of AI agent jobs.

**Query Parameters:**
- `page` (int): Page number
- `limit` (int): Items per page
- `status` (string): Filter by status

**Response:**
```json
{
  "success": true,
  "data": {
    "jobs": [
      {
        "id": "job_789",
        "content_id": "content_123",
        "status": "completed",
        "created_at": "2024-01-15T12:00:00Z",
        "completed_at": "2024-01-15T12:05:00Z",
        "agents_used": ["ideation", "writer", "optimizer"]
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 50,
      "pages": 3
    }
  }
}
```

## 📈 Marketing Automation Endpoints

### POST `/api/v1/marketing/campaigns`

Create new marketing campaign.

**Request Body:**
```json
{
  "name": "Q1 AI Marketing Campaign",
  "content_ids": ["content_123", "content_456"],
  "channels": ["social_media", "email", "blog"],
  "schedule": {
    "start_date": "2024-01-20T09:00:00Z",
    "end_date": "2024-03-31T18:00:00Z",
    "frequency": "weekly"
  },
  "target_audience": {
    "demographics": ["marketers", "content creators"],
    "interests": ["AI", "marketing automation"]
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "campaign": {
      "id": "campaign_123",
      "name": "Q1 AI Marketing Campaign",
      "status": "scheduled",
      "content_count": 2,
      "channels": ["social_media", "email", "blog"],
      "schedule": {
        "start_date": "2024-01-20T09:00:00Z",
        "end_date": "2024-03-31T18:00:00Z",
        "frequency": "weekly"
      },
      "created_at": "2024-01-15T13:00:00Z"
    }
  },
  "message": "Campaign created successfully"
}
```

### GET `/api/v1/marketing/campaigns`

Get list of marketing campaigns.

**Response:**
```json
{
  "success": true,
  "data": {
    "campaigns": [
      {
        "id": "campaign_123",
        "name": "Q1 AI Marketing Campaign",
        "status": "active",
        "content_count": 2,
        "channels": ["social_media", "email", "blog"],
        "performance": {
          "reach": 15000,
          "engagement": 1200,
          "conversions": 45
        },
        "created_at": "2024-01-15T13:00:00Z"
      }
    ]
  }
}
```

### POST `/api/v1/marketing/distribute`

Distribute content to specified channels.

**Request Body:**
```json
{
  "content_id": "content_123",
  "channels": ["twitter", "linkedin", "email"],
  "schedule": "2024-01-16T10:00:00Z",
  "customizations": {
    "twitter": {
      "hashtags": ["#AI", "#Marketing"],
      "character_limit": 280
    },
    "linkedin": {
      "hashtags": ["#ArtificialIntelligence", "#DigitalMarketing"],
      "include_image": true
    },
    "email": {
      "subject_line": "AI Marketing Strategies You Need to Know",
      "preview_text": "Discover the latest AI-powered marketing techniques"
    }
  }
}
```

## 📊 Analytics Endpoints

### GET `/api/v1/analytics/overview`

Get analytics overview dashboard data.

**Query Parameters:**
- `period` (string): Time period (7d, 30d, 90d, 1y)

**Response:**
```json
{
  "success": true,
  "data": {
    "overview": {
      "total_content": 150,
      "published_content": 120,
      "total_campaigns": 25,
      "active_campaigns": 8,
      "total_reach": 500000,
      "total_engagement": 25000,
      "conversion_rate": 3.2
    },
    "performance": {
      "content_performance": [
        {
          "content_id": "content_123",
          "title": "AI Marketing Guide",
          "views": 15000,
          "engagement": 1200,
          "conversions": 45
        }
      ],
      "channel_performance": [
        {
          "channel": "social_media",
          "reach": 250000,
          "engagement": 15000,
          "conversion_rate": 2.8
        }
      ]
    },
    "trends": {
      "content_creation": [
        {"date": "2024-01-01", "count": 5},
        {"date": "2024-01-02", "count": 8}
      ],
      "engagement": [
        {"date": "2024-01-01", "count": 1200},
        {"date": "2024-01-02", "count": 1500}
      ]
    }
  }
}
```

### GET `/api/v1/analytics/content/{content_id}`

Get detailed analytics for specific content.

**Response:**
```json
{
  "success": true,
  "data": {
    "content_analytics": {
      "content_id": "content_123",
      "title": "AI Marketing Guide",
      "views": 15000,
      "unique_views": 12000,
      "engagement": 1200,
      "likes": 800,
      "shares": 300,
      "comments": 100,
      "conversions": 45,
      "conversion_rate": 3.0,
      "avg_time_on_page": 180,
      "bounce_rate": 25.5,
      "channel_breakdown": [
        {
          "channel": "social_media",
          "views": 8000,
          "engagement": 600
        },
        {
          "channel": "email",
          "views": 5000,
          "engagement": 400
        },
        {
          "channel": "organic",
          "views": 2000,
          "engagement": 200
        }
      ],
      "geographic_data": [
        {
          "country": "United States",
          "views": 8000,
          "percentage": 53.3
        },
        {
          "country": "United Kingdom",
          "views": 3000,
          "percentage": 20.0
        }
      ]
    }
  }
}
```

## 🔌 WebSocket Endpoints

### WebSocket `/api/v1/websocket`

Real-time WebSocket connection for live updates.

**Connection URL:** `ws://localhost:8000/api/v1/websocket`

**Authentication:** Include JWT token in query parameter
```
ws://localhost:8000/api/v1/websocket?token=<jwt-token>
```

**Message Types:**

1. **Content Generation Updates:**
```json
{
  "type": "content_generation_update",
  "job_id": "job_789",
  "status": "processing",
  "progress": 65,
  "agent_status": [
    {
      "name": "writer",
      "status": "processing",
      "progress": 65
    }
  ]
}
```

2. **Real-time Collaboration:**
```json
{
  "type": "collaboration_update",
  "content_id": "content_123",
  "user_id": "user_456",
  "action": "typing",
  "position": 150,
  "timestamp": "2024-01-15T12:30:00Z"
}
```

3. **Campaign Performance:**
```json
{
  "type": "campaign_update",
  "campaign_id": "campaign_123",
  "metrics": {
    "reach": 15000,
    "engagement": 1200,
    "conversions": 45
  }
}
```

## 🚨 Error Codes

| Code | Description |
|------|-------------|
| `VALIDATION_ERROR` | Invalid request data |
| `AUTHENTICATION_ERROR` | Invalid or missing authentication |
| `AUTHORIZATION_ERROR` | Insufficient permissions |
| `NOT_FOUND` | Resource not found |
| `RATE_LIMIT_EXCEEDED` | Too many requests |
| `INTERNAL_ERROR` | Server error |
| `AGENT_ERROR` | AI agent processing error |
| `CONTENT_GENERATION_ERROR` | Content generation failed |

## 📝 Rate Limits

- **Authentication endpoints**: 10 requests per minute
- **Content endpoints**: 100 requests per minute
- **AI agent endpoints**: 50 requests per minute
- **Analytics endpoints**: 200 requests per minute
- **WebSocket connections**: 10 concurrent connections per user

## 🔒 Security

- All endpoints require authentication except `/health`
- JWT tokens expire after 30 minutes
- Refresh tokens expire after 7 days
- Rate limiting applied to all endpoints
- CORS configured for frontend domains
- Input validation on all endpoints
- SQL injection protection via SQLAlchemy
- XSS protection via content sanitization

This API specification provides a complete reference for integrating with the AI Multi-Agent Content Creation & Marketing System.
