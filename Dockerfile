# Dockerfile for building web site as part of workflow automation
FROM python

# Install needed Python libraries
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

# Make the repository the current working directory. This is automatically mounted by Github actions
WORKDIR /github/workspace

# Run the build.py script
ENTRYPOINT ["python build.py"]