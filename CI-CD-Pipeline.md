# CI/CD Pipeline

## Pipeline Steps

1. Developer pushes code to GitHub.
2. CI/CD Pipeline starts.
3. Install project dependencies.
4. Run automated tests.
5. Build Docker Image.
6. Deploy the application.

## Pipeline Flow

```mermaid
flowchart TD
    A[Push Code] --> B[Install Dependencies]
    B --> C[Run Tests]
    C --> D{Tests Passed?}
    D -->|Yes| E[Build Docker Image]
    D -->|No| F[Stop Pipeline]
    E --> G[Deploy Application]
