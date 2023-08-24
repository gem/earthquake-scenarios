import math
import numpy as np
import pandas as pd

# -------------------------------------------------------------------------
# Generic GMICE implementation
# -------------------------------------------------------------------------


def GenericSimpleGMICE(stations_idx, supported_imts, constants, conversions):
    """
    Generic wrapper for Simplified Predictive Equations

    MMI = a + b log(Y), σ

    """

    # Initialize output dataframe
    df = pd.DataFrame(index=stations_idx.index)

    # Determine imts in original values
    original_imts = [col.split("_").pop(0) for col in stations_idx.columns if col.endswith("_VALUE") and not col.startswith("MMI")]

    # Store original values
    for imt in supported_imts:
        if imt not in original_imts:
            df[f"{imt}_VALUE"] = float('nan')
            df[f"{imt}_LN_SIGMA"] = float('nan')
    
    # Remove original values that are not supported
    for imt in original_imts:
        if imt not in supported_imts:
            df[f"{imt}_VALUE"] = float('nan')
            df[f"{imt}_LN_SIGMA"] = float('nan')

    # General functional form
    Y = dict.fromkeys(supported_imts)
    for imt in supported_imts:
        if imt == "PGV":
            Y[imt] = lambda MMI: 10.**((1./constants[imt]['b'])*(
                                MMI - constants[imt]['a'])) * conversions['velocity']
        else:
            Y[imt] = lambda MMI: 10.**((1./constants[imt]['b'])*(
                                MMI - constants[imt]['a'])) * conversions['acceleration']

    # Apply GMICE
    for imt in supported_imts:
        df[f"{imt}_VALUE"] = stations_idx.MMI_VALUE.apply(Y[imt])
        df[f"{imt}_LN_SIGMA"] = constants[imt]['σ']

    # Return result
    return df


def GenericPiecewiseGMICE(stations_idx, supported_imts, constants, conversions):
    """
    Generic wrapper for Simplified Predictive Equations

    MMI = a1 + b1 log(Y), σ1 for MMI ≤ t_MMI 
    MMI = a2 + b2 log(Y), σ2 for MMI > t_MMI

    """

    # Initialize output dataframe
    df = pd.DataFrame(index=stations_idx.index)

    # Determine imts in original values
    original_imts = [col.split("_").pop(0) for col in stations_idx.columns if col.endswith("_VALUE") and not col.startswith("MMI")]

    # Store original values
    for imt in supported_imts:
        if imt not in original_imts:
            df[f"{imt}_VALUE"] = float('nan')
            df[f"{imt}_LN_SIGMA"] = float('nan')
    
    # Remove original values that are not supported
    for imt in original_imts:
        if imt not in supported_imts:
            df[f"{imt}_VALUE"] = float('nan')
            df[f"{imt}_LN_SIGMA"] = float('nan')

    # General functional form
    Y = dict.fromkeys(supported_imts)
    σ = dict.fromkeys(supported_imts)
    for imt in supported_imts:
        # Median value
        if imt == "PGV":
            Y[imt] = lambda MMI: 10.**((1./constants[imt]['b1'])*(
                                    MMI - constants[imt]['a1']))*conversions['velocity'] if \
                                    MMI <= constants[imt]['t_MMI'] else \
                                    10.**((1./constants[imt]['b2'])*(
                                    MMI - constants[imt]['a2']))*conversions['velocity']
            
        else:
            Y[imt] = lambda MMI: 10.**((1./constants[imt]['b1'])*(
                                    MMI - constants[imt]['a1']))*conversions['acceleration'] if \
                                    MMI <= constants[imt]['t_MMI'] else \
                                    10.**((1./constants[imt]['b2'])*(
                                    MMI - constants[imt]['a2']))*conversions['acceleration']
        # Uncertainty
        σ[imt] = lambda MMI: constants[imt]['σ1'] if MMI <= constants[imt]['t_MMI'] \
                                else constants[imt]['σ2']

    # Apply GMICE
    for imt in supported_imts:
        df[f"{imt}_VALUE"] = stations_idx.MMI_VALUE.apply(Y[imt])
        df[f"{imt}_LN_SIGMA"] = stations_idx.MMI_VALUE.apply(σ[imt])

    # Return result
    return df

