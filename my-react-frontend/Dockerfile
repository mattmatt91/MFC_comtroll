# Use an official Node runtime as a parent image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install any needed packages specified in package.json
RUN npm install

# Bundle app source
COPY public public
COPY src src
COPY *.js* ./

# Build the app
RUN npm run build

# Expose the port your app will run on
EXPOSE 3000

# Command to start your React app
CMD ["npm", "start"]