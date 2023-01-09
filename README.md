# organelle-segmenter-plugin


[![License BSD-3](https://img.shields.io/pypi/l/organelle-segmenter-plugin.svg?color=green)](https://github.com/ergonyc/organelle-segmenter-plugin/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/organelle-segmenter-plugin.svg?color=green)](https://pypi.org/project/organelle-segmenter-plugin)
[![Python Version](https://img.shields.io/pypi/pyversions/organelle-segmenter-plugin.svg?color=green)](https://python.org)
[![tests](https://github.com/ergonyc/organelle-segmenter-plugin/workflows/tests/badge.svg)](https://github.com/ergonyc/organelle-segmenter-plugin/actions)
[![codecov](https://codecov.io/gh/ergonyc/organelle-segmenter-plugin/branch/main/graph/badge.svg)](https://codecov.io/gh/ergonyc/organelle-segmenter-plugin)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/organelle-segmenter-plugin)](https://napari-hub.org/plugins/organelle-segmenter-plugin)

🚨🚨🚨🚨 WARNING 🚨🚨🚨🚨 
This is NOT yet working

 🚧 WIP 🚧
A plugin that enables image segmentation of organelles from linearly-unmixed florescence images based on the segmenter tools provided by Allen Institute for Cell Science.  This fork is NOT a 3D (volumetric) segmentation at this time.  Instead it is a proof-of-concept which infers an "best" Z-slice / Z-projection and performes a 2D analysis.


A [napari](https://napari.org/stable/) plugin to infer subcellular components leveraging [infer-subc](https://github.com/ergonyc/infer-subc) and [aics-segmenter]( https://allencell.org/segmenter )

## GOAL
To measure shape, position, size, and interaction of eight organelles/cellular components (Nuclei (NU), Lysosomes (LS),Mitochondria (MT), Golgi (GL), Peroxisomes (PO), Endoplasmic Reticulum (ER), Lipid Droplet (LD), and SOMA) during differentiation of iPSCs, in order to understand the Interactome / Spatiotemporal coordination.

🚧 WIP 🚧
 
### Forked from Allen Institute for Cell Science project
The Allen Cell & Structure Segmenter plugin for napari, from which this projects is forked, provides an intuitive graphical user interface to access the powerful segmentation capabilities of an open source 3D segmentation software package developed and maintained by the Allen Institute for Cell Science (classic workflows only with v1.0). ​[The Allen Cell & Structure Segmenter](https://allencell.org/segmenter) is a Python-based open source toolkit developed at the Allen Institute for Cell Science for 3D segmentation of intracellular structures in fluorescence microscope images. This toolkit brings together classic image segmentation and iterative deep learning workflows first to generate initial high-quality 3D intracellular structure segmentations and then to easily curate these results to generate the ground truths for building robust and accurate deep learning models. The toolkit takes advantage of the high replicate 3D live cell image data collected at the Allen Institute for Cell Science of over 30 endogenous fluorescently tagged human induced pluripotent stem cell (hiPSC) lines. Each cell line represents a different intracellular structure with one or more distinct localization patterns within undifferentiated hiPS cells and hiPSC-derived cardiomyocytes.

More details about Segmenter can be found at https://allencell.org/segmenter

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/docs/plugins/index.html
-->

## Installation 🚧 WIP 🚧

### Option 2 (recommended): 

Clone the repo and install as editable module via pip.  via [pip]:

    pip install -e <path_to_cloned_repo>


### Option 2 🚧 COMING SOON 🚧 (not yet available on pypy)

After you installed the lastest version of napari, you can go to "Plugins" --> "Install/Uninstall Package(s)". Then, you will be able to see all available napari plugins and you can find us by name `napari-allencell-segmenter`. Just click the "install" button to install the Segmenter plugin.

### Option 3: 🚧 COMING SOON 🚧 (not yet available on pypy)

You can also install `organelle-segmenter-plugin` via [pip]:

    pip install organelle-segmenter-plugin
    
## Quick Start

In the current version, there are two parts in the plugin: **workflow editor** and **batch processing**. The **workflow editor** allows users adjusting parameters in all the existing workflows in the lookup table, so that the workflow can be optimized on users' data. The adjusted workflow can be saved and then applied to a large batch of files using the **batch processing** part of the plugin. 

1. Open a file in napari by dragging multi-channel .czi file onto napari which will import a multi-channel, multi-Z 'layer'. (Using the menu's defaults to `aicsIMAGEIO` reader which automatically splits mutliple channels into individual layers.  The plugin is able to support multi-dimensional data in .tiff, .tif. ome.tif, .ome.tiff, .czi)
2. Start the plugin (open napari, go to "Plugins" --> "napari-allencell-segmenter" --> "workflow editor")
3. Select the image and channel to work on
4. Select a workflow based on the example image and target segmentation based on user's data. Ideally, it is recommend to start with the example with very similar morphology as user's data.
5. Click "Run All" to execute the whole workflow on the sample data.
6. Adjust the parameters of steps, based on the intermediate results. For instruction on the details on each function and the effect of each parameter, click the tooltip button. A complete list of all functions can be found [here](https://github.com/AllenCell/aics-segmentation/blob/main/aicssegmentation/structure_wrapper_config/function_params.md)
7. Click "Run All" again after adjusting the parameters and repeat step 6 and 7 until the result is satisfactory.
8. Save the workflow
9. Close the plugin and open the **batch processing** part by (go to "Plugins" --> "napari-allencell-segmenter" --> "batch processing")
10. Load the customized workflow (or an off-the-shelf workflow) json file
11. Load the folder with all the images to process
12. Click "Run"

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-allencell-segmenter" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/AllenCell/napari-allencell-segmenter/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
