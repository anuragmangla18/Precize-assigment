#Build the Docker image
docker build -t huggingface-report-generator .
#Run the Docker container
docker run --rm huggingface-report-generator
