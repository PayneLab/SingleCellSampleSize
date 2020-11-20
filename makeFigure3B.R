library(ggplot2)
library(dplyr)
library("reticulate")

#get the data from the parser
source_python("dataParser.py")
cells_7 = parse_fig3B(7)
cells_16 = parse_fig3B(16)
cells_20 = parse_fig3B(20)
cells_30 = parse_fig3B(30)
cells_100 = parse_fig3B(100)

dir.create("figures_tiffs")
tiff("figures_tiffs/fig3B.tiff", units="in", width=8, height=8, res=300)
par(mar=c(6, 6, 6, 6))

plot(cells_7$slope_over_var, cells_7$mean_accuracy,
     xlab="Slope Over Variation ", ylab="% False Positives ", pch=19, type="o",
     ylim=c(0,.5), lty=1, 
     cex.lab=2,cex.axis=1.5,cex.main=2, 
     lwd = 3) 

arrows(cells_7$slope_over_var, cells_7$mean_accuracy, cells_7$slope_over_var,cells_7$mean_accuracy+cells_7$deviation, length=0.05, angle=90)
arrows(cells_7$slope_over_var, cells_7$mean_accuracy, cells_7$slope_over_var,cells_7$mean_accuracy-cells_7$deviation, length=0.05, angle=90)


par(new=T)
plot(cells_16$slope_over_var, cells_16$mean_accuracy, pch=19, type="o", ann=F, axes=F, 
     ylim=c(0,.5), lty=2,lwd = 3,
     cex.lab=2,cex.axis=1.5,cex.main=2)
arrows(cells_16$slope_over_var, cells_16$mean_accuracy, cells_16$slope_over_var,cells_16$mean_accuracy+cells_16$deviation, length=0.05, angle=90)
arrows(cells_16$slope_over_var, cells_16$mean_accuracy, cells_16$slope_over_var,cells_16$mean_accuracy-cells_16$deviation, length=0.05, angle=90)


par(new=T)
plot(cells_20$slope_over_var, cells_20$mean_accuracy, pch=19, type="o", ann=F, axes=F, 
     ylim=c(0,.5), lty=3,lwd = 3,
     cex.lab=2,cex.axis=1.5,cex.main=2)
arrows(cells_20$slope_over_var, cells_20$mean_accuracy, cells_20$slope_over_var,cells_20$mean_accuracy+cells_20$deviation, length=0.05, angle=90)
arrows(cells_20$slope_over_var, cells_20$mean_accuracy, cells_20$slope_over_var,cells_20$mean_accuracy-cells_20$deviation, length=0.05, angle=90)

par(new=T)
plot(cells_30$slope_over_var, cells_30$mean_accuracy, pch=19, type="o", ann=F, axes=F, 
     ylim=c(0,.5), lty=4,lwd = 3,
     cex.lab=2,cex.axis=1.5,cex.main=2,)
arrows(cells_30$slope_over_var, cells_30$mean_accuracy, cells_30$slope_over_var,cells_30$mean_accuracy+cells_30$deviation, length=0.05, angle=90)
arrows(cells_30$slope_over_var, cells_30$mean_accuracy, cells_30$slope_over_var,cells_30$mean_accuracy-cells_30$deviation, length=0.05, angle=90)

par(new=T)
plot(cells_100$slope_over_var, cells_100$mean_accuracy, pch=19, type="o", ann=F, axes=F,
     ylim=c(0,.5), lty=5,lwd = 3,
     cex.lab=2,cex.axis=1.5,cex.main=2,)
arrows(cells_100$slope_over_var, cells_100$mean_accuracy, cells_100$slope_over_var,cells_100$mean_accuracy+cells_100$deviation, length=0.05, angle=90)
arrows(cells_100$slope_over_var, cells_100$mean_accuracy, cells_100$slope_over_var,cells_100$mean_accuracy-cells_100$deviation, length=0.05, angle=90)


legend("topright", legend = c("7 cells", "16 cells", "20 cells", "30 cells", "100 cells"),
       lty = 1:5, cex = 1.5)

dev.off()
