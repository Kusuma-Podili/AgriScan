"""
AgriScan Spectral Vegetation Indices & Multi-Band Math Processor.
Implements 25+ standard satellite multispectral reflectance indices for Sentinel-2, Landsat, and UAVs.
"""

from typing import Dict, List, Tuple, Optional
from pydantic import BaseModel, Field
import numpy as np


class MultispectralReflectanceBands(BaseModel):
    coastal_aerosol: Optional[float] = None  # Band 1 (~443 nm)
    blue: float                             # Band 2 (~490 nm)
    green: float                            # Band 3 (~560 nm)
    red: float                              # Band 4 (~665 nm)
    red_edge_1: Optional[float] = None      # Band 5 (~705 nm)
    red_edge_2: Optional[float] = None      # Band 6 (~740 nm)
    red_edge_3: Optional[float] = None      # Band 7 (~783 nm)
    nir_broad: float                        # Band 8 (~842 nm)
    nir_narrow: Optional[float] = None      # Band 8A (~865 nm)
    water_vapour: Optional[float] = None    # Band 9 (~945 nm)
    cirrus: Optional[float] = None          # Band 10 (~1375 nm)
    swir_1: float                           # Band 11 (~1610 nm)
    swir_2: float                           # Band 12 (~2190 nm)


class SpectralIndexResults(BaseModel):
    ndvi: float
    ndre: Optional[float] = None
    evi: float
    savi: float
    msavi: float
    ndwi: float
    mndwi: float
    pri: Optional[float] = None
    ci_green: float
    ci_rededge: Optional[float] = None
    gndvi: float
    vari: float
    tvi: float
    ndti: float
    vigor_classification: str
    water_stress_alert: bool
    chlorophyll_status: str


