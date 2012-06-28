allchangesdata <- data.frame("ec_clustering_tree.txtx",header=T,row.names=1,sep='\t')
Vstem <- Venn(allchangesdata)
Vstem6 <- Vstem[,"EC1","EC2","EC3","EC4","EC5","EC6"]
jpeg('ec_123456.jpg')
plot(Vstem6,doWeights=False)
dev.off()
