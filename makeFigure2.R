library(ggplot2)
library(dplyr)
library("reticulate")
# py_install("pandas")

#get the data from the parser
source_python("dataParser.py")
slope0p5 = parse_fig2(0.5)
slope1 = parse_fig2(1)
slope2 = parse_fig2(2)
slope4 = parse_fig2(4)

plot_func = function(slope){
        par(mar=c(6, 6, 6, 6))
        legend_position = "topleft"
        ylim=c(0,0.5)
        title = paste("Slope = ", toString(slope))
        plot(cells_7$deviation, cells_7$mean_accuracy, main=title,
             xlab="Variation ", ylab="% False Positve ", pch=19, type="o",
             ylim=ylim, lty=1,
             cex.lab=2,cex.axis=1.5,cex.main=2,
             lwd = 3) 
        
        arrows(cells_7$deviation, cells_7$mean_accuracy, cells_7$deviation,cells_7$mean_accuracy+cells_7$dev_accuracy, length=0.05, angle=90)
        arrows(cells_7$deviation, cells_7$mean_accuracy, cells_7$deviation,cells_7$mean_accuracy-cells_7$dev_accuracy, length=0.05, angle=90)
        
        par(new=T)
        plot(cells_16$deviation, cells_16$mean_accuracy, pch=19, type="o", ann=F, axes=F, 
             ylim=ylim, lty=2,
             cex.lab=2,cex.axis=1.5,cex.main=2,
             lwd = 3)
        arrows(cells_16$deviation, cells_16$mean_accuracy, cells_16$deviation,cells_16$mean_accuracy+cells_16$dev_accuracy, length=0.05, angle=90)
        arrows(cells_16$deviation, cells_16$mean_accuracy, cells_16$deviation,cells_16$mean_accuracy-cells_16$dev_accuracy, length=0.05, angle=90)
        
        par(new=T)
        plot(cells_20$deviation, cells_20$mean_accuracy, pch=19, type="o", ann=F, axes=F, 
             ylim=ylim, lty=3,
             cex.lab=2,cex.axis=1.5,cex.main=2,
             lwd = 3)
        arrows(cells_20$deviation, cells_20$mean_accuracy, cells_20$deviation,cells_20$mean_accuracy+cells_20$dev_accuracy, length=0.05, angle=90)
        arrows(cells_20$deviation, cells_20$mean_accuracy, cells_20$deviation,cells_20$mean_accuracy-cells_20$dev_accuracy, length=0.05, angle=90)
        
        par(new=T)
        plot(cells_30$deviation, cells_30$mean_accuracy, pch=19, type="o", ann=F, axes=F, 
             ylim=ylim, lty=4,
             cex.lab=2,cex.axis=1.5,cex.main=2,
             lwd = 3)
        arrows(cells_30$deviation, cells_30$mean_accuracy, cells_30$deviation,cells_30$mean_accuracy+cells_30$dev_accuracy, length=0.05, angle=90)
        arrows(cells_30$deviation, cells_30$mean_accuracy, cells_30$deviation,cells_30$mean_accuracy-cells_30$dev_accuracy, length=0.05, angle=90)
        
        par(new=T)
        plot(cells_100$deviation, cells_100$mean_accuracy, pch=19, type="o", ann=F, axes=F, 
             ylim=ylim, lty=5,
             cex.lab=2,cex.axis=1.5,cex.main=2,
             lwd = 3)
        arrows(cells_100$deviation, cells_100$mean_accuracy, cells_100$deviation,cells_100$mean_accuracy+cells_100$dev_accuracy, length=0.05, angle=90)
        arrows(cells_100$deviation, cells_100$mean_accuracy, cells_100$deviation,cells_100$mean_accuracy-cells_100$dev_accuracy, length=0.05, angle=90)
        
        
        legend(legend_position, legend = c("7 cells", "16 cells", "20 cells", "30 cells", "100 cells"),
               lty = 1:5, cex = 1.5)
}


dir.create("figures_jpg")
jpeg("figures_jpg/fig2.jpg", units="in", width=15, height=15, res=300)
par(mfrow=c(2,2))

#slope == 0.5
cells_7 = slope0p5[slope0p5[, "cells"] == 7,]
cells_16 = slope0p5[slope0p5[, "cells"] == 16,]
cells_20 = slope0p5[slope0p5[, "cells"] == 20,]
cells_30 = slope0p5[slope0p5[, "cells"] == 30,]
cells_100 = slope0p5[slope0p5[, "cells"] == 100,]
plot_func(slope=0.5)


#slope == 1
cells_7 = slope1[slope1[, "cells"] == 7,]
cells_16 = slope1[slope1[, "cells"] == 16,]
cells_20 = slope1[slope1[, "cells"] == 20,]
cells_30 = slope1[slope1[, "cells"] == 30,]
cells_100 = slope1[slope1[, "cells"] == 100,]
plot_func(slope=1)


#slope == 2
cells_7 = slope2[slope2[, "cells"] == 7,]
cells_16 = slope2[slope2[, "cells"] == 16,]
cells_20 = slope2[slope2[, "cells"] == 20,]
cells_30 = slope2[slope2[, "cells"] == 30,]
cells_100 = slope2[slope2[, "cells"] == 100,]
plot_func(slope=2)


#slope == 4
cells_7 = slope4[slope4[, "cells"] == 7,]
cells_16 = slope4[slope4[, "cells"] == 16,]
cells_20 = slope4[slope4[, "cells"] == 20,]
cells_30 = slope4[slope4[, "cells"] == 30,]
cells_100 = slope4[slope4[, "cells"] == 100,]
plot_func(slope=4)



dev.off()

