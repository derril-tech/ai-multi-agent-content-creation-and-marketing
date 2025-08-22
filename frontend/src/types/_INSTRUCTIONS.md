# Types Directory Instructions

## Purpose
This directory contains TypeScript type definitions, interfaces, and type utilities for the AI Multi-Agent Content Creation & Marketing System frontend.

## Structure
```
types/
├── index.ts              # Main type exports
├── api.ts                # API request/response types
├── auth.ts               # Authentication types
├── content.ts            # Content management types
├── agents.ts             # AI agent types
├── marketing.ts          # Marketing and campaigns types
├── analytics.ts          # Analytics and metrics types
├── ui.ts                 # UI component types
├── common.ts             # Common utility types
├── websocket.ts          # WebSocket message types
└── _INSTRUCTIONS.md      # This file
```

## Implementation Guidelines

### Type Design Principles
- **Comprehensive**: Cover all data structures and API contracts
- **Strict**: Use strict TypeScript configurations
- **Reusable**: Create generic types where appropriate
- **Documented**: Include JSDoc comments for complex types
- **Consistent**: Follow naming conventions and patterns
- **Extensible**: Design types to accommodate future changes

### API Types (`api.ts`)

#### Request/Response Patterns
```typescript
// Base API response structure
interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
  timestamp: string;
}

// Paginated responses
interface PaginatedResponse<T> extends ApiResponse<T[]> {
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}

// Error responses
interface ApiError {
  code: string;
  message: string;
  details?: Record<string, any>;
  timestamp: string;
}
```

#### HTTP Methods
```typescript
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH';

interface ApiRequest<T = any> {
  method: HttpMethod;
  url: string;
  data?: T;
  params?: Record<string, any>;
  headers?: Record<string, string>;
}
```

### Authentication Types (`auth.ts`)

#### User Types
```typescript
interface User {
  id: string;
  email: string;
  username: string;
  firstName: string;
  lastName: string;
  avatar?: string;
  role: UserRole;
  isActive: boolean;
  createdAt: string;
  updatedAt: string;
}

type UserRole = 'admin' | 'manager' | 'creator' | 'viewer';

interface UserProfile extends User {
  bio?: string;
  company?: string;
  website?: string;
  socialLinks?: SocialLinks;
  preferences: UserPreferences;
}
```

#### Authentication Types
```typescript
interface LoginCredentials {
  email: string;
  password: string;
  rememberMe?: boolean;
}

interface RegisterData {
  email: string;
  password: string;
  confirmPassword: string;
  firstName: string;
  lastName: string;
  username: string;
  acceptTerms: boolean;
}

interface AuthTokens {
  accessToken: string;
  refreshToken: string;
  expiresIn: number;
}

interface AuthState {
  user: User | null;
  tokens: AuthTokens | null;
  isAuthenticated: boolean;
  isLoading: boolean;
}
```

### Content Types (`content.ts`)

#### Content Structure
```typescript
interface Content {
  id: string;
  title: string;
  description?: string;
  content: string;
  type: ContentType;
  status: ContentStatus;
  tags: string[];
  metadata: ContentMetadata;
  authorId: string;
  createdAt: string;
  updatedAt: string;
  publishedAt?: string;
}

type ContentType = 'article' | 'blog' | 'social' | 'email' | 'ad' | 'video' | 'image';
type ContentStatus = 'draft' | 'review' | 'approved' | 'published' | 'archived';

interface ContentMetadata {
  seoTitle?: string;
  seoDescription?: string;
  keywords?: string[];
  targetAudience?: string[];
  tone?: string;
  language?: string;
  wordCount?: number;
  readingTime?: number;
}
```

#### Content Operations
```typescript
interface CreateContentData {
  title: string;
  description?: string;
  content: string;
  type: ContentType;
  tags?: string[];
  metadata?: Partial<ContentMetadata>;
}

interface UpdateContentData extends Partial<CreateContentData> {
  status?: ContentStatus;
}

interface ContentFilters {
  type?: ContentType;
  status?: ContentStatus;
  authorId?: string;
  tags?: string[];
  dateRange?: {
    start: string;
    end: string;
  };
  search?: string;
}
```

### AI Agent Types (`agents.ts`)

#### Agent Structure
```typescript
interface Agent {
  id: string;
  name: string;
  type: AgentType;
  description: string;
  capabilities: AgentCapability[];
  status: AgentStatus;
  config: AgentConfig;
  createdAt: string;
  updatedAt: string;
}

type AgentType = 'ideation' | 'writing' | 'editing' | 'optimization' | 'compliance' | 'distribution';
type AgentStatus = 'idle' | 'busy' | 'error' | 'offline';

interface AgentCapability {
  name: string;
  description: string;
  parameters: Record<string, any>;
}

interface AgentConfig {
  model: string;
  temperature: number;
  maxTokens: number;
  systemPrompt: string;
  customSettings?: Record<string, any>;
}
```

