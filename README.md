# Extracting From and To lines

## xpaths

### path to utterances
//*[@id="noFear-comparison"]/table/tbody
//div[@id="noFear-comparison"]/table[@class="noFear"]/tr

### path to speaker
//*[@id="noFear-comparison"]/table/tbody/tr[2]/td[2]/b
td[@class="noFear-left"]/b/text()

### path to shakespeare
//*[@id="noFear-comparison"]/table/tbody/tr[2]/td[2]
td[@class="noFear-left"]/div[@class="original-line"]

### path to english
//*[@id="noFear-comparison"]/table/tbody/tr[2]/td[3]
td[@class="noFear-right"]/div[@class="modern-line"]

### path to next page
//*[@id="ad-skin-img"]/div/div[3]/div[1]/div[2]/div/div[1]/a[2]

### Create vocab

https://github.com/rsennrich/subword-nmt
https://github.com/EdinburghNLP/nematus

