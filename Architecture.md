# System Architecture

```mermaid
flowchart TD
    A[User] --> B[API]
    B --> C[Backend]
    C --> D[Users Service]
    C --> E[Tasks Service]
    D --> F[(Database)]
    E --> F
