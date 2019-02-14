""" This script calculates ratios and plots from simulated power spectral data where parameter(s) vary."""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from fooof import FOOOF, FOOOFGroup

from ratios import *
from settings import *

def main():

    ###################### CENTER FREQUENCY ######################
    # Load data
    cf_low = np.load("../dat/cf_data_low.npy")
    cf_high = np.load("../dat/cf_data_high.npy")

    # Gather center frequency values iterated across for both low and high band
    cf_low_syns = []
    cf_high_syns = []

    for val in cf_low[2]:
        cf_low_syns.append(val.gaussian_params[0][0])
    for val in cf_high[2]:
        cf_high_syns.append(val.gaussian_params[0][0])

    # Calculate ratios
    cf_low_ratios = []
    cf_high_ratios = []

    for cf in cf_low[1]:
        cf_low_ratios.append(calc_band_ratio(cf_low[0], cf, THETA_BAND, BETA_BAND))

    for cf in cf_high[1]:
        cf_high_ratios.append(calc_band_ratio(cf_high[0], cf, THETA_BAND, BETA_BAND))

    # Make DataFrame of Center Frequencies and coresponding ratio values
    df_cf_low_cols = np.array([cf_low_ratios, cf_low_syns]).T.tolist()
    df_cf_high_cols = np.array([cf_high_ratios, cf_high_syns]).T.tolist()

    df_cf_low = pd.DataFrame(df_cf_low_cols, columns=["Band_Ratio", "Low_Center_Frequency"])
    df_cf_high = pd.DataFrame(df_cf_high_cols, columns=["Band_Ratio", "High_Center_Frequency"])

    # Subplots - define the figure
    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Low Center Freq")
    ax[1].set_xlabel("High Center Freq")
    ax[0].set_ylabel("Band Ratio")
    ax[1].set_ylabel("Band Ratio")

    # Fill in axes
    ax[0].plot(df_cf_low.Low_Center_Frequency, df_cf_low.Band_Ratio, color='r')
    ax[1].plot(df_cf_high.High_Center_Frequency, df_cf_high.Band_Ratio, color='r')

    plt.savefig("../figures/cf_vs_bandratio.pdf")

    ###################### Amplitude ######################

    # Load data
    amp_low = np.load("./dat/amp_data_low.npy")
    amp_high = np.load("./dat/amp_data_high.npy")

    # Gather Amplitude vales
    amp_low_syns = []
    amp_high_syns = []

    for val in amp_low[2]:
        amp_low_syns.append(val.gaussian_params[0][1])
    for val in amp_high[2]:
        amp_high_syns.append(val.gaussian_params[0][1])

    # Calculate band ratios
    amp_low_ratios = []
    amp_high_ratios = []

    for amp in amp_low[1]:
        amp_low_ratios.append(calc_band_ratio(amp_low[0], amp, THETA_BAND, BETA_BAND))

    for amp in amp_high[1]:
        amp_high_ratios.append(calc_band_ratio(amp_high[0], amp, THETA_BAND, BETA_BAND))

    # Create DataFrame
    df_amp_low_cols = np.array([amp_low_ratios, amp_low_syns]).T.tolist()
    df_amp_high_cols = np.array([amp_high_ratios, amp_high_syns]).T.tolist()

    df_amp_low = pd.DataFrame(df_amp_low_cols, columns=["Band_Ratio", "Low_Amplitude"])
    df_amp_high = pd.DataFrame(df_amp_high_cols, columns=["Band_Ratio", "High_Amplitude"])

    # Subplots - define the figure
    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Low_Amplitude")
    ax[1].set_xlabel("High_Amplitude")
    ax[0].set_ylabel("Band_Ratio")
    ax[1].set_ylabel("Band_Ratio")

    # Fill in axes
    ax[0].plot(df_amp_low.Low_Amplitude, df_amp_low.Band_Ratio, color='r')
    ax[1].plot(df_amp_high.High_Amplitude, df_amp_high.Band_Ratio, color='r')

    plt.savefig("../figures/amp_vs_bandratio.pdf")

    ###################### BAND WIDTH ######################

    bw_low = np.load("./dat/bw_data_low.npy")
    bw_high = np.load("./dat/bw_data_high.npy")

    bw_low_syns = []
    bw_high_syns = []

    for val in bw_low[2]:
        bw_low_syns.append(val.gaussian_params[0][2])
    for val in bw_high[2]:
        bw_high_syns.append(val.gaussian_params[0][2])

    bw_low_ratios = []
    bw_high_ratios = []

    for bw in bw_low[1]:
        bw_low_ratios.append(calc_band_ratio(bw_low[0], bw, THETA_BAND, BETA_BAND))

    for bw in bw_high[1]:
        bw_high_ratios.append(calc_band_ratio(bw_high[0], bw, THETA_BAND, BETA_BAND))

    df_bw_low_cols = np.array([bw_low_ratios, bw_low_syns]).T.tolist()
    df_bw_high_cols = np.array([bw_high_ratios, bw_high_syns]).T.tolist()

    df_bw_low = pd.DataFrame(df_bw_low_cols, columns=["Band_Ratio", "Low_BandWidth"])
    df_bw_high = pd.DataFrame(df_bw_high_cols, columns=["Band_Ratio", "High_BandWidth"])

    # Subplots - define the figure
    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Low_Band_Width")
    ax[1].set_xlabel("high_Band_Width")
    ax[0].set_ylabel("Band_Ratio")
    ax[1].set_ylabel("Band_Ratio")

    ax[0].plot(df_bw_low.Low_BandWidth, df_bw_low.Band_Ratio, color='r')
    ax[1].plot(df_bw_high.High_BandWidth, df_bw_high.Band_Ratio, color='r')

    plt.savefig("../figures/bw_vs_bandratio.pdf")

    ###################### Aperiodic Component ######################

    slope = np.load("./dat/slope_data.npy")

    slope_syns = []

    for val in slope[2]:
        slope_syns.append(val.background_params[1])

    slope_ratios = []

    for sl in slope[1]:
        slope_ratios.append(calc_band_ratio(slope[0], sl, THETA_BAND, BETA_BAND))

    slope_cols = np.array([slope_ratios, slope_syns]).T.tolist()

    df_slope = pd.DataFrame(slope_cols, columns=["Band_Ratio", "Slope"])

    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Slope_Value")
    ax[1].set_xlabel("Slope_Value")
    ax[0].set_ylabel("Band_Ratio")
    ax[1].set_ylabel("Band_Ratio")

    # LOG SCALING
    ax[0].set_yscale('log')
    #ax[0].set_xscale('log')

    ax[0].plot(df_slope.Slope, df_slope.Band_Ratio, color='r')
    ax[1].plot(df_slope.Slope, df_slope.Band_Ratio, color='r')

    plt.savefig("../figures/apc_vs_bandratio.pdf")

    ###################### ROTATION ######################

    # ALL OF THIS IS BROKEN!!!

