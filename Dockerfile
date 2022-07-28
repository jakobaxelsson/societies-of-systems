# Dockerfile for building web site as part of workflow automation
FROM python

# Make the repository the current working directory. This is automatically mounted by Github actions
WORKDIR /github/workspace

RUN ls

# Install needed Python libraries
RUN pip install -r requirements.txt

# Run the build.py script
ENTRYPOINT ["python build.py"]