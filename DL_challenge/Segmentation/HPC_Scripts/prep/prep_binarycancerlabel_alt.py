import os
os.environ['OV_DATA_BASE'] = "/bask/projects/p/phwq4930-renal-canc/data/seg_data"
from KCD.Segmentation.ovseg.preprocessing.SegmentationPreprocessing import SegmentationPreprocessing

data_name = 'masked_coreg_ncct'
spacing = 2

preprocessed_name = '2mm_binary_canceronly_alt'

lb_classes = [2]

target_spacing=[spacing]*3

kits19ncct_dataset_properties ={
    		'median_shape' : [104., 512., 512.],
    		'median_spacing' : [2.75,      0.8105, 0.8105],
    		'fg_percentiles' : [-118, 136 ],
    		'percentiles' : [0.5, 99.5],
    		'scaling_foreground' : [ 42.94977,  11.57459],
    		'n_fg_classes' : 1,
    		'scaling_global' : [ 510.60403, -431.1344],
    		'scaling_window' : [ 68.93295,  -65.79061]}

prep = SegmentationPreprocessing(apply_resizing=True, 
                                    apply_pooling=False, 
                                    apply_windowing=True,
                                    lb_classes=lb_classes,
                                    target_spacing=target_spacing,
                                    scaling = [ 42.94977,  11.57459],
                                    window = [-118, 136 ],
                                    reduce_lb_to_single_class = True,
                                    dataset_properties = kits19ncct_dataset_properties)


prep.initialise_preprocessing()

prep.preprocess_raw_data(raw_data=data_name,
                          preprocessed_name=preprocessed_name)