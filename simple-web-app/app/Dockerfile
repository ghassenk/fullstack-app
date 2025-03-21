FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask flask-cors

# Create a non-root user
RUN useradd -m appuser

# Change ownership of the application files to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]
