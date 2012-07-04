library(pvclust)


hclust_methods = c("average","ward","single", "complete","mcquitty", "median","centroid")
dist_methods = c("euclidean","maximum","manhattan","canberra","binary","minkowski")
for (hm in hclust_methods){

	for (dm in dist_methods){	
		mydata <- read.table("/homes/saketc/research2/saket/BLAST/machine_learning/allchanges/all_domain_changes_for_orange-mod.tab",sep='\t',header=T)
		rownames(mydata) <- mydata[,1]; mydata <- as.matrix(mydata[,-1]) 
		pv <- pvclust(scale(t(mydata)), method.dist=dm, method.hclust=hm, nboot=1000) # Perform the hierarchical cluster analysis
		clsig <- pvpick(pv, alpha=0.95, pv="au", type="geq", max.only=TRUE) # Retrieve members of significant clusters.
		clusters <- clsig$clusters
		clsig <- pvpick(pv, alpha=0.95, pv="au", type="geq", max.only=TRUE) # Retrieve members of significant clusters.
		clusters <- clsig$clusters
		confusion_matrix <- mat.or.vec(length(clusters), 6)
		row =1
		for (i in clusters){ 
		cluster_length <- length(i)
		for (j in 1:cluster_length){
		ec <- i[j]
		ec_subclass <-as.integer(unlist(strsplit(ec, ".", fixed = TRUE))[2])
		confusion_matrix[row,ec_subclass] <- confusion_matrix[row,ec_subclass]+1

		}
		row <- row+1
		}
		print(paste("hCluster Method=",hm,"distance Method =",dm)) 
		print (confusion_matrix)
		pdf(paste('allchanges/all_domain_changes_',hm,'_',dm,'_','.pdf',sep=""),height=6,width=50)
		plot(pv, hang=-1,cex=0.56,cex.pv=0.4); pvrect(pv, alpha=0.95) # Plots result as a dendrogram where the significant clusters are highlighted with red rectangles.
		dev.off()
	}
}

