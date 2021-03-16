import numpy as np
import pandas as pd
import statistics
import pandas as pd
import numpy as np
import scipy.stats
import statsmodels.stats.multitest
import operator
# from scipy import stats

#Functions for Figures 1 and 2
def find_mean(all_rep_slope, cells, deviation, slope):
    cells_df = all_rep_slope.loc[all_rep_slope["cells"]== cells]
    dev_df = cells_df.loc[cells_df["deviation"]==deviation]
    cell_df = dev_df.loc[dev_df["cells"]==cells]
    #make new df with info
    df = pd.DataFrame(columns=["mean_accuracy", "dev_accuracy", "deviation", "slope", "cells"])
    #find mean_accuracy and standard deviation
    mean = cell_df["accuracy"].mean()
    dev = cell_df["accuracy"].std()
    row = [mean, dev, deviation, slope, cells]
    df.loc[len(df)] = row
    return(df)
def group_by_slope(all_reps, slope):
    #cell 7
    dev0 = find_mean(all_reps, 7, 0, slope)
    dev0p25 = find_mean(all_reps, 7, .25, slope)
    dev0p5 = find_mean(all_reps, 7, .5, slope)
    dev0p7 = find_mean(all_reps, 7, .7, slope)
    dev1 = find_mean(all_reps, 7, 1, slope)

    cells_7 = pd.concat([dev0,dev0p25,dev0p5,dev0p7,dev1])
    cells_7

    #cell 16
    dev0 = find_mean(all_reps, 16, 0, slope)
    dev0p25 = find_mean(all_reps, 16, .25, slope)
    dev0p5 = find_mean(all_reps, 16, .5, slope)
    dev0p7 = find_mean(all_reps, 16, .7, slope)
    dev1 = find_mean(all_reps, 16, 1, slope)

    cells_16 = pd.concat([dev0,dev0p25,dev0p5,dev0p7,dev1])
    cells_16

    #cell 20
    dev0 = find_mean(all_reps, 20, 0, slope)
    dev0p25 = find_mean(all_reps, 20, .25, slope)
    dev0p5 = find_mean(all_reps, 20, .5, slope)
    dev0p7 = find_mean(all_reps, 20, .7, slope)
    dev1 = find_mean(all_reps, 20, 1, slope)

    cells_20 = pd.concat([dev0,dev0p25,dev0p5,dev0p7,dev1])
    cells_20

    #cell 30
    dev0 = find_mean(all_reps, 30, 0, slope)
    dev0p25 = find_mean(all_reps, 30, .25, slope)
    dev0p5 = find_mean(all_reps, 30, .5, slope)
    dev0p7 = find_mean(all_reps, 30, .7, slope)
    dev1 = find_mean(all_reps, 30, 1, slope)

    cells_30 = pd.concat([dev0,dev0p25,dev0p5,dev0p7,dev1])
    cells_30

    #cell 100
    dev0 = find_mean(all_reps, 100, 0, slope)
    dev0p25 = find_mean(all_reps, 100, .25, slope)
    dev0p5 = find_mean(all_reps, 100, .5, slope)
    dev0p7 = find_mean(all_reps, 100, .7, slope)
    dev1 = find_mean(all_reps, 100, 1, slope)

    cells_100 = pd.concat([dev0,dev0p25,dev0p5,dev0p7,dev1])
    cells_100

    all_cells = pd.concat([cells_7,cells_16,cells_20,cells_30,cells_100])
    return(all_cells)

#Functions for Figures 3A and 3B
def find_mean_fig3(slope_df, cells, slope_over_var):
    cell_df = slope_df.loc[slope_df["cells"]== cells]
    #make new df with info
    df = pd.DataFrame(columns=["mean_accuracy", "deviation", "cells", "slope_over_var"])
    mean = cell_df["accuracy"].mean()
    dev = cell_df["accuracy"].std()

    row = [mean, dev, cells, slope_over_var]
    df.loc[len(df)] = row
    return(df)