# -------------------------------------------------------------------------
# Piecewise GMICE (MMI = a1 + b1 log Y for CASE; MMI = a2 + b2 log Y o.w.)
# -------------------------------------------------------------------------


def CaprioEtAl2015():
    """
    Gilla, Marta, Bernadetta Tarigan, C. Bruce Worden, Stefan Wiemer, and David J. Wald.
    "Ground motion to intensity conversion equations (GMICEs): A global relationship and
    evaluation of regional dependency." Bulletin of the Seismological Society of America
    105, no. 3 (2015): 1476-1490.

    Simplified Predictive Equations:

    MMI = a1 + b1 log(Y) for MMI ≤ t_MMI
    MMI = a2 + b2 log(Y) for MMI > t_MMI
    """

    # Supported IMTs
    supported_imts = ["PGA" ,"PGV"]

    # Conversion from units to g
    conversions = dict.fromkeys(["acceleration", "velocity"])
    conversions["acceleration"] = (1./9.81) * (1./100.) # cm/s^2 to g
    conversions["velocity"] = 1. # cm/s to cm/s

    # Constants:
    constants = {
        "PGV": {'a1':  4.424, 'b1': 1.589,
                'a2':  4.018, 'b2': 2.671,
                'σ1':  0.9,   'σ2': 1.3,   't_MMI': 4.92},
        "PGA": {'a1':  2.270, 'b1': 1.647,
                'a2': -1.361, 'b2': 3.822,
                'σ1': 0.7,    'σ2': 1.4,   't_MMI': 4.87},
    }

    # Return result
    return supported_imts, constants, conversions


def MoratalaEtAl2021():
    """
    Moratalla, Jose M., Tatiana Goded, David A. Rhoades, Silvia Canessa, and Matthew C.
    Gerstenberger. "New ground motion to intensity conversion equations (GMICEs) for New
    Zealand." Seismological Society of America 92, no. 1 (2021): 448-459.

    Simplified Predictive Equations:

    MMI = a1 + b1 log(Y) for MMI ≤ t_MMI
    MMI = a2 + b2 log(Y) for MMI > t_MMI
    """

    # Supported IMTs
    supported_imts = ["PGA" ,"PGV"]

    # Conversion from units to g
    conversions = dict.fromkeys(["acceleration", "velocity"])
    conversions["acceleration"] = (1./9.81) * (1./100.) # cm/s^2 to g
    conversions["velocity"] = 1. # cm/s to cm/s

    # Constants:
    constants = {
        "PGV": {'a1':  4.1070, 'b1': 1.6323,
                'a2':  1.8970, 'b2': 3.8370,
                'σ1':  0.3455,   'σ2': 0.3455,   't_MMI': 5.7433},
        "PGA": {'a1':  1.7601, 'b1': 1.9920,
                'a2': -1.9095, 'b2': 3.9322,
                'σ1': 0.2769,    'σ2': 0.2769,   't_MMI': 5.5277},
    }

    # Return result
    return supported_imts, constants, conversions


