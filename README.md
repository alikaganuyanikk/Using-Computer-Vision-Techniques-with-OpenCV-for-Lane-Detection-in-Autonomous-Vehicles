# Using-Computer-Vision-Techniques-with-OpenCV-for-Lane-Detection-in-Autonomous-Vehicles

The purpose of this project is to develop a program that can identify lane markings in images or videos. While humans can use their eyes to determine the location of lane lines while driving, our vehicles lack this type of visual perception capability.

This is where computer vision comes into play, helping computers "see" through complex algorithms. By leveraging computer vision techniques with OpenCV, we can enable autonomous vehicles to detect lane markings effectively.

### Grayscale Conversion

**Grayscale Conversion**

The purpose of edge detection is to identify the boundaries of objects within images. Essentially, I will use edge detection to find areas of sharpness in an image.

### Why Convert an Image to Grayscale?

Images are composed of pixels. A three-channel color image contains red, green, and blue channels. In a grayscale image, each pixel has only one channel and only one intensity value. The absence of color information means less data usage and simpler processing procedures.
<div align="center">
  <img src="images/Resim21.png" alt="Example of Grayscale Conversion and Edge Detection">
  <p><em>Grayscale applied image</em></p>
</div>

### Gaussian Blur

Image noise can create false edges and ultimately affect edge detection. We need to reduce the noise and smooth our image while detecting edges.
<div align="center">
  <img src="images/Resim22.png" alt="Example of Gaussian Blur">
  <p><em>Gaussian Blur applied image</em></p>
</div>

### Canny Edge Detection

I will use this method to identify edges in the image. An edge corresponds to a region in the image where there is a sharp change in intensity. The Canny function will perform the derivative of our function in both the X and Y directions, measuring the change in intensity relative to neighboring pixels. A small derivative indicates a small change in intensity, while a large derivative indicates a significant change. If the gradient exceeds the upper threshold, it is considered an edge pixel. If it is below the lower threshold, it is rejected.
<div align="center">
  <img src="images/Resim23.png" alt="Canny Edge Detection">
  <p><em>Canny applied image</em></p>
</div>
