class Catalog(UniqueMixin, Base):
    """SQLAlchemy table for representing a source `catalog`."""
    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    instrument = Column(String)
    footprint = Column(Geography(geometry_type='MULTIPOLYGON', srid=4326))
    meta = Column(MutableDict.as_mutable(JSON), default={})

    catalog_stars = relationship("CatalogStar",
                                 backref="catalog",
                                 passive_deletes=True)
