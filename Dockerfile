# Stage 1: Build dependencies & plugins
FROM node:22-slim AS builder

# Install git to install community plugins
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Copy dependency manifests and setup scripts
COPY package.json package-lock.json* .npmrc* ./
COPY scripts/ ./scripts/
COPY quartz/ ./quartz/
COPY quartz.config.yaml quartz.config.default.yaml* ./

# Install npm dependencies and Quartz plugins
RUN npm install
RUN npx quartz plugin install

# Stage 2: Runtime image
FROM node:22-slim

# Install git in runtime for git history & file modification timestamps
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Copy installed dependencies and plugins from builder
COPY --from=builder /usr/src/app/ /usr/src/app/

# Copy all source files and markdown content
COPY . .

# Ensure entrypoint is executable
RUN chmod +x /usr/src/app/docker-entrypoint.sh

ENV NODE_ENV=production
ENV PORT=8080
ENV WS_PORT=3001

EXPOSE 8080 3001

ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]
CMD ["serve"]