def get_rep(sv, FP=False):
    if FP==True:
        rep1 = pd.read_csv("data/Fig3B/"+sv+"/rep1")
        rep2 = pd.read_csv("data/Fig3B/"+sv+"/rep2")
        rep3 = pd.read_csv("data/Fig3B/"+sv+"/rep3")
        rep4 = pd.read_csv("data/Fig3B/"+sv+"/rep4")
        rep5 = pd.read_csv("data/Fig3B/"+sv+"/rep5")
        rep6 = pd.read_csv("data/Fig3B/"+sv+"/rep6")
        rep7 = pd.read_csv("data/Fig3B/"+sv+"/rep7")
        rep8 = pd.read_csv("data/Fig3B/"+sv+"/rep8")
        rep9 = pd.read_csv("data/Fig3B/"+sv+"/rep9")
        rep10 = pd.read_csv("data/Fig3B/"+sv+"/rep10")
    else:
        rep1 = pd.read_csv("data/Fig3A/"+sv+"/rep1")
        rep2 = pd.read_csv("data/Fig3A/"+sv+"/rep2")
        rep3 = pd.read_csv("data/Fig3A/"+sv+"/rep3")
        rep4 = pd.read_csv("data/Fig3A/"+sv+"/rep4")
        rep5 = pd.read_csv("data/Fig3A/"+sv+"/rep5")
        rep6 = pd.read_csv("data/Fig3A/"+sv+"/rep6")
        rep7 = pd.read_csv("data/Fig3A/"+sv+"/rep7")
        rep8 = pd.read_csv("data/Fig3A/"+sv+"/rep8")
        rep9 = pd.read_csv("data/Fig3A/"+sv+"/rep9")
        rep10 = pd.read_csv("data/Fig3A/"+sv+"/rep10")

    all_reps_0p5 = pd.concat([rep1, rep2, rep3, rep4, rep5, rep6,
                              rep7,  rep8,  rep9,  rep10])
    return(all_reps_0p5)
def wrap_ttest(df, label_column, comparison_columns=None, alpha=.05, equal_var=True, return_all=False, correction_method='bonferroni', mincount=3, pval_return_corrected=True):
    try:
        '''Verify precondition that label column exists and has exactly 2 unique values'''
        label_values = df[label_column].unique()
        if len(label_values) != 2:
            print("Incorrectly Formatted Dataframe! Label column must have exactly 2 unique values.")
            return None

        '''Partition dataframe into two sets, one for each of the two unique values from the label column'''
        partition1 = df.loc[df[label_column] == label_values[0]]
        partition2 = df.loc[df[label_column] == label_values[1]]

        '''If no comparison columns specified, use all columns except the specified labed column'''
        if not comparison_columns:
            comparison_columns = list(df.columns)
            comparison_columns.remove(label_column)

        '''Determine the number of real valued columns on which we will do t-tests'''
        number_of_comparisons = len(comparison_columns)

        '''Store comparisons and p-values in two arrays'''
        comparisons = []
        pvals = []

        '''Loop through each comparison column, perform the t-test, and record the p-val'''

        for column in comparison_columns:
            if len(partition1[column].dropna(axis=0)) <= mincount:
                continue
            elif len(partition2[column].dropna(axis=0)) <= mincount:
                continue
            else:
                stat, pval = scipy.stats.ttest_ind(
                    a=partition1[column].dropna(axis=0),
                    b=partition2[column].dropna(axis=0),
                    equal_var=equal_var
                )

                comparisons.append(column)
                pvals.append(pval)
#         import pdb;pdb.set_trace()
        if len(pvals) == 0: # None of the groups had enough members to pass the mincount
            raise InvalidParameterError("No groups had enough members to pass mincount; no tests run.")

        '''Correct for multiple testing to determine if each comparison meets the new cutoff'''
        results = statsmodels.stats.multitest.multipletests(pvals=pvals, alpha=alpha, method=correction_method)
        reject = results[0]

        '''Format results in a pandas dataframe'''
        results_df = pd.DataFrame(columns=['Comparison','P_Value'])

        '''If return all, add all comparisons and p-values to dataframe'''
        if return_all:
            if pval_return_corrected:
                results_df['Comparison'] = comparisons
                results_df['P_Value'] = results[1]

            else:
                results_df['Comparison'] = comparisons
                results_df['P_Value'] = pvals

            '''Else only add significant comparisons'''
        else:
            for i in range(0, len(reject)):
                if reject[i]:
                    if pval_return_corrected:
                        results_df = results_df.append({'Comparison':comparisons[i],'P_Value':results[1][i]}, ignore_index=True)
                    else:
                        results_df = results_df.append({'Comparison':comparisons[i],'P_Value':pvals[i]}, ignore_index=True)


        '''Sort dataframe by ascending p-value'''
        results_df = results_df.sort_values(by='P_Value', ascending=True)
        results_df = results_df.reset_index(drop=True)

        '''If results df is not empty, return it, else return None'''
        if len(results_df) > 0:
            return results_df
        else:
            return None


    except:
        print("Incorrectly Formatted Dataframe!")
        return None

