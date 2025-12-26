# retinal-information-bottleneck

Investigating the information loss in a rudimentary model of the retina

---

## Motivation

In my first year of undergraduate neuroscience, I learned that the human retina is **not a one-to-one pixel level representation of the visual world.**
In particular, retinal ganglion cells pool information from many photoreceptors, creating a significant information bottleneck before signals ever reach the brain.

This raised a fundamental question for me:

> How much information do we actually lose at the retinal level and how is coherent visual perception still possible?

To answer this question, I built a simplified computational model of the retina using convolutional neural networks (CNNs), focusing on how information is compressed and transformed prior to downstream processing.


## Project Overview

### This project implements:

- A retina-inspired encoder that mimics spatial pooling and bottlenecking

- A decoder that attempts to reconstruct the original image

- Quantitative measures of information loss vs. reconstruction fidelity

### The goal is not biological realism, but rather:

- To study functional consequences of early visual compression

- To understand how much structure can survive aggressive dimensionality reduction
