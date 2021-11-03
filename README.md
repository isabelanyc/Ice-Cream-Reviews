<p align="center">
  <img src="./images/ben_jerry.jpeg"  width="850" height="300">
</p>

## The Customer Is Always Right! A Spoonful of Ice Cream Reviews and NLP

### Project Summary
According to the [International Dairy Foods Association](https://www.idfa.org/ice-cream-sales-trends), Americans consume pounds of ice cream per year. That is a whole lot of ice cream! It makes sense for ice cream manufacturers to care a lot about their cusomter's opinions about their flavors. This project seeks out to lend a helping hand to the ice cream industry by building a ice cream review classifier. Using NLP techniques, each review can be classified as good or bad.

In addition to applying machine learning methods to create the classifier, an exensive EDA was done to further understand which flavors people like/dislike and which brands are most popular.

### Data
The dataset used for this project comes from [Kaggle](https://www.kaggle.com/tysonpo/ice-cream-dataset). The data is broken down into 

```
| brand   | key   | author         | date       |   stars | title                             |   helpful_yes |   helpful_no | text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |   taste |   ingredients |   texture |   likes |\n|:--------|:------|:---------------|:-----------|--------:|:----------------------------------|--------------:|-------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------:|--------------:|----------:|--------:|\n| bj      | 0_bj  | Ilovebennjerry | 2017-04-15 |       3 | Not enough brownies!              |            10 |            3 | Super good, don't get me wrong. But I came for the caramel and brownies, not the sweet cream. The packaging made it seem like brownies were packed and bountiful *crying frowny emoji* I'd say the taste of this was amazing, but the ratio of brownie to sweet cream was disappointing. Liked it regardless but probably won't buy again simply because it didn't live up to its promising package. I'll find another one that has a better ratio and wayyy more yummy chewy brownies.                                                                                                                                                                                                                                                     |     nan |           nan |       nan |     nan |\n|         |       |                |            |         |                                   |               |              | Overall, good flavor, texture, idea, and brownies. Not so great caramel/sweet cream/ brownie RATIO. Just add more brownies. Please.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |         |               |           |         |\n| bj      | 0_bj  | Sweettooth909  | 2020-01-05 |       5 | I’m OBSESSED with this pint!      |             3 |            0 | I decided to try it out although I’m not a huge caramel fan, and the first buy was ok, didn’t like the caramel too much and for some reason that specific pint barely had any brownies! Like there were some on top but from the middle to the bottom? Zilch. Nada. Nothing! It was disappointing. But for some reason, I bought it again and I really do believe it was just that point bcuz the second one was glorious!! I had a big brownie chunk in EVERY bite. Plus the caramel didn’t bother me as much and I took a liking to it. Conclusion: I’m on my fifth pint, of the week and I’m going back to get my daily pint cus I’m kinda sick and need some happiness.                                                                 |     nan |           nan |       nan |     nan |\n| bj      | 0_bj  | LaTanga71      | 2018-04-26 |       3 | My favorite...More Caramel Please |             5 |            2 | My caramel core begins to disappear about half way through. I only buy this for the caramel core. The first time I purchased this I was not even aware that there were blonde bits in there. You had me a salted caramel core, well this is the fourth pint that I have purchased and the caramel is plentiful at the top then it begins to get sparse about half way down at 3/4s of the way down its gone. It works out in my husbands favor because he doesn't care for the caramel so he gets to finish my pint while having a full pint of his choice. Please please please, its called salted caramel core for a reason. Let the caramel flow through the core. P.S. You could put a little extra in there, I totally would not mind. |     nan |           nan |       nan |     nan |
```


### Project Breakdown
The main files for this project can be found under `notebooks`:

- `1_data_wrangling.ipynb`: 
   
- `2_eda.ipynb`:

- `3_preprocessing.ipynb`:

- `4_modelling.ipynb`:

### Results

```
                precision    recall  f1-score   support

         Bad       0.90      0.75      0.82      1349
        Good       0.94      0.98      0.96      5154

    accuracy                           0.93      6503
   macro avg       0.92      0.87      0.89      6503
weighted avg       0.93      0.93      0.93      6503
```

### Future Work
