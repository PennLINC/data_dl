# abcd_dl
downloader (and deleter) for ABCD from NDA


This will download and subsquently delete subject data from the ABCD data on NDA. 


```python
import abcd_dl
abcd_dl.download(['sub-NDARINV00BD7VDC'],'/cbica/home/bertolem/abcd_dl/dl/','/cbica/home/bertolem/abcd_dl',4)

#here is where you process the data, store your results

abcd_dl.delete('/cbica/home/bertolem/abcd_dl/dl/','/cbica/home/bertolem/abcd_dl') #remove files, keep directory structure
abcd_dl.delete_scary('/cbica/home/bertolem/abcd_dl/dl/') #remove all files you downloaded, including the directory structure (i.e., rm -f -r /cbica/home/bertolem/abcd_dl/dl/)
```
