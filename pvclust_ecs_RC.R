library(pvclust)
mydata <- read.table("/homes/saketc/research2/saket/BLAST/machine_learning/allchanges_RC_for_orangemod.tab",sep='\t',header=T)
rownames(mydata) <- mydata[,1]; mydata <- as.matrix(mydata[,-1]) 
pv <- pvclust(scale(t(mydata)), method.dist="canberra", method.hclust="ward", nboot=1000) # Perform the hierarchical cluster analysis
pdf('ec6_all_changes_RC.pdf',height=6,width=50)
plot(pv, hang=-1,cex=0.56,cex.pv=0.4); pvrect(pv, alpha=0.95) # Plots result as a dendrogram where the significant clusters are highlighted with red rectangles.
dev.off()

clsig <- pvpick(pv, alpha=0.95, pv="au", type="geq", max.only=TRUE) # Retrieve members of significant clusters.
clusters <- clsig$clusters
