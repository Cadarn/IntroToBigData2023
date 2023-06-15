# Streamlit Practical

We will use the Python Streamlit package to demonstrate how we can build interactive data apps/dashboards in Python.

During the workshop we built our first app, `first_app.py` to showcase the simplicty with which we can get started. This app can be run from the command line using the command:

```
streamlit run first_app.py
```
**Note**: You will need to be in the same directory as the app and have an active conda environment that has Streamlit installed together with the required libraries. If you have used the IBD23-workshop.yml to build a conda environment you should have everything you need.

The command above will launch the app locally and you should be able to view it in any web browser by going to `localhost:8501`.

## A more complicated example

In the workshop we also showcased a more intricate example that is called `tweet_app.py`. This can also be run using:
```
streamlit run tweet_app.py
```

**Note**: As both apps are in the same directory they both will also render the `pages` directory contents in the sidebar.

## Extension
It is left to the students to experiment with this technology to explore builiding their own apps with whatever data interests them.