<think>
Okay, let's start by understanding the user's request. They need a tech-spec.md for a payment orchestrator product. The product is a transaction monitoring and payment issue resolution platform for financial institutions. The key here is to outline the technical specifications in a clear and structured way.

First, the stack. Since it's a financial service, reliability and scalability are crucial. I'll go with Go for the backend because it's efficient and good for high-performance systems. For the frontend, React is a solid choice for a responsive UI. PostgreSQL with TimescaleDB extension makes sense for time-series data from transactions. Redis for caching and Kafka for real-time event streaming would handle the data flow efficiently.

Hosting should be free-tier-first. Using AWS is a good bet because they offer free tiers for EC2, RDS, and S3. Docker and Kubernetes will help with containerization and orchestration. GitHub Actions for CI/CD is free and integrates well with GitHub repos.

Data model needs tables for transactions, issues, clients, and resolution logs. Each table should have essential fields like IDs, timestamps, statuses, and foreign keys. For example, the transactions table will track each payment, while the issues table will log problems with their status and resolution steps.

API surface should cover the main functionalities: creating transactions, monitoring, reporting issues, resolving them, and generating reports. RESTful endpoints with methods like POST, GET, PUT, and DELETE will handle these actions. Each endpoint's purpose needs to be clear, like /transactions for creating and listing transactions.

Security is critical for financial apps. OAuth 2.0 with JWT for authentication, AWS IAM for role-based access, and AWS Secrets Manager for managing credentials. HTTPS with Let's Encrypt for encryption in transit. Data at rest should be encrypted using AWS KMS.

Observability includes logging with AWS CloudWatch, metrics with Prometheus and Grafana for dashboards, and distributed tracing with AWS X-Ray. These tools help monitor performance and troubleshoot issues.

Build/CI with GitHub Actions for automated testing and deployment. Docker images pushed to ECR, Kubernetes deployments via Helm charts. Monitoring alerts set up in CloudWatch and Prometheus to ensure the system is reliable.

I need to make sure each section is specific and includes numerical data where possible, like using PostgreSQL 15 and Go 1.21. Also, mention the exact platforms and services to keep it actionable. Avoid any fluff, just the necessary details for the tech team to implement.
</think>

```markdown
# Tech Spec: Payment Orchestrator v1

## Stack
- **Language**: Go 1.21 (backend), TypeScript 5.3 (frontend)
- **Frameworks**: Gin-Gonic (HTTP), React 18 (UI), PostgreSQL 15 (DB), TimescaleDB 2.15 (time-series extension)
- **Runtime**: Docker 24.0, Kubernetes 1.28 (orchestration)

## Hosting
- **Free-tier-first**: AWS EC2 t4g.nano (backend), RDS PostgreSQL (free tier), S3 (storage)
- **Platforms**: GitHub Actions (CI/CD), AWS ECR (container registry), CloudFront (CDN)

## Data Model
1. **Transactions**
   - `id` (UUID), `client_id` (UUID), `amount` (numeric), `status` (enum: pending, success, failed), `timestamp` (timestamptz)
2. **Issues**
   - `id` (UUID), `transaction_id` (UUID), `type` (enum: fraud, duplicate, timeout), `resolved_at` (timestamptz), `resolution_steps` (JSONB)
3. **Clients**
   - `id` (UUID), `name` (string), `api_key` (string), `notification_webhook` (URL)
4. **ResolutionLogs**
   - `id` (UUID), `issue_id` (UUID), `action` (string), `performed_by` (string), `timestamp` (timestamptz)

## API Surface
1. `POST /transactions` – Create transaction
2. `GET /transactions` – List transactions (filter by status)
3. `POST /issues` – Report transaction issue
4. `PUT /issues/{id}/resolve` – Resolve issue
5. `GET /clients` – List clients
6. `POST /clients` – Register client
7. `GET /reports` – Generate compliance report (CSV)
8. `GET /health` – System health check

## Security Model
- **Auth**: OAuth 2.0 with JWT (signed by AWS KMS)
- **Secrets**: AWS Secrets Manager (API keys, DB credentials)
- **IAM**: AWS IAM roles for Kubernetes pods (least-privilege)
- **Encryption**: HTTPS (Let's Encrypt), AES-256 at rest (AWS KMS)

## Observability
- **Logs**: AWS CloudWatch (structured JSON logs)
- **Metrics**: Prometheus (exposed via `/metrics` endpoint)
- **Traces**: AWS X-Ray (distributed tracing for transaction flows)
- **Alerts**: Grafana dashboards (error rates > 1%, latency > 500ms)

## Build/CI
- **CI**: GitHub Actions (unit tests, static analysis, Docker build)
- **CD**: Helm chart deployment to EKS (blue/green rollout)
- **Testing**: 80%+ coverage (Go unit tests), Chaos Engineering (K6 for fault injection)
- **Build Time**: < 3 minutes (cached dependencies)
```