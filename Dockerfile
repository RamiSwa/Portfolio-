# ✅ Use a lightweight Python image
FROM python:3.10-slim

# ✅ Set the working directory
WORKDIR /app

# ✅ Install system dependencies in a single step
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ✅ Copy and install dependencies first (optimized caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy the project files (excluding .git, .env, and other unnecessary files)
COPY . .

# ✅ Expose the port for Django
EXPOSE 8000

# ✅ Run migrations, collect static files, and start the server
CMD ["bash", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:${PORT:-8000} config.wsgi:application"]
