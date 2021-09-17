# Robotic Light Painting Workshop

## Department of Design, SJSU, CA

![image](https://user-images.githubusercontent.com/13201783/122343449-ff6da180-cf45-11eb-8baf-2d452b6c068e.png)

## Workshop Team

* Prof. Matthias Kohler
* Romana Rust
* Gonzalo Casas
* Beverly Lytle
* Michael Lyrenmann

## Workshop Description

This workshop will introduce parametric tools and produce light drawings using SJSU's UR robot. The workshop will focus on two areas:

### Generative Design

Using a combination of Rhino, Grasshopper, you will learn how to develop a parametric workflow where you are creating a machine that produces an infinite number of variations of a design. Using Grasshopper you can automate these tasks and explore the larger design space of your ideas. 

### Robotic Drawing

Automation is a power tool in manufacturing and cheaper and safer robots are now available for artists and designer to explore. ....


## Examples
* http://eduardochamorro.github.io/beansreels/portfolio/lightpainting.html
* http://lightpaintingblog.com/using-virtual-reality-to-augment-light-drawing/
* http://mkmra2.blogspot.com/2017/01/robotic-painting-with-line-of-lights.html
* https://www.idz.ro/rlp/
* https://fstoppers.com/bts/introducing-3d-light-painting-called-holopainting-133534
* https://www.youtube.com/watch?v=C9Zf-JKBrDM
* https://www.facebook.com/629838447196347/photos/a.757921707721353/764319487081575/?type=3


## Tools
* Single light dot
* round array of LEDs (controllable via Arduino)
* line-like array of LEDs (controllable via Arduino)

## Outcome
* 360 Video to view on Phone or goggles
* One image for exhibition
* Video of creation

## Schedule

### Part I: Introduction to Rhino / Grasshopper (Parametric Platform)

Date Friday, Sept 24th 2021, 17:00 - 19:00 CEST, on Zoom 
pacific time? 8am - 10:30am Pacific Time

In this introduction we will introduce you to Rhino/Grasshopper as a platform and demonstrate the full process from creating of curves to robot movement in simulation.
We will record this lecture so you can watch it later on.


### Part 2: Offline Practice and Project Development

Between the Part 1 and Part 2, you will all work on your specific project ideas. Feel free to contact us via Slack as needed for help. It takes time to learn grasshopper so don't expect to pick it up right away. In addition to watching the recorded video from Part 1, here are a few helpful resources for learning Grasshopper:

Here are a few videos by the creator of Grasshopper, David Rutten:

[Grasshopper Getting Started by David Rutten - 01 - Interface Basics](https://vimeopro.com/rhino/grasshopper-getting-started-by-david-rutten)

If you want a more in-depth grasshopper handbook, Modelab has created an excellent book with example files:

[The Grasshopper Primer Third Edition](https://modelab.gitbooks.io/grasshopper-primer/content/index.html)

* https://gramaziokohler.github.io/teaching_materials/rhino/
* https://gramaziokohler.github.io/teaching_materials/grasshopper/

### Part 3: Friday before 



# Files

I will be using Google Drive to provide you the tutorial files and other files needed for the Workshop. These files can be found at this [link](https://drive.google.com/drive/folders/1CN08vqqBTsIr9l08Cg3W08fXpyRp2-hw?usp=sharing).

[https://drive.google.com/drive/folders/1CN08vqqBTsIr9l08Cg3W08fXpyRp2-hw?usp=sharing](https://drive.google.com/drive/folders/1CN08vqqBTsIr9l08Cg3W08fXpyRp2-hw?usp=sharing)

---

# Platforms

## Software

### Miro

I will be using Miro to sketch certain ideas throughout the workshop. Feel free to also use Miro to sketch your ideas for your project. 

Link to Miro Workshop Board: 

[https://miro.com/app/board/o9J_lPeTaeA=/](https://miro.com/app/board/o9J_lPeTaeA=/)

### Rhino

We will be using Rhino as the primary platform. 

You can download a 90-day free evaluation version of Rhino 7 here:

[Windows 90-day Evaluation](https://www.rhino3d.com/download/rhino-for-windows/evaluation) (64-bit Windows 8.1 or 10)

[MacOS 90-day Evaluation](https://www.rhino3d.com/download/rhino-for-mac/evaluation) (Note: only Intel chip macs, not the new M1 processes released this fall)

### Grasshopper

[Grasshopper](https://www.rhino3d.com/features/#grasshopper) is a plugin for Rhino, and as of version 7, is installed by default in both the Mac and Windows versions. To open Grasshopper within Rhino, simply type "Grasshopper" in the command line or click the Grasshopper icon in the Standard toolbar (second from far right, green circle with insect).

### Grasshopper Plugins

One of the best things about Grasshopper is the massive ecosystem of third-party plugins. However, Grasshopper plugins can sometimes be difficult to install. However, things are getting better with Rhino 7. You should be able to use the Rhino Command "PackageManager" to open up the new Rhino package manager and install the plugins from the web. If you are not Some of these will not work on MacOs. Here is what the package manager looks like when you search for the Human plugin.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/919ee89c-36c3-425f-bb6c-5e396069742e/PackageManager.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/919ee89c-36c3-425f-bb6c-5e396069742e/PackageManager.jpg)

**List of Grasshopper Plugins you should try to install:**

- **Human**: You should be able to install either the Mac or PC version of Human via the **Package Manager**. Please note: there are two plugins that are named Human. One is "Human" and one is "Human-UI". Only download the "Human" version. The UI version is for creating User Interfaces for your parametric model. Fun, but not needed for this workshop.
- **Wombat**: This plugin can be installed via the **Package Manager**. Wombat has some helpful components for working with text and fonts.
- **Clipper**: This plugin provides similar functionality to the Pathfinder tools in Illustrator. Great for adding or subtracting shapes (Boolean Union, Difference, Intersection) as well as offsetting polylines. It can be installed via the **Package Manager**.
- **Bifocals**: Bifocals is **not in the package manager**. It is not essential, but I use it during teaching as it shows both the icon and the text label of the components. While learning Grasshopper it is a helpful plugin to have, but not necessary. You can either download it from the plugins folder on Google Drive or go to the original source on the Food4Rhino website. To download it, go to the [Food4Rhino.com](http://food4rhino.com) , register, and download. You will need to place the GHA file in your Grasshopper Library. It should work for either PC or Mac. The website says it is for Rhino 4 & 5, but it works in Rhino 7.

    [Bifocals](https://www.food4rhino.com/app/bifocals)

- **Robots**: This plugin will be much harder to install and will only work on Windows. Robots is a plugin for Rhino developed at The Bartlett School of Architecture by Vicente Soler. It works for a number of different robot models and brands such as Universal Robots, ABB robots, and Kuka robots. To find out more about the Robots project, visit its home on Github:

    [Releases · visose/Robots](https://github.com/visose/Robots/releases)

    1. Go to the Workshop Google Drive and go to Plugins > Robots. Download all of the files in the folder.
    2. Unblock all of the files (right-click on each file > properties > unblock > apply). 
    3. Copy the *robots.gha* and the *robots.dll* files to your Grasshopper Components folder. You can find this hidden folder by going to Grasshopper > *File > Special Folders > Components Folder*. 
    4. In your Windows *Documents* folder, Create a new folder called "Robots"
    5. Place the *SJSU.xml* and *SJSU.3DM* files that you downloaded and unblocked in this Robots folder.
    6. Closer Grasshopper and Rhino and restart them. If all was successful, you should now have a "Robots" tab in Grasshopper. 

### Illustrator

You can import or export vector art between Rhino and Illustrator. You can also copy/paste between Rhino and Illustrator, although I don't recommend it for larger files.

























Duration: 3 days, 27.10-29.10
-	Use the workshop as black box
Questions
-	How many students? 15 students
-	What software they are familiar with?
-	1 UR5 e series robot
Result: Picture, Video 




### Software requirements:


Workshop Participants

Participants’ Involvement and Learning Goals:



Provided Equipment
UR10 robots

Required Equipment

