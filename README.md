# General

The toughts to solve this Puzzle were based on the info given in the file **TaskDescriptionDepthCamera.pdf**

As the images given were Color Images with 3 bands, I took the freedom to make my life easier and convert them to grayscale PNG images, some of them i inverted back as the volume was being given negative...

About **Ratio**, I did not really understand what was being expected. Was it supposed to be like which objects are bigger than the others??? We don't really know the real sizes here as we don't know if we are talking about meters, millimeters, etc...

As a plus the script does output 3D images based on the depth images given. See the .ply files

## Development

I used Python 3.8.2

The actual tool/technolgy stack is:

- [Python3](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [pyrgbd](https://github.com/unclearness/pyrgbd)

## Configuring & Running

First of all you will need to install Python3.

Second, you will need to install some libraries:

<code> pip3 install numpy </code>

<code> pip3 install opencv-python </code>

Besides that as we are using a non-released library you do have to copy the **pyrgbd** folder into your Python site-packages folder. To know where your site-packages folder is, execute the following command:

<code> python3 -m site --user-site </code>

Third, executing it:

<code> python3 script.py </code>
