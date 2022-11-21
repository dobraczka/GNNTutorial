# Kernel Setup

If you work on the clara/paula cluster load python:
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