#Functions for supplemental fig 3
def make_sv_col(row):
    slope = row["slope"]
    dev = row["deviation"]
    sv = str(slope)+"/"+str(dev)
    return sv

def parse_fig1(slope):
    if slope==0.5:
        file_name = "slope0p5"
    elif slope==1:
        file_name = "slope1"
    elif slope==2:
        file_name = "slope2"
    elif slope==4:
        file_name = "slope4"
    else:
        return("Enter a valid slope")
    #Read in Data
    rep1 = pd.read_csv("data/Fig1/rep1/"+file_name)
    rep2 = pd.read_csv("data/Fig1/rep2/"+file_name)
    rep3 = pd.read_csv("data/Fig1/rep3/"+file_name)
    rep4 = pd.read_csv("data/Fig1/rep4/"+file_name)
    rep5 = pd.read_csv("data/Fig1/rep5/"+file_name)
    rep6 = pd.read_csv("data/Fig1/rep6/"+file_name)
    rep7 = pd.read_csv("data/Fig1/rep7/"+file_name)
    rep8 = pd.read_csv("data/Fig1/rep8/"+file_name)
    rep9 = pd.read_csv("data/Fig1/rep9/"+file_name)
    rep10 = pd.read_csv("data/Fig1/rep10/"+file_name)

    #comebine all reps
    all_reps = pd.concat([rep1,rep2,rep3,rep4,rep5,rep6,rep7,rep8,rep8,rep10])

    #find mean accuracy and groups by slope
    slope_mean = group_by_slope(all_reps, slope)
    slope_mean.reset_index(drop=True, inplace=True)
    return(slope_mean)

def parse_fig2(slope):
    if slope==0.5:
        file_name = "slope0p5"
    elif slope==1:
        file_name = "slope1"
    elif slope==2:
        file_name = "slope2"
    elif slope==4:
        file_name = "slope4"
    else:
        return("Enter a valid slope")

    #Read in Data
    rep1 = pd.read_csv("data/Fig2/rep1/"+file_name)
    rep2 = pd.read_csv("data/Fig2/rep2/"+file_name)
    rep3 = pd.read_csv("data/Fig2/rep3/"+file_name)
    rep4 = pd.read_csv("data/Fig2/rep4/"+file_name)
    rep5 = pd.read_csv("data/Fig2/rep5/"+file_name)
    rep6 = pd.read_csv("data/Fig2/rep6/"+file_name)
    rep7 = pd.read_csv("data/Fig2/rep7/"+file_name)
    rep8 = pd.read_csv("data/Fig2/rep8/"+file_name)
    rep9 = pd.read_csv("data/Fig2/rep9/"+file_name)
    rep10 = pd.read_csv("data/Fig2/rep10/"+file_name)

    #comebine all reps
    all_reps = pd.concat([rep1,rep2,rep3,rep4,rep5,rep6,rep7,rep8,rep8,rep10])

    #find mean accuracy and groups by slope
    slope_mean = group_by_slope(all_reps, slope)
    slope_mean.reset_index(drop=True, inplace=True)

    return(slope_mean)

def parse_fig3A(cells):
    if((cells != 7) and (cells != 16) and (cells != 20) and (cells != 30) and (cells != 100)):
        print("Enter a valid cell number")
        return

    slope_var_0p5 = get_rep("slope_var_0p5")
    slope_var_0p5 = find_mean_fig3(slope_var_0p5, cells, slope_over_var=.5)

    slope_var_1 = get_rep("slope_var_1")
    slope_var_1 = find_mean_fig3(slope_var_1, cells, slope_over_var=1)

    slope_var_1p5 = get_rep("slope_var_1p5")
    slope_var_1p5 = find_mean_fig3(slope_var_1p5, cells, slope_over_var=1.5)

    slope_var_2 = get_rep("slope_var_2")
    slope_var_2 = find_mean_fig3(slope_var_2, cells, slope_over_var=2)

    slope_var_3 = get_rep("slope_var_3")
    slope_var_3 = find_mean_fig3(slope_var_3, cells, slope_over_var=3)

    slope_var_4 = get_rep("slope_var_4")
    slope_var_4 = find_mean_fig3(slope_var_4, cells, slope_over_var=4)

    slope_var_6 = get_rep("slope_var_6")
    slope_var_6 = find_mean_fig3(slope_var_6, cells, slope_over_var=6)

    df = pd.concat([slope_var_0p5,slope_var_1,slope_var_1p5,slope_var_2,slope_var_3,
                             slope_var_4, slope_var_6])
    df.reset_index(drop=True, inplace=True)
    return(df)

