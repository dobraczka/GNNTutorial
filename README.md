# An intro to Graph Neural Networks 🕸️🧠

Graph Neural Networks have seen a rise in popularity. This is no surprise since various forms of information can be understood in the context of graphs from social networks to molecules.
This notebook intends to illuminate the inner workings of [Graph Convolutional Networks](https://arxiv.org/abs/1609.02907) and give an intuition into some other types of Networks which extend this idea.

# Environment and Kernel Setup

If you work on the clara/paula cluster [load](https://www.sc.uni-leipzig.de/user-doc/quickstart/hpc/#use-preinstalled-software) python:
```
ml Python/3.9.5-GCCcore-10.3.0
```
or Anaconda

```
ml Anaconda3/2021.11
```

and then create the environment with the respective dependencies:

```
conda env create n "PyG" -f environment.yml
```

Activate the environment

```
conda activate PyG
``` 

Now create a kernel to use in the Jupyter Notebook

```
ipython kernel install --user --name "PyG" --display-name "PyG"
```

Now you can go to the JupyterLab, select the kernel `PyG` and run the notebook.
