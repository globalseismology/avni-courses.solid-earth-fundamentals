## Building Jupyter Book

Jupyter Book is an open-source tool for building publication-quality books and documents from computational material.

Jupyter Book allows users to

* write their content in [markdown files](https://myst-parser.readthedocs.io/en/latest/) or [Jupyter](https://jupyter.org/) notebooks,
* include computational elements (e.g., code cells) in either type,
* include rich syntax such as citations, cross-references, and numbered equations, and
* using a simple command, run the embedded code cells, [cache](https://jupyter-cache.readthedocs.io/en/latest/) the outputs and convert this content into:
    * a web-based interactive book and
    * a publication-quality PDF.

The Jupyter Book can be built by cleaning earlier builds, and building the book by forcing execution of notebooks to create content (through the `execute_notebooks : "force"` option in the [configuration file](_config.yml).

```
jupyter-book clean . --all
jupyter-book build -W -n --keep-going .
```

## Some Issues

### Change kernel name
Upon executing of the building process, there might be an error suggesting that the Python kernel is not found. This could be the case even if the Notebook itself executes properly from the server. The kernel name that Jupyter Lab displays on a notebook can be different from what Sphinx needs to create the Jupyter book. The available kernel for an environment is found using: 

```
%conda activate fall2022-sef
%jupyter kernelspec list
Available kernels:
  python3    /opt/export/course/geo203/anaconda3/envs/fall2022/share/jupyter/kernels/python3
```

If you open up your notebooks in a text editor (or change the extension to .json),
you should find a part like this:

```
{
   "metadata": {
      "kernelspec": {
        "name": "conda_fall2022",
        "display_name": "fall2022 [~/opt/export/course/geo203/anaconda3/envs/fall2022/]",
        "language": "python"
      }
   }
}
```

The "name" field needs to be one of the availabel kernel names from the `jupyter kernelspec list` command above. The jupyter notebook needs to be changed to:

```
{
   "metadata": {
      "kernelspec": {
        "name": "python3",
        "display_name": "fall2022 [~/opt/export/course/geo203/anaconda3/envs/fall2022/]",
        "language": "python"
      }
   }
}
```

One way to do this for multiple files is to replace using the `sed` command:

`sed -i -e 's/conda_fall2022/python3/g' ./*/*.ipynb`

After this replacement, the jupyter-book commands should create the book without issues.

### Hide or remove cell contents

For certain applications like a slideshow, the content of the code is not relevant. This can be hidden by modifying the Cell Metadata in the `Property Inspector -> Advanced Tools -> Cell Metadata` of the Notebook. If you add the tag `hide-input` to a cell, then Jupyter Book will hide the cell but display the outputs. Here’s an example of cell metadata that would trigger the “hide code” behavior:

```
{
    "tags": [
        "hide-input"
    ]
}
```
If you want the cell code to be completely removed instead of being hidden, use the `remove-input` tag instead of `hide-input`.