def MontalvoArrietaEtAl2019():
    """
    Montalvo‐Arrieta, Juan C., Xyoli Pérez‐Campos, Leonardo Ramirez‐Guzman, Rocío L.
    Sosa‐Ramírez, Moisés Contreras Ruiz‐Esparza, and Miguel Leonardo‐Suárez.
    "Macroseismic Intensities from the 19 September 2017 Mw 7.1 Puebla–Morelos Earthquake."
    Seismological Research Letters 90, no. 6 (2019): 2142-2153.

    Simplified Predictive Equations:

    MMI = a1 + b1 log(Y) for MMI ≤ t_MMI
    MMI = a2 + b2 log(Y) for MMI > t_MMI
    """

    # Supported IMTs
    supported_imts = ["PGA" ,"PGV", "SA(1.0)", "SA(2.0)", "SA(3.0)"]

    # Conversion from units to g
    conversions = dict.fromkeys(["acceleration", "velocity"])
    conversions["acceleration"] = (1./9.81) * (1./100.) # cm/s^2 to g
    conversions["velocity"] = 1. # cm/s to cm/s

    # Constants NOTE: The authors note a as b, b as m; t_MMI not directly provided
    constants = {
        "PGV": {'a1':   3.7037, 'b1': 2.2353,
                'a2': -1.2863,  'b2': 7.7556,
                'σ1':   0.17,   'σ2': 0.17,   't_Y': 0.9039},
        "PGA": {'a1':   1.7539, 'b1': 2.1428,
                'a2': -15.4299, 'b2': 11.5325,
                'σ1': 0.11,     'σ2': 0.11,   't_Y': 1.8301},
        "SA(1.0)": {'a1':   1.2346, 'b1': 2.3458,
                    'a2': -15.0481, 'b2': 10.6370,
                    'σ1':  0.23,    'σ2': 0.23,   't_Y': 1.9638},
        "SA(2.0)": {'a1':  1.9865,  'b1': 2.3346,
                    'a2': -1.0293,  'b2': 4.3100,
                    'σ1':  0.21,    'σ2': 0.21,   't_Y': 1.5267},
        "SA(3.0)": {'a1':  2.6109, 'b1': 2.5574,
                    'a2': -0.4066, 'b2': 5.0577,
                    'σ1': 0.23,     'σ2': 0.23,   't_Y': 1.2069},
    }

    # Need to calculate t_MMI
    for imt in supported_imts:
        constants[imt]["t_MMI"] = constants[imt]['a1'] + constants[imt]['b1'] * math.log10(constants[imt]['t_Y'])

    # Return result
    return supported_imts, constants, conversions


def WordenEtAl2012():
    """
    C. B. Worden, M. C. Gerstenberger, D. A. Rhoades, D. J. Wald; 
    Probabilistic Relationships between Ground‐Motion Parameters and 
    Modified Mercalli Intensity in California. 
    Bulletin of the Seismological Society of America 2012;; 
    102 (1): 204–221. doi: https://doi.org/10.1785/0120110156
    
    Simplified Predictive Equations:

    MMI = a1 + b1 log(Y) for MMI ≤ t1
    MMI = a2 + b2 log(Y) for MMI > t1
    """

    # Supported IMTs
    supported_imts = ["PGA" ,"PGV", "SA(0.3)", "SA(1.0)", "SA(3.0)"]

    # Conversion from units to g
    conversions = dict.fromkeys(["acceleration", "velocity"])
    conversions["acceleration"] = (1./9.81) * (1./100.) # cm/s^2 to g
    conversions["velocity"] = 1. # cm/s to cm/s

    # Constants NOTE: The authors note a1 as c1, b1 as b1, a2 as c3, b2 as c4, t_MMI as t1
    # Constants:
    constants = {
        "PGV": {'a1':  3.78,  'b1': 1.47,
                'a2':  2.89,  'b2': 3.16,
                'σ1':  0.65,  'σ2': 0.65,   't_MMI': 0.53},
        "PGA": {'a1':  1.78,  'b1': 1.55,
                'a2':  -1.60, 'b2': 3.70,
                'σ1':  0.73,  'σ2': 0.73,   't_MMI': 1.57},
        "SA(0.3)": {'a1':  1.26,  'b1': 1.69,
                    'a2':  -4.15, 'b2': 4.14,
                    'σ1':  0.84,  'σ2': 0.84,   't_MMI': 2.21},
        "SA(1.0)": {'a1':  2.50,  'b1': 1.51,
                    'a2':  0.20,  'b2': 2.90,
                    'σ1':  0.80,  'σ2': 0.80,   't_MMI': 1.65},
        "SA(3.0)": {'a1':  3.81,  'b1': 1.17,
                    'a2':  1.99,  'b2': 3.01,
                    'σ1':  0.95,  'σ2': 0.95,   't_MMI': 0.99},                                        
                }

    # Return result
    return supported_imts, constants, conversions


