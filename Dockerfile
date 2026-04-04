FROM python:3.12.3

#  working directory
WORKDIR /usr/src/app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask gunicorn
# Expose  port
EXPOSE 8000
# EXPOSE 5000

# Run the application
CMD ["gunicorn", "-w" , "4", "-b", "0.0.0.0:8000", "run:app"]
# cmd ["python","run.py"]