# Dockerfile for building web site as part of workflow automation
FROM python

# Install needed Python libraries
RUN pip install -r /github/workspace/requirements.txt

# Make the repository the current working directory. This is automatically mounted by Github actions
WORKDIR /github/workspace

# Run the build.py script
ENTRYPOINT ["python build.py"]