#### Workflow Types
```typescript
interface Workflow {
  id: string;
  name: string;
  description: string;
  steps: WorkflowStep[];
  status: WorkflowStatus;
  currentStep: number;
  progress: number;
  createdAt: string;
  updatedAt: string;
}

interface WorkflowStep {
  id: string;
  name: string;
  agentId: string;
  order: number;
  status: StepStatus;
  input: Record<string, any>;
  output?: Record<string, any>;
  error?: string;
}

type WorkflowStatus = 'pending' | 'running' | 'completed' | 'failed' | 'cancelled';
type StepStatus = 'pending' | 'running' | 'completed' | 'failed' | 'skipped';
```

### Marketing Types (`marketing.ts`)

#### Campaign Types
```typescript
interface Campaign {
  id: string;
  name: string;
  description: string;
  type: CampaignType;
  status: CampaignStatus;
  content: Content[];
  channels: CampaignChannel[];
  schedule: CampaignSchedule;
  metrics: CampaignMetrics;
  createdAt: string;
  updatedAt: string;
}

type CampaignType = 'awareness' | 'consideration' | 'conversion' | 'retention';
type CampaignStatus = 'draft' | 'scheduled' | 'active' | 'paused' | 'completed' | 'cancelled';

interface CampaignChannel {
  id: string;
  type: ChannelType;
  name: string;
  config: ChannelConfig;
  status: ChannelStatus;
}

type ChannelType = 'email' | 'social' | 'web' | 'sms' | 'push' | 'ads';
type ChannelStatus = 'active' | 'inactive' | 'error';
```

#### Analytics Types
```typescript
interface CampaignMetrics {
  impressions: number;
  clicks: number;
  conversions: number;
  ctr: number;
  cpc: number;
  cpm: number;
  roi: number;
  revenue: number;
}

interface AnalyticsEvent {
  id: string;
  type: string;
  userId?: string;
  sessionId: string;
  timestamp: string;
  properties: Record<string, any>;
  context: EventContext;
}

interface EventContext {
  page: string;
  referrer?: string;
  userAgent: string;
  ip?: string;
  location?: GeoLocation;
}
```

### UI Types (`ui.ts`)

#### Component Props
```typescript
interface BaseComponentProps {
  className?: string;
  children?: React.ReactNode;
  id?: string;
  'data-testid'?: string;
}

interface ButtonProps extends BaseComponentProps {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost' | 'destructive';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
  loading?: boolean;
  onClick?: () => void;
  type?: 'button' | 'submit' | 'reset';
}

interface InputProps extends BaseComponentProps {
  type?: 'text' | 'email' | 'password' | 'number' | 'tel' | 'url';
  placeholder?: string;
  value?: string;
  onChange?: (value: string) => void;
  error?: string;
  required?: boolean;
  disabled?: boolean;
}
```

#### Form Types
```typescript
interface FormField<T = any> {
  name: string;
  label: string;
  type: 'text' | 'email' | 'password' | 'select' | 'textarea' | 'checkbox' | 'radio';
  value: T;
  error?: string;
  required?: boolean;
  validation?: ValidationRule[];
  options?: SelectOption[];
}

interface ValidationRule {
  type: 'required' | 'minLength' | 'maxLength' | 'pattern' | 'email' | 'custom';
  value?: any;
  message: string;
}

interface SelectOption {
  value: string;
  label: string;
  disabled?: boolean;
}
```

### Common Types (`common.ts`)

#### Utility Types
```typescript
// Generic types
type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;
type Required<T, K extends keyof T> = T & Required<Pick<T, K>>;
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

// Time types
type ISOString = string;
type Timestamp = number;

// ID types
type UUID = string;
type ID = string | number;

// Status types
type LoadingState = 'idle' | 'loading' | 'success' | 'error';
type AsyncState<T> = {
  data: T | null;
  loading: boolean;
  error: string | null;
};
```

#### Pagination Types
```typescript
interface PaginationParams {
  page: number;
  limit: number;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
}

interface PaginationMeta {
  currentPage: number;
  totalPages: number;
  totalItems: number;
  itemsPerPage: number;
  hasNextPage: boolean;
  hasPreviousPage: boolean;
}
```

### WebSocket Types (`websocket.ts`)

#### Message Types
```typescript
interface WebSocketMessage<T = any> {
  type: string;
  payload: T;
  timestamp: string;
  id?: string;
}

interface WebSocketEvent {
  type: 'connect' | 'disconnect' | 'message' | 'error';
  data?: any;
  timestamp: string;
}

// Specific message types
interface ContentUpdateMessage {
  contentId: string;
  updates: Partial<Content>;
  userId: string;
}

interface AgentStatusMessage {
  agentId: string;
  status: AgentStatus;
  progress?: number;
  message?: string;
}
```

## Development Tasks
1. Define base API types and patterns
2. Create authentication type definitions
3. Build content management types
4. Add AI agent type definitions
5. Create marketing and campaign types
6. Implement analytics and metrics types
7. Define UI component types
8. Add common utility types
9. Create WebSocket message types
10. Add comprehensive JSDoc documentation

## Best Practices
- Use strict TypeScript configuration
- Prefer interfaces over types for object shapes
- Use union types for finite sets of values
- Include JSDoc comments for complex types
- Export types from index.ts for easy imports
- Use generic types for reusable patterns
- Validate types at runtime when necessary
- Keep types close to their usage
- Use branded types for type safety
- Implement proper error types
