#!/bin/bash

# Development script for AI Multi-Agent Content Creation & Marketing System
# This script starts both frontend and backend in development mode

set -e

echo "🚀 Starting AI Multi-Agent Content Creation & Marketing System Development Environment"
echo "=================================================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if required tools are installed
check_requirements() {
    print_status "Checking system requirements..."
    
    # Check Node.js
    if ! command -v node &> /dev/null; then
        print_error "Node.js is not installed. Please install Node.js 18+"
        exit 1
    fi
    
    # Check npm
    if ! command -v npm &> /dev/null; then
        print_error "npm is not installed. Please install npm"
        exit 1
    fi
    
    # Check Python
    if ! command -v python3 &> /dev/null; then
        print_error "Python 3 is not installed. Please install Python 3.9+"
        exit 1
    fi
    
    # Check if PostgreSQL is running (optional check)
    if command -v pg_isready &> /dev/null; then
        if ! pg_isready -q; then
            print_warning "PostgreSQL might not be running. Please ensure PostgreSQL is started."
        fi
    fi
    
    # Check if Redis is running (optional check)
    if command -v redis-cli &> /dev/null; then
        if ! redis-cli ping &> /dev/null; then
            print_warning "Redis might not be running. Please ensure Redis is started."
        fi
    fi
    
    print_success "System requirements check completed"
}

# Setup frontend
setup_frontend() {
    print_status "Setting up frontend..."
    
    cd frontend
    
    # Check if node_modules exists
    if [ ! -d "node_modules" ]; then
        print_status "Installing frontend dependencies..."
        npm install
    fi
    
    # Check if .env.local exists
    if [ ! -f ".env.local" ]; then
        print_status "Creating frontend environment file..."
        cp env.example .env.local
        print_warning "Please edit frontend/.env.local with your configuration"
    fi
    
    cd ..
    print_success "Frontend setup completed"
}

# Setup backend
setup_backend() {
    print_status "Setting up backend..."
    
    cd backend
    
    # Check if virtual environment exists
    if [ ! -d "venv" ]; then
        print_status "Creating Python virtual environment..."
        python3 -m venv venv
    fi
    
    # Activate virtual environment
    print_status "Activating virtual environment..."
    source venv/bin/activate
    
    # Install dependencies
    print_status "Installing backend dependencies..."
    pip install -r requirements.txt
    
    # Check if .env exists
    if [ ! -f ".env" ]; then
        print_status "Creating backend environment file..."
        cp env.example .env
        print_warning "Please edit backend/.env with your configuration"
    fi
    
    cd ..
    print_success "Backend setup completed"
}

# Start backend server
start_backend() {
    print_status "Starting backend server..."
    
    cd backend
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Start the server
    print_status "Starting FastAPI server on http://localhost:8000"
    uvicorn main:app --reload --host 0.0.0.0 --port 8000 &
    
    BACKEND_PID=$!
    echo $BACKEND_PID > .backend.pid
    
    cd ..
    print_success "Backend server started (PID: $BACKEND_PID)"
}

# Start frontend server
start_frontend() {
    print_status "Starting frontend server..."
    
    cd frontend
    
    # Start the development server
    print_status "Starting Next.js development server on http://localhost:3000"
    npm run dev &
    
    FRONTEND_PID=$!
    echo $FRONTEND_PID > .frontend.pid
    
    cd ..
    print_success "Frontend server started (PID: $FRONTEND_PID)"
}

# Cleanup function
cleanup() {
    print_status "Shutting down development servers..."
    
    # Kill backend process
    if [ -f "backend/.backend.pid" ]; then
        BACKEND_PID=$(cat backend/.backend.pid)
        if kill -0 $BACKEND_PID 2>/dev/null; then
            kill $BACKEND_PID
            print_status "Backend server stopped"
        fi
        rm backend/.backend.pid
    fi
    
    # Kill frontend process
    if [ -f "frontend/.frontend.pid" ]; then
        FRONTEND_PID=$(cat frontend/.frontend.pid)
        if kill -0 $FRONTEND_PID 2>/dev/null; then
            kill $FRONTEND_PID
            print_status "Frontend server stopped"
        fi
        rm frontend/.frontend.pid
    fi
    
    print_success "Development environment shutdown complete"
}

# Main execution
main() {
    # Set up signal handlers for cleanup
    trap cleanup EXIT INT TERM
    
    # Check requirements
    check_requirements
    
    # Setup both frontend and backend
    setup_frontend
    setup_backend
    
    # Start servers
    start_backend
    sleep 2  # Give backend time to start
    start_frontend
    
    print_success "Development environment is ready!"
    echo ""
    echo "🌐 Frontend: http://localhost:3000"
    echo "🔧 Backend API: http://localhost:8000"
    echo "📚 API Documentation: http://localhost:8000/docs"
    echo "💚 Health Check: http://localhost:8000/health"
    echo ""
    echo "Press Ctrl+C to stop all servers"
    echo ""
    
    # Wait for user interrupt
    wait
}

# Run main function
main
