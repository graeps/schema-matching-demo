# develop stage
FROM node:20-alpine3.20 AS develop-stage
# set the working directory
WORKDIR /app
# Copy the working directory in the container
COPY package*.json ./
# Install the project dependencies
RUN npm install -g @quasar/cli
# Copy the rest of the project files to the container
COPY . .

#build stage
FROM develop-stage AS build-stage
RUN npm install
RUN quasar build


#production stage
# Use Nginx image from the previous stage for the nginx container
FROM nginx:stable-alpine AS production-stage
# Copy the build application from the previous stage to the Nginx container
COPY --from=build-stage /app/dist/spa /usr/share/nginx/html
# Copy the nginx configuration file
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

# Start Nginx to serve the application
CMD ["nginx", "-g", "daemon off;"]
