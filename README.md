# KBKO Mad Skillz

> **Integrated Platform Combining Analytics, Automation, and AI-Driven Planning**

An enterprise-grade system that seamlessly integrates data analytics, process automation, and intelligent planning with AI agents to enable data-driven decision making.

## 🎯 Overview

KBKO Mad Skillz is a modular, scalable platform designed to:

- **Analyze** complex data with advanced analytics (Blackbird)
- **Automate** workflows and schedule tasks intelligently (Smokey)
- **Plan** operations and simulate scenarios with AI (Seymour Shadows)
- **Manage** core infrastructure and authentication (KBKO Core)

## 📦 Project Structure

```
KBKO-mad-skillz/
├── kbko_core/           # Core infrastructure & utilities
│   ├── config/          # Configuration management
│   ├── database/        # Database layer & ORM
│   ├── auth/            # Authentication & authorization
│   └── logging/         # Centralized logging
├── blackbird/           # Analytics & visualization
│   ├── analytics/       # Data analysis engines
│   ├── visualization/   # Data visualization tools
│   └── mapping/         # Data mapping & transformation
├── smokey/              # Automation & scheduling
│   ├── automation/      # Workflow automation
│   ├── scheduler/       # Task scheduling
│   └── ai_agents/       # AI-powered agents
├── seymour_shadows/     # Planning & simulation
│   ├── planner/         # Planning engine
│   ├── simulations/     # Scenario simulations
│   ├── knowledge/       # Knowledge management
│   └── dashboard/       # Analytics dashboard
├── tests/               # Test suite
└── docs/                # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip or conda
- PostgreSQL (recommended) or SQLite

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/babyboyKBKO369-ctrl/KBKO-mad-skillz.git
cd KBKO-mad-skillz
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
cp .env.example .env
# Edit .env with your configuration
```

5. **Run tests**
```bash
pytest
```

## 📚 Modules

### KBKO Core
Core infrastructure providing shared utilities, configuration management, database access, authentication, and logging for all modules.

**Key Features:**
- Configuration management system
- Database ORM layer
- Authentication & authorization
- Structured logging

### Blackbird (Analytics)
Advanced analytics and visualization engine for processing and visualizing complex datasets.

**Key Features:**
- Data analysis pipelines
- Real-time analytics
- Interactive visualizations
- Data transformation & mapping

### Smokey (Automation)
Intelligent workflow automation and task scheduling with AI agent integration.

**Key Features:**
- Workflow automation
- Task scheduling
- Event-driven automation
- AI agent orchestration

### Seymour Shadows (Planning)
Intelligent planning engine with scenario simulation and AI-powered decision support.

**Key Features:**
- Strategic planning
- Scenario simulation
- Knowledge management
- Interactive dashboards

## 🔧 Configuration

Create a `.env` file in the project root:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost/kbko
# or for SQLite:
# DATABASE_URL=sqlite:///./kbko.db

# API
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=True

# Authentication
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json

# AI Services
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
```

## 🧪 Testing

Run the complete test suite:

```bash
pytest                          # Run all tests
pytest --cov                    # With coverage report
pytest tests/unit/              # Run only unit tests
pytest tests/integration/       # Run only integration tests
pytest -v                       # Verbose output
pytest -k "test_pattern"        # Run specific tests
```

## 📖 Documentation

- [Architecture Guide](docs/architecture.md) - System design and component relationships
- [API Documentation](docs/api.md) - REST API reference
- [Roadmap](docs/roadmap.md) - Project timeline and planned features

## 🛠️ Development

### Code Style

We use Black, isort, and flake8 for code quality:

```bash
# Format code
black .

# Sort imports
isort .

# Check linting
flake8 .

# Type checking
mypy .
```

### Pre-commit Hooks

Install pre-commit hooks:

```bash
pre-commit install
```

### Running Locally

```bash
# Start the API server
uvicorn kbko_core.main:app --reload

# Run a specific module
python -m smokey.scheduler

# Run with custom config
python -m seymour_shadows.dashboard --config config/custom.yaml
```

## 🚢 Deployment

### Docker

Build and run with Docker:

```bash
docker build -t kbko-mad-skillz:latest .
docker run -p 8000:8000 kbko-mad-skillz:latest
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/babyboyKBKO369-ctrl/KBKO-mad-skillz/issues)
- **Discussions**: [GitHub Discussions](https://github.com/babyboyKBKO369-ctrl/KBKO-mad-skillz/discussions)

---

**Built with ❤️ by the KBKO Team**
