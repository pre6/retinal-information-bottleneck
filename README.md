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


## Rabbithole #1: What even are RGB values and why does the question of converting them to wavelength kind of not make any sense


Images on a computer have pixel level representations in order to present them on a screen. Each pixel has three values associated with it. Red, Green Blue levels. $(R,G,B)$

Where:

| RGB Value         | Color Description |
|-------------------|-------------------|
| $(255, 0, 0)$       | Pure Red          |
| $(0, 255, 0)$       | Pure Green        |
| $(0, 0, 255)$       | Pure Blue         |
| $(255, 255, 255)$   | White             |
| $(0, 0, 0)$         | Black             |
| $(128, 128, 128)$   | Gray              |


Reading the wiki page on the history of [RGB color model](https://en.wikipedia.org/wiki/RGB_color_model#History_of_RGB_color_model_theory_and_usage) I realize that this model was made before they knew that there were only three types of cone cells in the eye. I thought this was interesting.

In order to make my model, I might convert the RGB values into a wavelength. Wavelengths in the visual spectrum are electromagnetic waves that are visible to the human eye. In particular, these wavelengths are absorbed by a corresponding cone or rod cell and interact with a protein called Opsin which then causes a casade of other proteins. This process is called phototransduction.

So we need to convert them from one to the other. But we are unable to make a perfect conversion because of the idea of [Metamerism](https://en.wikipedia.org/wiki/Metamerism_%28color%29)

<img width="500" height="750" alt="image" src="https://github.com/user-attachments/assets/a1c738d1-34da-4e2b-b3e8-1dde5629bdd4" />

The idea of Metamerism is that two images with seemingly the same colour could have two different wavelengths. In the first column, we see that the wavelength from the yellow ball is only yellow, while the second ball is a mixed of three different wavelengths. This idicates that there could be a numerous amount of combinations that give rise to the same colour. For the purposes of this project this does not matter. But it is really interesting to think about how if we have a "yellow" wavelength, the wavelength hits the R,B,B cones in a specfic ratio, meaning if we have the same ratio of red green and blue we can artificially make yellow which is how the monitor you are reading this very project on works!! (Maybe this could be a way to test our retina or something tbd)

