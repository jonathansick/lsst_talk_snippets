imagelog = ImageLog(server='marvin')
imagelog[image_key]
imagelog.find(query, fields=field_list, one=False)
imagelog.set(image_key, field, value)
imagelog.distinct(self, field, selector, images=None)
imagelog.compress_fits(path_key, selector=query,
                       alg="Rice", q=4, delete=False)
imagelog.decompress_fits(path_key, decompKey=None,
                         decompDir=None, selector=query,
                         delete=False, overwrite=False,
                         nthreads=multiprocessing.cpu_count())
imagelog.rename_field(old_field, new_field, selector=query, multi=True)
imagelog.delete_field(field, selector=query, multi=True)
imagelog.move_files(path_key, dest_dirname, selector=query, copy=False)
imagelog.delete_files(path_key, selector=query)
