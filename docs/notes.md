# ongoing development notes

## subclassing allen cell tools

### aics-segmentation - Workflows
Created a gang of subclassed Workflow tools to extend rather than re-instantiate.  These were done in the `infer-subc-2D` dependency which exports `.workflow`.   

Key extensions are:
- pulling from the infer_subc_2d `Directories`
- enabling other _categories_ to workflow steps. e.g.
  - INFER_Z
  - POST_POST_PROCESSING



### napari-aics-segmentation - 

## pitfalls

the plugins expect _`layer_kwargs`_ as the reader.  

to engage the plugin readers you have to drag and drop the file ... simply using the "open" from the file menu doesn't properly search teh plugins...

Need to see if we put `napari-aicsimagio` back if we can choose to use our plugin _reader_ with D&D
-------
incondsistencies in the way the plugins are described... getting all the npe2 stuff right was tough.