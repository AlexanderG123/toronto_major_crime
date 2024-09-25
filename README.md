# Toronto Major Crime Trends and Analysis

## Overview of the Project

This repo documents the steps and processes used in creating the paper "Toronto Major Crime". 

Use this folder to reproduce the results on your own.

Note on LLM usage: 
LLMs were used, GPT 4 was helpful with a lot of the coding aspects of the project, in particular the simulation.  

## File Structure

The repo is structured as:

-   `input/data` contains the data sources used in analysis including the raw data. NOTE: As the data file was too large to upload to Github, to access this data the paper will need to be reproduced and the "data_download.py" script will need to be run. 
-   `outputs/data` contains the cleaned dataset that was constructed.
-   `outputs/paper` contains the files used to generate the paper, including the Quarto document and reference bibliography file, as well as the PDF of the paper. 
-   `scripts` contains the Python scripts used to simulate, download and clean data.