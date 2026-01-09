# retinal-information-bottleneck

Investigating the information loss in a rudimentary model of the retina

---

## Motivation

In my first year of undergraduate neuroscience, I learned that the human retina is **not a one-to-one pixel level representation of the visual world.**
In particular, retinal ganglion cells pool information from many photoreceptors, creating a significant information bottleneck before signals ever reach the brain. Also the retinal cone and rod cells fire at different absorbtion levels of a specific wavelength. From cell to cell, however, they might differ slightly which I thought was interesting. A seemingly rigid representation of the visual world being inherantly probabilistic in addtion to being compressed.

This raised a fundamental question for me:

> How much information do we actually lose at the retinal level and how is coherent visual perception still possible?

To answer this question, I built a simplified computational model of the retina using convolutional neural networks (CNNs), focusing on how information is compressed and transformed prior to downstream processing.


## Overall Idea

### This project implements:

- A retina-inspired encoder that mimics spatial pooling and bottlenecking

- A decoder that attempts to reconstruct the original image

- Quantitative measures of information loss vs. reconstruction fidelity

### The goal is not biological realism, but rather:

- To study functional consequences of early visual compression

- To understand how much structure can survive aggressive dimensionality reduction

## Project Overview:

1. RGV values to Wavelengths
2. Compute the Brightness of each pixel
3. Implement Rod cells
4. Implement Cone cells
5. Distributions of rod and cone cells in the retina
6. Investigate different ways to calculate the informatioon of the Retina


## Rabbithole #1: How to convert RGB values to cone and rod cell activations

The goal for this investigation is to convert RGB values and convert them to the activations of LMS (Long, Medium, Short) cone cells in your eye. To understand how to do this, we need to understand where RGB values actually come from. RGB values were concieved to trick our brains into firing cones cells in a way to mimic a speficic firing patterns of the LSM cells of a color. This lso means the many different light spectra can produce the same LMS activations, this is called [Metamerism](https://en.wikipedia.org/wiki/Metamerism_%28color%29). This also means that we can produced ratios of LMS activations that don't get produced in the natural world (some colors dont have a wavelength). 

It some ways the RGB values orginated from our retinal cells. Therefore, there is a way to get the LMS activations from RGB values from a pixel. To do this we need to understand color spaces, in particular the CIE 1931 Color Space.


So to find the given wavelength from a given RGB value, we can calculate the Hue, or what colour it is meant to show then we can convert that colour into a wavelength.

### CIE 1931 Color Space

A color space is a system for consistantly recreating particular color sensations. We do this by understanding the construction of eye.

Our eyes have 3 types of cone cells:

1. Long Cone cells - responsed mostly to red light
2. Medium Cone cells  - responsed mostly to red light
3. Short Cone cells  - responsed mostly to red light

These LMS activations were converted into a XYZ color space, to make it more absolute. The points are picked on the color space to represent RGB and subsequent colors are defined based on this. 

So in order to extract the LMS activations (based on CIE 1931) I need to transfer the RGB values to the color space XYZ coordinates then transfrom them to the LMS values. 

(My old version of this project had used a rudimentary conversion of Hue to wavelength, which I have now deemed as redundant : [Old project](https://github.com/pre6/Creating_Retina_Using_CNN)

References:

[Color Spaces: Explained from the Ground Up - Video Tech Explained](https://www.youtube.com/watch?v=99v96TL-tuY)

[CIE Color Space](https://en.wikipedia.org/wiki/CIE_1931_color_space)

[Colorimetry Fundamentals and Applications](https://www.academia.edu/34154313/Colorimetry_Fundamentals_and_Applications)

[conversion from sRGB to XYZ](https://en.wikipedia.org/wiki/SRGB)

[conversion of XYZ to LMS activations](https://en.wikipedia.org/wiki/LMS_color_space)


[used this code](https://gist.github.com/jcupitt/1aecfab677abfac4bc64efd1b0bcb463)

[also used this code](https://stackoverflow.com/questions/56200998/converting-a-rgb-image-to-lms-and-vice-versa-using-opencv)



