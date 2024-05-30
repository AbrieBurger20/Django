FROM python:3.12

# Set the working directory
WORKDIR /mySite

# Install dependencies
COPY requirements.txt /mySite/
RUN pip install -r requirements.txt

# Copy project 
COPY . /mySite/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]