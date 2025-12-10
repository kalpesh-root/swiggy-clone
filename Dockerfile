# ------------ Stage 1: Build Dependencies ------------
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-cache-dir -r requirements.txt


# ------------ Stage 2: Final Runtime Image ------------
FROM python:3.10-slim

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy app code
COPY . .

# Set permissions so appuser can access files
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "swiggy_clone:app"]

