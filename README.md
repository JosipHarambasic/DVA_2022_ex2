# DVA 2022: Exercise 2: Dimensional Reduction

## Goals
**Goal 1**: Understand what "high dimensional" data means, and how this typically looks in python 

You should be able to:
- Explain what the "shape" attribute of an numpy array indicates
- reshape numpy arrays

**Goal 2**: Understand how dimensional reduction can be applied in data visualization

You should be able to:
- Explain, what dimensional reduction is and why it is needed in data visualization
- Compute t-SNE, PCA and UMAP and apply it in an interactive application

## How to run the code
Tip: If you have never used python before, or the following points could 
just as well be part of the intergalactic highway scheme of Prostetnic Vogon Jeltz, please 
Google "how to install requirements.txt in python tutorial" and 
pick the one most attractive to you. 


1. If you haven't install Python https://www.python.org/downloads/ 
   or Conda https://anaconda.org/ (conda is up to your )
   
2. Open a Terminal on your machine and move to the directory of the code: 
   
    `cd /directory/of/this/code`
3. (Optional, but an indicator for good taste) Create a new virtual environment
   
    `python -m venv venv`
    
    Activate:
   
    Windows: `venv\Scripts\activate.bat`
   
    Else: `source venv/bin/activate`


4. Install the dependencies if you haven't before:
   
    `pip install -r requirements.txt`

5. Now you can always start your application directly with:
   `python -m bokeh serve --show .`

6. Abort it with Ctrl + C

## Questions? 
1. Google it
2. Ask a friend
3. Post to the forum 
4. Ask during the office hour
5. (Last resort) Write me a mail halter@ifi.uzh.ch