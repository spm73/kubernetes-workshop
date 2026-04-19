FROM python:3.12-slim

# Avoid temporal cache files
ENV PYTHONDONTWRITEBYTECODE=1
# Avoid buffering prints
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.10.8 /uv /uvx /bin/

COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev --frozen

COPY main.py .

CMD ["uv", "run", "main.py"]