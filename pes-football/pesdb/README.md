# Introduction

This project provides some useful tools for pes-football players.

# Dataset

Data is crawled from [pesdb](http://www.pesdb.net) and is pre-processed and saved in ``data/``.

Players have been exported from PES 2019 (Data Pack 5.00).

# Usage

## 1. Compare player at any level

If you want to compare L. SANE at level 30 and S. MANE at level 40, run...

``` python
python compare_player.py SANE 30 MANE 40
```

If given level exceeds the max-level of the player, max-level will be used in the comparison.

You don't have to give exact names of players. Lacking given name, upper or lower case are all fine, my code will find the most similar one in the dataset. 

``` python
python compare_player.py sane 30 mane 30
python compare_player.py l.sane 30 s.mane 30
```

## 2. Search scouts

Search 100% scouts combinations given player name or/and existing scouts. 

Combinations that need only two scouts will be listed on top.

**Note** that only 5-star scouts are supported.

### 2.1 Search by player name

If you want Messi, 

``` python
python smart_scout.py -p messi | head -10
```

### 2.2 Search by existing scouts

If you already have a ``SS`` scout and a ``30+`` scout, run... 

``` python
python smart_scout.py -s SS#30+
```

will give you all possible players.

### 2.3 Search by player name and existing scouts

If you want Messi and fortunately already have a ``SS`` scout and a ``30+`` scout, run... 

``` python
python smart_scout.py -p messi -s SS#30+
```

will give you all possible players.


## 3. Find similar players

Find top 10 similar players with the given one according to players' abilities. Similarity is calculated by followings steps:

 - Treat player's ability as a vector
 - Apply PCA to reduce dimensions of ability vector
 - Use cosine to calculate similarity


``` python
python similar_player.py messi

--------------------L. MESSI--------------------
idx  ratings(30)  similarity  name
 1       88          0.993    P. DYBALA
 2       88          0.987    P. COUTINHO
 3       85          0.986    F. THAUVIN
 4       94          0.983    NEYMAR
 5       86          0.976    D. MERTENS
 6       86          0.971    N. FEKIR
 7       88          0.968    M. REUS
 8       90          0.963    E. HAZARD
 9       90          0.959    A. GRIEZMANN
10       84          0.956    F. BERNARDESCHI
```

The results are shown as above. It really make sense that P. DYBALA and P. COUTINHO are very similar to L. MESSI.