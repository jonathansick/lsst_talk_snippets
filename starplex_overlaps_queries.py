session.query(Catalog)\
    .filter(func.ST_Intersects(Catalog.footprint,
                               main_footprint)\


for catalog in overlapping_catalogs:
    clip = session.query(
        func.ST_Intersection(catalog.footprint,
                                main_catalog).\
        one()


for clip in clips:
    A = 0.
    for part in clip:
        A += self._s.scalar(part.ST_Area(use_spheroid=False))


def compiled_footprint(session, catalogs):
    """Returns a Geoalchemy2 footprint polygon from the compiled footprint."""
    return session.query(
        func.ST_Union(*[catalog.footprint for catalog in catalogs])).\
        one()[0]
