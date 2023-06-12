### Rupture geometry

All models here use the steep, northeast-dipping nodal plane, which seems to be 
supported by the dynamic rupture and finite fault models.

Though the strike, dip and rake of the earthquake are consistently estimated 
between models, there is a minor amount of variation in the location. This may 
not be super impactful, because the epicenter is offshore, so the epicentral 
distance to urban centers may not vary dramatically.

However, there is great variation in the depth of the rupture, at least as 
given by the hypocenters in the ruptures. Most models here as well as other
high-quality sources (e.g., [Ye et al., 
2017](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2017GL076085)) 
show rupture extending from about 20-70 km depth, with the centroid (location 
of maximum seismic moment release) at about 50 km. Ruptures much shallower than 
this should be treated with some skepticism.

The JMA model from the XML is striking orthogonally to the other models.  It 
was originally also in the southern hemisphere (negative latitudes) but I (RS) 
fixed it. I think whoever originally created the .xml file made some typos.  It 
should probably be redone from scratch.


### Tectonic region

The earthquake ruptured in the subducting Cocos slab, therefore Intraplate type 
GMPEs should be used.
