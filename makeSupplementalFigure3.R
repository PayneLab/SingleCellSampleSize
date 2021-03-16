library(ggplot2)
library(dplyr)
library("reticulate")

#get the data from the parser
source_python("dataParser.py")

df = prase_supplemtal3(cells = 7, sv="slope_var_1")
df <- subset (df, select = -`Unnamed: 0`)

dir.create("figures_jpg")
jpeg("figures_jpg/supFig3.jpg", units="in", width=8, height=8, res=300)
par(mar=c(6, 6, 6, 6))
ggplot(df, aes(x=sv, y=accuracy)) + 
  geom_boxplot(outlier.shape=NA) + #avoid plotting outliers twice
  geom_jitter(position=position_jitter(width=.1, height=0)) +
  theme_classic() +
  ylim(.5,.8) +
  ylab("Accuracy") +
  xlab("Slope Over Variation")

dev.off()

#test to see if there is a significant difference between any of the combination of S/V
aov_result = aov(df$accuracy ~ df$sv)
aov_sum = summary(aov_result)#if the pvalue is small it means at least one group has a different mean
aov_sum[[1]][["Pr(>F)"]]


#Check for all of the combinations of cells and s/v
all_cell_types = list(7,16,20,30,100)
all_sv_types = list('slope_var_0p5', "slope_var_1","slope_var_1p5","slope_var_2","slope_var_4","slope_var_6")

for(cell_type in all_cell_types){
  for(sv_type in all_sv_types){
    df = prase_fig3_rep(cells = cell_type, sv=sv_type)
    df <- subset (df, select = -`Unnamed: 0`)
    aov_result = aov(df$accuracy ~ df$sv)
    aov_result = aov(df$accuracy ~ df$sv)
    aov_sum = summary(aov_result)#if the pvalue is small it means at least one group has a different mean
    pval = unlist(aov_sum)[["Pr(>F)1"]]
    if(pval < .05){
      print("fail")
    }
  }
}


