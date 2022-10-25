# bioformats_jar was screwing things up. with OME
conda create -n napari-npe2 python=3.9 pip notebook 
conda activate napari-npe2
pip install 'napari[all]'
pip install scipy scikit-learn matplotlib #jupyter
pip install aicsimageio 
pip install aicspylibczi
pip install aicssegmentation #downgrades napari and scikitlearn

pip install napari-aicsimageio  
pip install black
pip install pytest

pip install -e ../infer-subc-2D #infer_subc_2d

pip install -e .