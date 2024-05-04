# Use an official Node.js base image
FROM node:14-alpine as builder

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install dependencies using npm ci for a clean install
RUN npm ci

# Copy the application's source code to the container
COPY . .

# Build the application
RUN npm run build

# Start a new stage from a smaller base image to reduce final image size
FROM node:14-alpine

# Set the working directory in the new image context
WORKDIR /app

# Copy runtime dependencies from the builder stage
COPY --from=builder /app/package*.json ./
RUN npm ci --only=production

# Copy the build output from the builder stage
COPY --from=builder /app/dist ./dist

# Expose the port the app runs on
EXPOSE ${LOCAL_DEV_PORT}

# Add metadata to the image to describe which port the container is listening on at runtime
LABEL maintainer="Your Name <youremail@example.com>"
LABEL version="1.0"
LABEL description="Sample Node.js application"

# Set the command to start the app using npm start
# Using environment variable from .env file to set runtime command
CMD [ "npm", "start" ]
