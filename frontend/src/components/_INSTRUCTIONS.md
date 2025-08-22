# Components Folder Instructions

This folder contains all React components for the AI Multi-Agent Content Creation & Marketing System frontend.

## 📁 Folder Structure

```
components/
├── ui/                    # Base UI components (Button, Card, Input, etc.)
├── layout/               # Layout components (Header, Sidebar, Footer)
├── forms/                # Form components and validation
├── providers/            # Context providers (Theme, Auth, etc.)
└── features/            # Feature-specific components
```

## 🎯 Component Guidelines

### Naming Conventions
- Use PascalCase for component names
- Use descriptive, semantic names
- Include component type in name (e.g., `UserProfile`, `ContentCard`)

### File Structure
```typescript
// ComponentName.tsx
import React from 'react'
import { ComponentProps } from './ComponentName.types'

export interface ComponentProps {
  // Props interface
}

export function ComponentName({ prop1, prop2 }: ComponentProps) {
  return (
    // JSX
  )
}
```

### Styling Guidelines
- Use Tailwind CSS classes
- Follow the design system in `tailwind.config.js`
- Use CSS custom properties for theming
- Ensure responsive design
- Maintain accessibility standards

### Props and Types
- Define TypeScript interfaces for all props
- Use proper typing for event handlers
- Include JSDoc comments for complex components
- Export types from separate `.types.ts` files

### State Management
- Use React hooks for local state
- Use Zustand for global state
- Keep components focused and single-purpose
- Avoid prop drilling

## 🔧 Implementation Tasks

### UI Components (ui/)
- [ ] Button variants and states
- [ ] Form inputs (Text, Email, Password, etc.)
- [ ] Modal and Dialog components
- [ ] Loading and Error states
- [ ] Toast notifications
- [ ] Data table components
- [ ] Chart and visualization components

### Layout Components (layout/)
- [ ] Main navigation header
- [ ] Sidebar navigation
- [ ] Footer component
- [ ] Page layout wrapper
- [ ] Responsive navigation menu
- [ ] Breadcrumb navigation

### Form Components (forms/)
- [ ] Form validation hooks
- [ ] Input field components
- [ ] Form submission handling
- [ ] Error message display
- [ ] Form field groups
- [ ] File upload components

### Feature Components (features/)
- [ ] Content editor
- [ ] AI agent status display
- [ ] Analytics dashboard widgets
- [ ] Marketing campaign components
- [ ] User management components
- [ ] Settings and configuration components

## 🎨 Design System Integration

### Colors
- Primary: Blue (#0ea5e9)
- Secondary: Purple (#d946ef)
- Accent: Yellow (#eab308)
- Neutral: Gray scale

### Typography
- Font family: Inter
- Headings: Bold weights
- Body: Regular weight
- Code: JetBrains Mono

### Spacing
- Use Tailwind spacing scale
- Consistent padding and margins
- Responsive spacing

### Components
- Follow atomic design principles
- Build from atoms to organisms
- Maintain consistency across the app

## 🧪 Testing Requirements

- Unit tests for all components
- Integration tests for complex components
- Accessibility testing
- Visual regression testing
- Cross-browser compatibility

## 📝 Documentation

- Include JSDoc comments
- Create Storybook stories
- Document component usage examples
- Maintain component API documentation

## 🔄 State Management

### Local State
- Use `useState` for simple state
- Use `useReducer` for complex state logic
- Use `useCallback` and `useMemo` for optimization

### Global State
- Use Zustand for global state
- Create stores for different domains
- Keep state normalized

### Server State
- Use React Query for server state
- Implement proper loading states
- Handle error states gracefully

## 🚀 Performance

- Implement React.memo for expensive components
- Use lazy loading for large components
- Optimize bundle size
- Implement proper code splitting

## 🔒 Security

- Sanitize user inputs
- Validate props and data
- Implement proper error boundaries
- Follow security best practices

## 📱 Responsive Design

- Mobile-first approach
- Breakpoint consistency
- Touch-friendly interactions
- Accessible on all devices

This folder is the foundation of the user interface. All components should be built with reusability, maintainability, and performance in mind.
