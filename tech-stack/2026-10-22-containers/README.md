## Preamble
<img src="s1.png" width="50%">
<img src="s2.png" width="50%">
<img src="s3.png" width="50%">
<img src="s4.png" width="50%">

<!-- <img src="hykes.png" width="50%"> -->

## Goal
**Today:** Recognize when to use a container
* Jargon
* Examples

**Tomorrow:** Practice, Practice, Practice
* Tutorial
* Workout Plan


## Motivation

<img src="hpc-preamble.png" width="50%">

<!--
another example is when you want to work but you don't have your machine so the configuration isn't the way you like it

another example is how i use cloud tools because they behave the same on every machine because they don't run local (problem of latency)

example from https://github.com/mfriedel/DS6021_F26 https://github.com/mfriedel/DS6021_F26#python-environment-setup -- this section is all about getting requirements.txt to work but ....... the problem can be bigger ...... the concept of containers lets us package up one level ...... os level virtualization
-->

### Environment Example DS 6021
https://github.com/mfriedel/DS6021_F26




## CONTENT
### jargon
<img src="docker-architecture.webp" width="100%">

### Applications
1. Devcontainers
2. Local Databases

<img src="Docker_Logo.svg.webp" width="50%">

<img src="Kubernetes_logo_without_workmark.svg.webp" width="50%">




Docker Desktop App
Docker Account


## Container Sequence
https://docs.docker.com/get-started/docker-overview/
https://uvads.github.io/container-basics/
[dotScale 2013 - Solomon Hykes - Why we built Docker](https://www.youtube.com/watch?v=3N3n9FzebAA)

### Images v Containers

metaphor Image:Recipie::Container:Food

Exploring Docker Desktop
images -> layers (use joke and compare to dockerfile)
containers -> files (use welcome to docker and compare to unix file system)

# How to practice
1. Work the docs "Getting Started" -- [https://www.docker.com/trainings/](https://www.docker.com/trainings/)
    * Installation
    * Download and run your first container
    * Download and run a stack
    * Build your first image
    * Share the image
  
2. Tell some jokes
    * Get this container running
    * https://github.com/uvasds-systems/joke-container
    * Courtesy of Professor Magee
  
3. Build your own
    * Build and image of your development environment
    * Share that image
  

# References
1. What is Docker - https://docs.docker.com/get-started/docker-overview/
2. Build and share a containerized application - https://docs.docker.com/get-started/tutorials/run-an-app/
3. Containers in Data Science - https://uvads.github.io/container-basics/
4. [dotScale 2013 - Solomon Hykes - Why we built Docker](https://www.youtube.com/watch?v=3N3n9FzebAA)




# everything below here will go away before tlak time
------- jargon to make sure we cover

Docker "Docker distributes applications in images." ~docs.docker.com
Kubernetes. -"Docker is a container runtime technology that allows you to build, test, and deploy applications faster than traditional methods. It packages software into standardized units called containers with everything the software needs to run—including libraries, system tools, and code. Kubernetes is a container orchestration tool that allows you to scale your container systems so you can manage, coordinate and schedule containers at a vast scale." ~ [aws.amazon.com](https://aws.amazon.com/compare/the-difference-between-kubernetes-and-docker/)
Docker, Inc.
Docker Hub
Dockerfile
Docker Desktop
Solomon Hykes

image
container "A container is a running instance of an image." ~docs.docker.com
layer
Dockerfile

virtualization - turn a physical resource into multiple logical resources
virtual environment - uses the same kernel
container - os-level virtualization
virtual machine - running a separate kernel in a logical allocation




