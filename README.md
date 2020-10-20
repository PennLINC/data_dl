# data downloader for open source MRI data
This will download and subsquently delete subject data from data on NDA. The point is to not keep data that is available publically on our own storage.

```python
import data_dl
data_dl.download(['sub-NDARINV00BD7VDC'],'/cbica/home/bertolem/data_dl/dl/','/cbica/home/bertolem/data_dl','all',4)

#arg 1: subject list, strings in a list
#arg 2: where should we put your data?
#arg 3: where should I keep the log? we use this to show what downloaded, and use it to delete things
#arg 5: what data? dwi, frmi, all
#arg 5: how many cores?

#here is where you process the data, store your results

#remove files
data_dl.delete('/cbica/home/bertolem/data_dl/dl/','/cbica/home/bertolem/data_dl')
```