#     rot = np.load("./dat/rot_data.npy")
#     rot_freqs = [ rot[0][0][0], rot[0][0][-1]]

#     rot_ratio_diff = []

#     freqs, ps = gen_power_spectrum(rot_freqs, [0,1],[])

#     control_ratio = calc_band_ratio(freqs, ps, THETA_BAND, BETA_BAND)
#     control_ratio

#     for rt in rot:
#         #print(set(rt[1]))
#         altered_ratio = calc_band_ratio(rt[0], rt[2], THETA_BAND, BETA_BAND)
#         print(altered_ratio)
#         rot_ratio_diff.append(control_ratio - altered_ratio)

#     rot_ratio_diff

    ######################################################
    ################### Relative Power ###################
    ######################################################


    ###################### RELATIVE CENTER FREQUENCY ######################

    rel_t_ps_cf_low = calc_group_relative_power(cf_low[0], cf_low[1], THETA_BAND)
    rel_b_ps_cf_low = calc_group_relative_power(cf_low[0], cf_low[1], BETA_BAND)

    rel_t_ps_cf_high = calc_group_relative_power(cf_high[0], cf_high[1], THETA_BAND)
    rel_b_ps_cf_high = calc_group_relative_power(cf_high[0], cf_high[1], BETA_BAND)

    cf_r_ratios_low = calc_group_rel_ratios(rel_t_ps_cf_low, rel_b_ps_cf_low)
    cf_r_ratios_high = calc_group_rel_ratios(rel_t_ps_cf_high, rel_b_ps_cf_high)

    # Make DataFrame of Center Frequencies and coresponding ratio values
    df_cf_low_cols = np.array([cf_r_ratios_low, cf_low_syns]).T.tolist()
    df_cf_high_cols = np.array([cf_r_ratios_high, cf_high_syns]).T.tolist()

    df_cf_low = pd.DataFrame(df_cf_low_cols, columns=["Relative_Ratio", "Low_Center_Frequency"])
    df_cf_high = pd.DataFrame(df_cf_high_cols, columns=["Relative_Ratio", "High_Center_Frequency"])

    # Subplots - define the figure
    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Low_Center_Freq")
    ax[1].set_xlabel("High_Center_Freq")
    ax[0].set_ylabel("Band_Ratio")
    ax[1].set_ylabel("Band_Ratio")

    # Fill in axes
    ax[0].plot(df_cf_low.Low_Center_Frequency, df_cf_low.Relative_Ratio, color='r')
    ax[1].plot(df_cf_high.High_Center_Frequency, df_cf_high.Relative_Ratio, color='r')

    plt.savefig("../figures/rel_cf_vs_bandratio.pdf")
    ###################### RELATIVE AMPLITUDE ######################

    rel_t_ps_amp_low = calc_group_relative_power(amp_low[0], amp_low[1], THETA_BAND)
    rel_b_ps_amp_low = calc_group_relative_power(amp_low[0], amp_low[1], BETA_BAND)

    rel_t_ps_amp_high = calc_group_relative_power(amp_high[0], amp_high[1], THETA_BAND)
    rel_b_ps_amp_high = calc_group_relative_power(amp_high[0], amp_high[1], BETA_BAND)

    amp_r_ratios_low = calc_group_rel_ratios(rel_t_ps_amp_low, rel_b_ps_amp_low)
    amp_r_ratios_high = calc_group_rel_ratios(rel_t_ps_amp_high, rel_b_ps_amp_high)

    # Create DataFrame
    df_amp_low_cols = np.array([amp_r_ratios_low, amp_low_syns]).T.tolist()
    df_amp_high_cols = np.array([amp_r_ratios_high, amp_high_syns]).T.tolist()

    df_amp_low = pd.DataFrame(df_amp_low_cols, columns=["Relative_Ratio", "Low_Amplitude"])
    df_amp_high = pd.DataFrame(df_amp_high_cols, columns=["Relative_Ratio", "High_Amplitude"])

    # Subplots - define the figure
    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Low_Amplitude")
    ax[1].set_xlabel("High_Amplitude")
    ax[0].set_ylabel("Band_Ratio")
    ax[1].set_ylabel("Band_Ratio")

    # Fill in axes
    ax[0].plot(df_amp_low.Low_Amplitude, df_amp_low.Relative_Ratio, color='r')
    ax[1].plot(df_amp_high.High_Amplitude, df_amp_high.Relative_Ratio, color='r')

    plt.savefig("../figures/rel_amp_vs_bandratio.pdf")

    ###################### RELATIVE BAND WIDTH ######################

    bw_low = np.load("./dat/bw_data_low.npy")
    bw_high = np.load("./dat/bw_data_high.npy")

    rel_t_ps_bw_low = calc_group_relative_power(bw_low[0], bw_low[1], THETA_BAND)
    rel_b_ps_bw_low = calc_group_relative_power(bw_low[0], bw_low[1], BETA_BAND)

    rel_t_ps_bw_high = calc_group_relative_power(bw_high[0], bw_high[1], THETA_BAND)
    rel_b_ps_bw_high = calc_group_relative_power(bw_high[0], bw_high[1], BETA_BAND)

    bw_r_ratios_low = calc_group_rel_ratios(rel_t_ps_bw_low, rel_b_ps_bw_low)
    bw_r_ratios_high = calc_group_rel_ratios(rel_t_ps_bw_high, rel_b_ps_bw_high)

    df_bw_low_cols = np.array([bw_r_ratios_low, bw_low_syns]).T.tolist()
    df_bw_high_cols = np.array([bw_r_ratios_high, bw_high_syns]).T.tolist()

    df_bw_low = pd.DataFrame(df_bw_low_cols, columns=["Relative_Ratio", "Low_BandWidth"])
    df_bw_high = pd.DataFrame(df_bw_high_cols, columns=["Relative_Ratio", "High_BandWidth"])

    # Subplots - define the figure
    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Low_Band_Width")
    ax[1].set_xlabel("High_Band_Width")
    ax[0].set_ylabel("Relative_Ratio")
    ax[1].set_ylabel("Relative_Ratio")

    ax[0].plot(df_bw_low.Low_BandWidth, df_bw_low.Relative_Ratio, color='r')
    ax[1].plot(df_bw_high.High_BandWidth, df_bw_high.Relative_Ratio, color='r')

    plt.savefig("../figures/rel_bw_vs_bandratio.pdf")

    ###################### RELATIVE APERIODIC COMPONENT ######################

    slope = np.load("./dat/slope_data.npy")

    rel_t_ps_sl = calc_group_relative_power(slope[0], slope[1], THETA_BAND)
    rel_b_ps_sl = calc_group_relative_power(slope[0], slope[1], BETA_BAND)

    slope_r_ratios_low = calc_group_rel_ratios(rel_t_ps_sl, rel_b_ps_sl)

    slope_cols = np.array([slope_r_ratios_low, slope_syns]).T.tolist()

    df_slope = pd.DataFrame(slope_cols, columns=["Relative_Ratio", "Slope"])

    fig, ax = plt.subplots(2, 1, figsize=[6, 7])

    ax[0].set_xlabel("Slope_Value")
    ax[1].set_xlabel("Slope_Value")
    ax[0].set_ylabel("Relative_Ratio_Log")
    ax[1].set_ylabel("Relative_Ratio")

    # LOG SCALING
    ax[0].set_yscale('log')
    #ax[0].set_xscale('log')

    ax[0].plot(df_slope.Slope, df_slope.Relative_Ratio, color='r')
    ax[1].plot(df_slope.Slope, df_slope.Relative_Ratio, color='r')

    plt.savefig("../figures/rel_apc_vs_bandratio.pdf")

if __name__ == "__main__":
    main()
    