# -------------------------------------------------------------------------
# Simplified GMICE (MMI = a + b log Y)
# -------------------------------------------------------------------------


def PanjamaniEtAl2016():
    """
    Panjamani, Anbazhagan, Ketan Bajaj, Sayed SR Moustafa, and Nassir SN Al‐Arifi.
    "Relationship between intensity and recorded ground‐motion and spectral
    parameters for the Himalayan region." Bulletin of the Seismological Society of
    America 106, no. 4 (2016): 1672-1689.

    Simplified Predictive Equations:

    MMI = a + b log(Y)
    """

    # Supported IMTs
    supported_imts = ["PGA" ,"PGV", "SA(0.3)", "SA(1.0)", "SA(2.0)", "SA(3.0)"]

    # Conversion from units to g
    conversions = dict.fromkeys(["acceleration", "velocity"])
    conversions["acceleration"] = (1./9.81) * (1./100.) # cm/s^2 to g
    conversions["velocity"] = 1. # cm/s to cm/s

    # Constants:
    constants = {
        "PGA": {'a': 0.142, 'b': 3.233, 'σ': 0.52},
        "PGV": {'a': 3.422, 'b': 2.679, 'σ': 0.52},
        "SA(0.3)": {'a': 0.045, 'b': 2.846, 'σ': 0.56},
        "SA(1.0)": {'a': 1.765, 'b': 2.713, 'σ': 0.58},
        "SA(2.0)": {'a': 2.713, 'b': 2.152, 'σ': 0.62},
        "SA(3.0)": {'a': 3.589, 'b': 2.447, 'σ': 0.65},
    }

    # Return result
    return supported_imts, constants, conversions


def CataldiEtAl2021():
    """
    Cataldi, Laura, Lara Tiberi, and Giovanni Costa. "Estimation of MCS intensity
    for Italy from high quality accelerometric data, using GMICEs and Gaussian
    Naïve Bayes Classifiers." Bulletin of Earthquake Engineering 19 (2021): 2325-2342.

    Simplified Predictive Equations:

    MMI = a + b log(Y)
    """

    # Supported IMTs
    supported_imts = ["PGA" ,"PGV", "SA(0.3)", "SA(1.0)", "SA(3.0)"]

    # Conversion from units to g
    conversions = dict.fromkeys(["acceleration", "velocity"])
    conversions["acceleration"] = (1./9.81) * (1./100.) # cm/s^2 to g
    conversions["velocity"] = 1. # cm/s to cm/s

    # Constants:
    constants = {
        "PGA": {'a': 1.32, 'b': 2.33, 'σ': 0.49},
        "PGV": {'a': 4.96, 'b': 2.65, 'σ': 0.47},
        "SA(0.3)": {'a': 0.65, 'b': 2.69, 'σ': 0.73},
        "SA(1.0)": {'a': 2.41, 'b': 2.41, 'σ': 0.64},
        "SA(3.0)": {'a': 2.31, 'b': 2.31, 'σ': 0.74},
    }

    # Return result
    return supported_imts, constants, conversions


