# Image_Warping
Warping an image to a bird view.

Using Pithagora's theorem to get hight and width of the object. That would, of course, not be the right height and width because this is a classical **projective reconstruction** where we do not have such information and we have a **distorsion.**

In order to obtain a reconstruction of the model in which objects have their correct (Euclidean - real world) shape, it is necessary to determine the calibration of the cameras.

Added lines to follow selecting the dots, to you know what kind of the rectangle (or other shape) you are making.

# Example

### Original Image

![original](./images/book_1.jpg)

### Warped Image

![warped_image](./images/warped_book_1.jpg)
