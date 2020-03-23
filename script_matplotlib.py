from matplotlib_surface_plotting import plot_surf
import nibabel as nb
import numpy as np

vertices, faces=nb.freesurfer.io.read_geometry('lh.inflated')
overlay = nb.freesurfer.io.read_morph_data('lh.thickness')

#optional masking of medial wall
cortex=nb.freesurfer.io.read_label('lh.cortex.label')
mask=np.ones_like(overlay).astype(bool)
mask[cortex]=0
overlay[mask]=np.min(overlay)

plot_surf( vertices, faces, overlay, rotate=[90,270])