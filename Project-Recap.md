
# Recap: Deploying a Web Application with Nginx, Flask, and MySQL in Kubernetes

## 1. Initial Setup and Environment Preparation

- **Environment**: Kubernetes environment set up using Minikube running on WSL (Windows Subsystem for Linux) with an OpenSUSE distribution.
- **Components to Deploy**:
  - **Nginx**: Serves static content (HTML) and proxies API requests to the backend.
  - **Flask**: Python web framework acting as the backend server to handle API requests and interact with the database.
  - **MySQL**: Relational database to store user data and preferences.

## 2. Building and Preparing Docker Images

- **Flask Docker Image**: Built a Docker image for the Flask application using a `Dockerfile` specifying a Python base image and necessary dependencies (`Flask`, `mysql-connector-python`).
- **Minikube Docker Environment**: Ensured to build the Docker image within Minikube’s Docker environment:
  ```bash
  eval $(minikube -p minikube docker-env)
  docker build -t flask-app:latest .
  ```

## 3. Deploying MySQL in Kubernetes

- **MySQL Deployment and Service**:
  - Created a Kubernetes deployment and service for MySQL, defining a persistent volume to store data.
  - Configured the MySQL root user with a password and ensured Flask app connectivity.

## 4. Deploying Flask Application in Kubernetes

- **Flask Deployment and Service**:
  - Configured a deployment YAML file (`flask-deployment.yaml`) for Flask with environment variables for `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, and `MYSQL_DATABASE`.
  - Set up Flask as a `ClusterIP` service for internal communication with Nginx.

## 5. Configuring Nginx to Serve Static Content and Proxy API Requests

- **Nginx Configuration (`nginx.conf`)**:
  - Configured Nginx to serve `index.html` and proxy `/api/` requests to Flask at `http://flask-service:5000/`.
  - Defined Kubernetes ConfigMaps for `nginx.conf` and `index.html` to dynamically mount these into the Nginx container.

- **Nginx Deployment and Service**:
  - Created a deployment YAML file (`nginx-deployment.yaml`) for Nginx with volume mounts for ConfigMaps.
  - Configured Nginx as a `NodePort` service to expose it externally via Minikube.

## 6. Applying Configurations and Verifying Deployment

- **Applying Kubernetes Manifests**:
  - Applied configurations using `kubectl apply -f <file-name>.yaml` for MySQL, Flask, and Nginx.
  - Monitored pod status with `kubectl get pods`.

- **Verifying Connectivity**:
  - Verified that Nginx served the static page and proxied requests to Flask.
  - Ensured Flask correctly connected to MySQL and returned user data as JSON.

## 7. Troubleshooting Common Issues

- **Image Pull Issues**: Resolved `ErrImagePull` by building Docker images in Minikube’s Docker environment.
- **MySQL Access Denied**: Fixed MySQL access issues by correcting credentials and updating Flask environment variables.
- **Configuration Errors**: Ensured correct Nginx configuration and proper ConfigMap mounts.
- **Application Errors**: Used logs (`kubectl logs -l app=<app-name>`) to troubleshoot API and connectivity problems.

## 8. Final Verification and Successful Deployment

- **Testing the Web Application**:
  - Accessed the web application via Minikube service URL, displaying user data and preferences fetched from Flask API.
  - Confirmed Nginx served static content and acted as a reverse proxy for Flask.

## 9. Enhancements and Next Steps

- **Optimize for Production**: Use a production-grade WSGI server (e.g., Gunicorn) and secure with HTTPS.
- **Scale the Application**: Implement Kubernetes Horizontal Pod Autoscaling (HPA).
- **Deploy to Cloud**: Migrate to managed Kubernetes services (e.g., AWS EKS, GKE, Azure AKS).
- **Improve Monitoring and Logging**: Use tools like Prometheus and Grafana for performance monitoring.

## Conclusion

Successfully set up a Kubernetes environment with Minikube to deploy a web application using Nginx, Flask, and MySQL. You navigated through setup challenges, applied best practices, and resolved common issues related to connectivity and permissions.

Fantastic work! 🚀 If you have any more questions or want to explore further enhancements, feel free to ask!
