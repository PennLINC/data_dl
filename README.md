# abcd_dl
Downloader (and deleter) for ABCD from NDA.
This will download and subsquently delete subject data from the ABCD data on NDA. The point is to not keep data that is available publically on our own storage.

```python
import abcd_dl
abcd_dl.download(['sub-NDARINV00BD7VDC'],'/cbica/home/bertolem/abcd_dl/dl/','/cbica/home/bertolem/abcd_dl',4)

#arg 1: subject list, strings in a list
#arg 2: where should we put your data?
#arg 3: where should I keep the log? we use this to show what downloaded, and use it to delete things
#arg 4: how many cores?

#here is where you process the data, store your results

abcd_dl.delete('/cbica/home/bertolem/abcd_dl/dl/','/cbica/home/bertolem/abcd_dl') #remove files, keep directory structure
abcd_dl.delete_scary('/cbica/home/bertolem/abcd_dl/dl/') #remove all files you downloaded, including the directory structure (i.e., rm -f -r /cbica/home/bertolem/abcd_dl/dl/)
```
