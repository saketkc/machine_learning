allchangesdata <-read.table("allchangesmod.tab",header=T,row.names=1)
allchangesdist <- dist(allchangesdata,method="canberra")
hc <- hclust(allchangesdist,method="ward")
maxheight = max(hc$height)
height_25 = 0.25*maxheight
height_50 = 0.50*maxheight
height_75 = 0.75*maxheight

ct_25 <- cutree(hc,h=height_25)
ct_50 <- cutree(hc,h=height_50)
ct_75 <- cutree(hc,h=height_75)
ct_100 <- cutree(hc,h=maxheight)
print ("#################################################################################")
for ( i in 1:length(ct_25)) {
	print (ct_25[i])
}
print ("#################################################################################")
for ( i in 1:length(ct_50)) {
	print (ct_50[i])
}
print ("#################################################################################")
for ( i in 1:length(ct_75)) {
	print (ct_75[i])
}
print ("#################################################################################")
for ( i in 1:length(maxheight)) {
	print (ct_100[i])
}