def parse_fig3B(cells):
    if((cells != 7) and (cells != 16) and (cells != 20) and (cells != 30) and (cells != 100)):
        print("Enter a valid cell number")
        return

    slope_var_0p5 = get_rep("slope_var_0p5", FP=True)
    slope_var_0p5 = find_mean_fig3(slope_var_0p5, cells, slope_over_var=.5)

    slope_var_1 = get_rep("slope_var_1", FP=True)
    slope_var_1 = find_mean_fig3(slope_var_1, cells, slope_over_var=1)

    slope_var_1p5 = get_rep("slope_var_1p5", FP=True)
    slope_var_1p5 = find_mean_fig3(slope_var_1p5, cells, slope_over_var=1.5)

    slope_var_2 = get_rep("slope_var_2", FP=True)
    slope_var_2 = find_mean_fig3(slope_var_2, cells, slope_over_var=2)

    slope_var_3 = get_rep("slope_var_3", FP=True)
    slope_var_3 = find_mean_fig3(slope_var_3, cells, slope_over_var=3)

    slope_var_4 = get_rep("slope_var_4", FP=True)
    slope_var_4 = find_mean_fig3(slope_var_4, cells, slope_over_var=4)

    slope_var_6 = get_rep("slope_var_6", FP=True)
    slope_var_6 = find_mean_fig3(slope_var_6, cells, slope_over_var=6)

    df = pd.concat([slope_var_0p5,slope_var_1,slope_var_1p5,slope_var_2,slope_var_3,
                             slope_var_4, slope_var_6])
    df.reset_index(drop=True, inplace=True)
    return(df)

def parse_supplemtal2():
    df = pd.read_csv("data/SupFig2/LungMap72Cell.txt", sep="\t", index_col="Uniprot_ID")

    C10_cols = ["C10-1","C10-2","C10-3","C10-4","C10-5","C10-6","C10-7","C10-8","C10-9","C10-10","C10-11", "C10-12","C10-13","C10-14","C10-15","C10-16","C10-17","C10-18","C10-19"]
    SVEC_cols = ["SVEC-1","SVEC-2","SVEC-3","SVEC-4","SVEC-5","SVEC-6","SVEC-7","SVEC-8","SVEC-9","SVEC-10","SVEC-11", "SVEC-12","SVEC-13","SVEC-14","SVEC-15","SVEC-16","SVEC-17","SVEC-18","SVEC-19", "SVEC-20"]

    df["C10_average"] = df[C10_cols].mean(axis=1)
    df["SVEC_average"] = df[SVEC_cols].mean(axis=1)

    df["C10_stdev"] = df[C10_cols].std(axis=1)
    df["SVEC_stdev"] = df[SVEC_cols].std(axis=1)


    df["C10-SVEC"] = df["C10_average"] - df["SVEC_average"]
    df["abs_C10-SVEC"] = df["C10-SVEC"].abs()

    df_plot = df[["C10_stdev", "abs_C10-SVEC"]]

    df_plot = df_plot.dropna()

    #run t-test
    df_ttest = pd.read_csv("data/SupFig2/LungMap72Cell.txt", sep="\t", index_col="Uniprot_ID")

    cols_to_keep = C10_cols + SVEC_cols
    cols_to_keep
    df_ttest = df_ttest[cols_to_keep]
    df_ttest = df_ttest.drop(df_ttest.index[[1225]])
    df_ttest = df_ttest.transpose()
    df_ttest = df_ttest.astype(float)
    df_ttest['cell_line'] = ["C"] * 19 + ["S"] * 20

    test_df = wrap_ttest(df=df_ttest, label_column="cell_line", correction_method='fdr_bh',mincount=7, pval_return_corrected=True, return_all=True)
    test_df.index=test_df["Comparison"]
    test_df=test_df.drop(columns="Comparison")
    test_df.columns=['pval']
    test_df

    final_df = pd.concat([test_df, df_plot],axis=1, join='inner')

    return(final_df)

def prase_supplemtal3(cells, sv):
    all_reps = get_rep(sv)

    all_reps["sv"] = all_reps.apply(lambda row: make_sv_col(row), axis=1)
    cell_number = all_reps[all_reps["cells"]==cells]
    return(cell_number)
