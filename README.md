# HotC
Card scanner and value evaluator, saves card to collection.

# Step-by-Step Work Tickets

## Phase 1: Backend Development

### 1. Set Up Backend Repository
- [x] Create a GitHub repository for the backend.
- [x] Initialize with:
  - [x] A `README.md`
  - [x] A `.gitignore` file for Python
  - [x] A basic folder structure (`/app`, `/tests`, etc.)
  - [x] A `requirements.txt` file for dependencies.

### 2. Initialize Flask/FastAPI Backend
- [x] Create a basic Flask/FastAPI app with a single test route (e.g., `/health` for health checks).
- [x] Set up configuration for development and production environments.

### 3. Set Up Docker for Backend
- [x] Write a `Dockerfile` for the Flask/FastAPI app.
- [x] Test the container locally to ensure it runs without errors.

### 4. Set Up PostgreSQL with Docker Compose
- [ ] Add a PostgreSQL service in `docker-compose.yml`.
- [ ] Configure the backend to connect to the PostgreSQL container.

### 5. Develop Image Processing Functionality
- [ ] Implement the OCR script using OpenCV and pytesseract.
- [ ] Test the script locally with sample Yu-Gi-Oh! card images.

### 6. Create API Endpoints
- [ ] `POST /upload`: Accept image uploads and return OCR results.
- [ ] `GET /card/{id}`: Retrieve card details from the database.

### 7. Add Unit Tests for Backend
- [ ] Write tests for the image processing function.
- [ ] Test the `/upload` and `/card/{id}` endpoints.
- [ ] Mock pytesseract for controlled testing.

---

## Phase 2: Mobile App Development

### 1. Set Up Mobile Repository
- [ ] Create a GitHub repository for the mobile app.
- [ ] Initialize with Flutter (or React Native) boilerplate.

### 2. Build Basic UI
- [ ] Implement a simple home screen with an image upload button.
- [ ] Create a results page to display OCR data from the backend.

### 3. Integrate API Calls
- [ ] Connect the mobile app to the `/upload` API.
- [ ] Display returned OCR results in the UI.

### 4. Add Unit Tests for Mobile App
- [ ] Test the image upload functionality.
- [ ] Mock API responses for the results display feature.

---

## Phase 3: Authentication

### 1. Implement JWT Authentication in Backend
- [ ] Add user registration and login endpoints (`POST /register`, `POST /login`).
- [ ] Secure the `/upload` and `/card/{id}` routes with JWT.

### 2. Add Authentication to Mobile App
- [ ] Implement login/signup pages.
- [ ] Store and send JWT tokens with API requests.

### 3. Test Authentication
- [ ] Write backend tests for token generation and validation.
- [ ] Test protected routes with valid/invalid tokens.

---

## Phase 4: Containerization and Testing

### 1. Finalize Dockerization
- [ ] Optimize the `Dockerfile` for production (e.g., multi-stage builds).
- [ ] Ensure `docker-compose.yml` includes all services (backend, database, real-time server if applicable).

### 2. Integration Testing with Docker
- [ ] Simulate the entire stack locally with Docker Compose.
- [ ] Test end-to-end flows (image upload, OCR processing, and card retrieval).

### 3. Set Up CI/CD Pipeline
- [ ] Configure GitHub Actions for automated builds and tests.
- [ ] Add Docker build and push steps for containerized services.

---

## Phase 5: Deployment

### 1. Deploy Backend
- [ ] Deploy the Dockerized backend to AWS, Google Cloud, or Heroku.
- [ ] Set up managed PostgreSQL services (RDS, Cloud SQL, etc.).

### 2. Deploy Mobile App
- [ ] Build and publish the mobile app to app stores (Google Play, Apple App Store).
- [ ] Test production backend integration.

### 3. Monitor and Optimize
- [ ] Set up logging and monitoring for the backend (e.g., AWS CloudWatch, Sentry).
- [ ] Collect user feedback and refine features.

---

## Stretch Goals
- [ ] **Real-Time Features**: Implement Firebase or Socket.IO for live updates (e.g., multiplayer card games).
- [ ] **Enhanced Features**: Add user profiles, a card library, or advanced search functionality.
