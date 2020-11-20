##Supplemental 2
library(ggplot2)
library(dplyr)
library(directlabels)
library("reticulate")
library("dplyr")

#get the data from the parser
source_python("dataParser.py")
sup2_data = parse_supplemtal2()

dir.create("figures_jpg")
jpeg("figures_jpg/supFig2.jpg", units="in", width=8, height=8, res=300)
#Supplemental Figure 2
sup2_data %>% mutate(Color = ifelse(pval < .05,"red","black")) %>%
ggplot(aes(x = C10_stdev, y = `abs_C10-SVEC`, color = Color)) +
  geom_point() +
  theme_classic(base_size = 14)+
  scale_color_identity() +
  xlim(0, 1.5)+
  ylim(0, 1.5)+
  ylab("Fold Change Between Cell Types")+
  xlab("Variation")+
  theme(axis.title.x = element_text(size=30),
        axis.title.y = element_text(size=30),
        axis.text.x = element_text(face="bold",
                                   size=14),
        axis.text.y = element_text(face="bold",
                                   size=14))+
  geom_abline(aes(intercept = 0, slope = 1), linetype=1) +
  geom_abline(aes(intercept = 0, slope = 2),linetype=2) +
  geom_abline(aes(intercept = 0, slope = 4), linetype=3)

dev.off()
