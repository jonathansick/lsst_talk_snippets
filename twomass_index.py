c.ensure_index([("coord", GEO2D),
                ("j_m-k_m", ASCENDING),
                ("k_m", ASCENDING), ("j_m", ASCENDING), ("h_m", ASCENDING),
                ("h_m-k_m", ASCENDING), ("j_m-h_m", ASCENDING)],
               min=-90., max=360.,
               name="radec_color",
               background=True)
