require(ggplot2)
require(scales)

#Figure 4A

myData = read.csv("data/Fig4/fig4A", row.names=1)

dir.create("figures_tiffs")
tiff("figures_tiffs/fig4A.tiff", units="in", width=8, height=10, res=300)
par(mar=c(6, 6, 6, 6))
dens <- apply(myData, 2, density)
plot(NA, xlim=range(-3,3), ylim=range(sapply(dens, "[", "y")), xlab="True S/V - Estimated S/V", ylab="Density",
     cex.lab=2.5, cex.axis=2)
mapply(lines, dens, col=1:length(dens), lwd=6)
legend("topright", legend=c("100 cells", "30 cells", "20 cells", "16 cells", "7 cells"), fill=1:length(dens),
       cex=2)

dev.off()

#Figure 4B
full_population = read.csv("data/Fig4/fig4B", row.names=1)
#drop proteins below 1
dropped = full_population[full_population$slope/full_population$sd >= 1,]

tiff("figures_tiffs/fig4B.tiff", units="in", width=5, height=5, res=300)
ggplot(dropped, aes(x = trsv)) +  
  geom_bar(aes(y = (..count..)/200)) + 
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



###GETTING NUMBERS
length(rownames(dropped))
length(rownames(full_population))
#make a histgram of the true sv
# hist(full_population$trsv)
# hist(dropped$trsv, main="Histogram of samples kept with cutoff = 1", xlab = "slope/variaion")
proteins_lost = length(rownames(full_population[full_population$trsv>=1,])) - length(rownames(dropped[dropped$trsv>=1,]))
proteins_lost
good_kept = length(rownames(dropped[dropped$trsv>=1,]))
good_kept
bad_kept = length(rownames(dropped[dropped$trsv<1,]))
bad_kept

length(rownames(dropped[dropped$trsv==0,]))*100/400
length(rownames(dropped[dropped$trsv==.5,]))*100/400
length(rownames(dropped[dropped$trsv==1,]))*100/400
length(rownames(dropped[dropped$trsv==1.5,]))*100/400
length(rownames(dropped[dropped$trsv==2,]))*100/400




