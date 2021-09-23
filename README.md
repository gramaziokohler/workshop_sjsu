# Robotic 360° Light Painting Workshop

at Department of Design, San Jose State University (SJSU), CA

![light2](https://user-images.githubusercontent.com/13201783/133784455-98f1603c-2795-4ea7-be04-f8d1fedb6658.jpg)

## Workshop Team

* Prof. Matthias Kohler
* Romana Rust
* Gonzalo Casas
* Beverly Lytle
* Michael Lyrenmann

## Workshop Description

This workshop will introduce parametric tools and produce 360° light drawings using SJSU's [UR5 robot](https://www.universal-robots.com/e-series/) and an [Insta360](https://www.insta360.com/) camera. The workshop will focus on two areas:

* Generative Design

    Using a combination of Rhino, Grasshopper and custom python tools, you will learn how to develop a parametric workflow to explore an infinite number of variations of a light design. We will provide you with a visualisation tool to anticipate how your 360° light drawing will look like.

* Robotic Light Drawing

    We will bring custom-made light tools for different light *strokes* to create the 360° light paintings. You will test different light tools, learn how to automate tasks and plan for safe robot motions. 


## Light Tools

We will bring different light tools with different attachments that allow you to control your light *stroke*. This can range from a single point to a line to diffused light. We will provide tools that allow you to easily adjust the light intensity and colour.

## Outcome
* 360° image to view in a browser
* picture for exhibition
* video of creation

## Schedule

### Part I: Introduction to Rhino / Grasshopper (Parametric Platform) on Zoom

Friday, Sept 24th 2021
09:00 - 11:00 AM GMT-7
06:00 - 08:00 PM CET

In this introduction we will introduce you to Rhino/Grasshopper as a platform and demonstrate the full process from creating of curves to robot movement in simulation.
We will record this lecture so you can watch it later on.

### Part 2: Offline Practice and Project Development

Between the Part 1 and Part 3, you will all work on your specific project ideas. Feel free to contact us via Slack as needed for help. It takes time to learn grasshopper so don't expect to pick it up right away. In addition to watching the recorded video from Part 1, here are a few helpful resources for learning Grasshopper.

* https://gramaziokohler.github.io/teaching_materials/rhino/
* https://gramaziokohler.github.io/teaching_materials/grasshopper/

Here are a few videos by the creator of Grasshopper, David Rutten:

[Grasshopper Getting Started by David Rutten - 01 - Interface Basics](https://vimeopro.com/rhino/grasshopper-getting-started-by-david-rutten)

If you want a more in-depth grasshopper handbook, Modelab has created an excellent book with example files:

[The Grasshopper Primer Third Edition](https://modelab.gitbooks.io/grasshopper-primer/content/index.html)



### Part 3: Session before workshop

Friday, Oct 22th 2021
09:00 - 11:00 AM GMT-7
06:00 - 08:00 PM CET

Last questions, talk about each designs, last changes ...

### Part 4: Workshop Week



# Files

We will share the main tools and files via this repository.

Our presentaton and useful links can also be found on the [MIRO board](https://miro.com/app/board/o9J_lwOiOCk=/)

# Communication

We created a slack channel for this workshop:

* [workshop-sjsu-2021](https://gramaziokohler.slack.com/messages/workshop-sjsu-2021/)

# Platforms

## Software

### Rhino

We will be using Rhino as the primary platform. 

If you don't have it already, you can download a 90-day free evaluation version of Rhino 7 here:

[Windows 90-day Evaluation](https://www.rhino3d.com/download/rhino-for-windows/evaluation)

[MacOS 90-day Evaluation](https://www.rhino3d.com/download/rhino-for-mac/evaluation)

### Grasshopper

[Grasshopper](https://www.rhino3d.com/features/#grasshopper) is a plugin for Rhino, and as of version 7, is installed by default in both the Mac and Windows versions. To open Grasshopper within Rhino, simply type "Grasshopper" in the command line or click the Grasshopper icon in the Standard toolbar (second from far right, green circle with insect).

### Grasshopper Plugins

One of the best things about Grasshopper is the massive ecosystem of third-party plugins. However, Grasshopper plugins can sometimes be difficult to install. However, things are getting better with Rhino 7. You should be able to use the Rhino Command "PackageManager" to open up the new Rhino package manager and install the plugins from the web.

* [Anemone](https://www.food4rhino.com/en/app/anemone)

On Mac, you need to copy the `anemone.gha` file into your Grasshopper Components folder. You can find this hidden folder by going to `Grasshopper > File > Special Folders > Components Folder`.

### Anaconda 3

We use Anaconda to make sure Python and all required libraries are installed correctly on all platforms. Please use the following download to install it:

* [Anaconda Individual Edition](https://www.anaconda.com/products/individual)

### Visual Studio Code

Most of the examples will be used from Rhino/Grasshopper, but the option to use them as stand alone scripts might create more opportunities. For that reason, we recommend installing the free code editor Visual Studio Code along with its Python extension:

* [VS Code](https://code.visualstudio.com/)
* [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Illustrator

You can import or export vector art between Rhino and Illustrator. You can also copy/paste between Rhino and Illustrator, although I don't recommend it for larger files.

## Installation

We use `conda` to make sure we have clean, isolated environment for dependencies.

First time using `conda`? Make sure you run this at least once:

    (base) conda config --add channels conda-forge

Now create a new conda environment:

    (base) conda env create -f https://dfab.link/sjsu-2021.yml

### Get the workshop files

    (base) conda activate sjsu
    (sjsu) git clone https://github.com/gramaziokohler/workshop_sjsu

### Add COMPAS to Rhino

    (sjsu) python -m compas_rhino.install -v 7.0