def TianEtAl2021():
    """
    Tian, Xiufeng, Zengping Wen, Weidong Zhang, and Jie Yuan. "New ground
    motion to intensity conversion equations for china." Shock and Vibration
    2021 (2021): 1-21.

    Simplified Predictive Equations:

    MMI = a + b log(Y)
    """

    # Supported IMTs
    supported_imts = ["PGA" ,"PGV", "SA(0.3)", "SA(1.0)", "SA(2.0)", "SA(3.0)"]

    # Conversion from units to g
    conversions = dict.fromkeys(["acceleration", "velocity"])
    conversions["acceleration"] = (1./9.81) * (1./100.) # cm/s^2 to g
    conversions["velocity"] = 1. # cm/s to cm/s

    # Constants: NOTE: TianEtAl2021 provides coefficients in opposite order
    constants = {
        "PGA": {'b': 2.906, 'a': 0.554, 'σ': 0.6069},
        "PGV": {'b': 3.310, 'a': 3.233, 'σ': 0.6749},
        "SA(0.3)": {'b': 2.873, 'a': -0.327, 'σ': 0.6140},
        "SA(1.0)": {'b': 3.065, 'a':  0.540, 'σ': 0.7027},
        "SA(2.0)": {'b': 4.082, 'a': -0.152, 'σ': 1.0265},
        "SA(3.0)": {'b': 4.062, 'a':  0.817, 'σ': 1.0118},
    }

    # Return result
    return supported_imts, constants, conversions


def AhmadzadehEtAl2020():
    """
    Ahmadzadeh, Somayeh, Gholam Javan Doloei, and Hamid Zafarani. "Ground motion
    to intensity conversion equations for Iran." Pure and Applied Geophysics 177,
    no. 11 (2020): 5435-5449.

    Simplified Predictive Equations:

    MMI = a + b log(Y)
    """
    
    # Supported IMTs
    supported_imts = ["PGA" ,"PGV"]

    # Conversion from units to g
    conversions = dict.fromkeys(["acceleration", "velocity"])
    conversions["acceleration"] = (1./9.81) * (1./100.) # cm/s^2 to g
    conversions["velocity"] = 1. # cm/s to cm/s

    # Constants:
    constants = {
        "PGA": {'a': -0.58, 'b': 3.47, 'σ': 1.31},
        "PGV": {'a':  3.35, 'b': 3.31, 'σ': 1.38},
    }

    # Return result
    return supported_imts, constants, conversions
    

# -------------------------------------------------------------------------
# Main function wrapper
# -------------------------------------------------------------------------


def gmice(name, stations_df):

    # Initialize stations_out
    stations_out = stations_df.copy()
    stations_out["GMICE"] = ""
    
    # Determine relevant rows
    idx = stations_out.STATION_TYPE == "macroseismic"

    # Dispatcher
    gmice_type = {
                        "AhmadzadehEtAl2020": GenericSimpleGMICE,
                        "PanjamaniEtAl2016": GenericSimpleGMICE,
                        "TianEtAl2021": GenericSimpleGMICE,
                        "CataldiEtAl2021": GenericSimpleGMICE,
                        "CaprioEtAl2015": GenericPiecewiseGMICE,
                        "MoratalaEtAl2021": GenericPiecewiseGMICE,
                        "MontalvoArrietaEtAl2019": GenericPiecewiseGMICE,
                        "WordenEtAl2012": GenericPiecewiseGMICE,
                        }
    gmice_dispatcher = {
                        "AhmadzadehEtAl2020": AhmadzadehEtAl2020,
                        "PanjamaniEtAl2016": PanjamaniEtAl2016,
                        "TianEtAl2021": TianEtAl2021,
                        "CataldiEtAl2021": CataldiEtAl2021,
                        "CaprioEtAl2015": CaprioEtAl2015,
                        "MoratalaEtAl2021": MoratalaEtAl2021,
                        "MontalvoArrietaEtAl2019": MontalvoArrietaEtAl2019,
                        "WordenEtAl2012": WordenEtAl2012,
                        }
    supported_gmice = list(gmice_dispatcher.keys())
    assert (name in supported_gmice), f"{name} not yet implemented; try {supported_gmice}"

    # Call relevant GMICE
    supported_imts, constants, conversions = gmice_dispatcher[name]()
    new_values = gmice_type[name](stations_out[idx], supported_imts, constants, conversions)
    new_values["GMICE"] = name

    # Overwrite cells
    col_overwrite = new_values.columns
    stations_out.loc[idx, col_overwrite] = new_values
    stations_out["REFERENCES"] = stations_out["REFERENCES"].astype(str) + f"_{name}"
    
    # Return result
    return stations_out, supported_imts

