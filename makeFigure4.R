require(ggplot2)
require(scales)

#####Figure 4A####

fig1_data = read.csv("data/Fig4/fig4A", row.names=1)

dir.create("figures_jpg")
jpeg("figures_jpg/fig4A.jpg", units="in", width=8, height=10, res=300)
par(mar=c(6, 6, 6, 6))
dens <- apply(fig1_data, 2, density)
plot(NA, xlim=range(-3,3), ylim=range(sapply(dens, "[", "y")), xlab="True S/V - Estimated S/V", ylab="Density",
     cex.lab=2.5, cex.axis=2)
mapply(lines, dens, col=1:length(dens), lwd=6)
legend("topright", legend=c("100 cells", "30 cells", "20 cells", "16 cells", "7 cells"), fill=1:length(dens),
       cex=2)

dev.off()

#Calculations for manuscript
sd(fig1_data$c100)
sd(fig1_data$c30)

#####Figure 4B####
full_population = read.csv("data/Fig4/fig4B", row.names=1)
#drop proteins below 1
dropped = full_population[full_population$slope/full_population$sd >= 1,]

jpeg("figures_jpg/fig4B.jpg", units="in", width=5, height=5, res=300)
ggplot(dropped, aes(x = trsv)) +  
  geom_bar(aes(y = (..count..)/1000)) + #divide by 200 because there were 200 samples taken for each trsv
  theme_classic()+
  scale_y_continuous(labels=percent)+
  xlab("True S/V") +
  ylab("Percent Kept") +
  theme(axis.title.x = element_text(size=20),
        axis.title.y = element_text(size=20),
        axis.text.x = element_text(face="bold",
                                   size=14),
        axis.text.y = element_text(face="bold",
                                   size=14))

dev.off()

##Calculations for manuscript
#how many proteins are remove usinging filtering criteria
dropped$sv = dropped$slope/dropped$sd
good_kept = dropped[dropped$trsv == 2,]
length(rownames(good_kept))/1000

