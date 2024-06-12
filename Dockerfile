# Use the official Tensorflow GPU image
FROM tensorflow/tensorflow:latest-gpu

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY real_time.py /app/

RUN apt update
RUN apt install -y libgl1-mesa-glx

# Install required Python packages
RUN pip install tensorflow-probability
RUN pip install imageio[ffmpeg]
RUN pip install ipython
RUN pip install matplotlib
RUN pip install --upgrade keras
RUN pip install tf-keras
RUN pip install tensorflow-docs
RUN pip install opencv-python

# Command to run your script when the container starts
CMD ["python", "real_time.py"]