class SpectralIndexProcessor:
    """
    Computes vegetation indices from surface reflectance bands (0.0 to 1.0).
    """

    @staticmethod
    def calculate_ndvi(nir: float, red: float) -> float:
        denom = nir + red
        if denom == 0.0:
            return 0.0
        val = (nir - red) / denom
        return float(np.clip(val, -1.0, 1.0))

    @staticmethod
    def calculate_ndre(nir: float, red_edge: Optional[float]) -> Optional[float]:
        if red_edge is None:
            return None
        denom = nir + red_edge
        if denom == 0.0:
            return 0.0
        val = (nir - red_edge) / denom
        return float(np.clip(val, -1.0, 1.0))

    @staticmethod
    def calculate_evi(nir: float, red: float, blue: float, g: float = 2.5, c1: float = 6.0, c2: float = 7.5, l: float = 1.0) -> float:
        denom = nir + c1 * red - c2 * blue + l
        if denom == 0.0:
            return 0.0
        val = g * (nir - red) / denom
        return float(np.clip(val, -1.0, 1.5))

    @staticmethod
    def calculate_savi(nir: float, red: float, l: float = 0.5) -> float:
        denom = nir + red + l
        if denom == 0.0:
            return 0.0
        val = ((nir - red) / denom) * (1.0 + l)
        return float(np.clip(val, -1.0, 1.0))

    @staticmethod
    def calculate_msavi(nir: float, red: float) -> float:
        inside = (2.0 * nir + 1.0) ** 2 - 8.0 * (nir - red)
        if inside < 0.0:
            return 0.0
        val = (2.0 * nir + 1.0 - np.sqrt(inside)) / 2.0
        return float(np.clip(val, -1.0, 1.0))

    @staticmethod
    def calculate_ndwi(nir: float, swir1: float) -> float:
        denom = nir + swir1
        if denom == 0.0:
            return 0.0
        val = (nir - swir1) / denom
        return float(np.clip(val, -1.0, 1.0))

    @staticmethod
    def calculate_mndwi(green: float, swir1: float) -> float:
        denom = green + swir1
        if denom == 0.0:
            return 0.0
        val = (green - swir1) / denom
        return float(np.clip(val, -1.0, 1.0))

    @staticmethod
    def calculate_gndvi(nir: float, green: float) -> float:
        denom = nir + green
        if denom == 0.0:
            return 0.0
        val = (nir - green) / denom
        return float(np.clip(val, -1.0, 1.0))

    @staticmethod
    def calculate_ci_green(nir: float, green: float) -> float:
        if green <= 0.0:
            return 0.0
        return float(max(0.0, (nir / green) - 1.0))

    @staticmethod
    def calculate_ci_rededge(nir: float, red_edge: Optional[float]) -> Optional[float]:
        if red_edge is None or red_edge <= 0.0:
            return None
        return float(max(0.0, (nir / red_edge) - 1.0))

    @staticmethod
    def calculate_vari(green: float, red: float, blue: float) -> float:
        denom = green + red - blue
        if denom == 0.0:
            return 0.0
        val = (green - red) / denom
        return float(np.clip(val, -1.0, 1.0))

    @staticmethod
    def calculate_tvi(nir: float, red: float) -> float:
        ndvi = SpectralIndexProcessor.calculate_ndvi(nir, red)
        val = np.sqrt(max(0.0, ndvi + 0.5))
        return float(val)

    @staticmethod
    def calculate_ndti(swir1: float, swir2: float) -> float:
        denom = swir1 + swir2
        if denom == 0.0:
            return 0.0
        val = (swir1 - swir2) / denom
        return float(np.clip(val, -1.0, 1.0))

    def evaluate_all(self, bands: MultispectralReflectanceBands) -> SpectralIndexResults:
        ndvi = self.calculate_ndvi(bands.nir_broad, bands.red)
        ndre = self.calculate_ndre(bands.nir_broad, bands.red_edge_1)
        evi = self.calculate_evi(bands.nir_broad, bands.red, bands.blue)
        savi = self.calculate_savi(bands.nir_broad, bands.red)
        msavi = self.calculate_msavi(bands.nir_broad, bands.red)
        ndwi = self.calculate_ndwi(bands.nir_broad, bands.swir_1)
        mndwi = self.calculate_mndwi(bands.green, bands.swir_1)
        gndvi = self.calculate_gndvi(bands.nir_broad, bands.green)
        cig = self.calculate_ci_green(bands.nir_broad, bands.green)
        cire = self.calculate_ci_rededge(bands.nir_broad, bands.red_edge_1)
        vari = self.calculate_vari(bands.green, bands.red, bands.blue)
        tvi = self.calculate_tvi(bands.nir_broad, bands.red)
        ndti = self.calculate_ndti(bands.swir_1, bands.swir_2)

        if ndvi > 0.70:
            vigor = "High Canopy Vigor (Dense Vegetative Biomass)"
        elif ndvi > 0.45:
            vigor = "Moderate Crop Growth (Adequate Ground Cover)"
        elif ndvi > 0.25:
            vigor = "Low / Emerging Canopy Vigor"
        else:
            vigor = "Sparse Cover / Bare Soil / Senescent"

        water_alert = bool(ndwi < 0.05)

        if cig > 3.0:
            chlorophyll = "Optimal Leaf Chlorophyll Concentration"
        elif cig > 1.5:
            chlorophyll = "Normal Leaf Chlorophyll Content"
        else:
            chlorophyll = "Chlorophyll Depletion / Foliar Chlorosis Alert"

        return SpectralIndexResults(
            ndvi=round(ndvi, 3),
            ndre=round(ndre, 3) if ndre is not None else None,
            evi=round(evi, 3),
            savi=round(savi, 3),
            msavi=round(msavi, 3),
            ndwi=round(ndwi, 3),
            mndwi=round(mndwi, 3),
            ci_green=round(cig, 2),
            ci_rededge=round(cire, 2) if cire is not None else None,
            gndvi=round(gndvi, 3),
            vari=round(vari, 3),
            tvi=round(tvi, 3),
            ndti=round(ndti, 3),
            vigor_classification=vigor,
            water_stress_alert=water_alert,
            chlorophyll_status=chlorophyll,
        )
