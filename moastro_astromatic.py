from moastro.astromatic import BatchSourceExtractor, Scamp
image_log = ImageLog(server='marvin')
image_sel = {'instrument': 'megaprime',
             'xi_eta': {'$within': {'$box': [[-4., -4.], [4., 4.]]}},
             'decomp_p_path': {'$exists': 1},
             'weightmap_path': {'$exists': 1}}

se_configs = {'PARAMETERS_NAME': 'se/scamp_catalog.param',
              'CATALOG_TYPE': 'FITS_LDAC',
              'DETECT_THRESH': '50.0', ...}
se = BatchSourceExtractor(image_log, image_sel, 'decomp_p_path',
                          'scamp.se_catalog_path',
                          weightKey='weightmap_path',
                          configs=se_configs)
se.run()

scamp_configs = {'ASTREF_CATALOG': 'USNO-B1',
                 'CENTROID_KEYS': 'XWIN_IMAGE,YWIN_IMAGE',
                 'CROSSID_RADIUS': '2.0', ...}
scamp = Scamp.from_db(image_log, image_sel,
                      'scamp.se_catalog_path',
                      configs=scamp_configs)
scamp.run()
scamp.save_scamp_headers(scampKey='scamp.header_path')
