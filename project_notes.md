									
<h1>QUORA QUESTION PAIR SIMILARITY PROJECT NOTES</h1>

<h3>BASICS</h3>
<li>train.csv has the data</li>
<li>features - id(int), qid1(int), qid2(int), question1(string), question2(string)</li>
<li>label - is_duplicate(int)</li>
<li>this is a binary classification problem</li>
<li>metrics used will be log loss and binary confusion matrix</li>


<h3>EDA</h3>
<li>bar chart of number of duplicate and non duplicate question pairs</li>
<li>bar chart of number of questions which are repeated and not repeated in the entire dataset</li>
<li>checking for duplicate data points in the dataset</li>
<li>log histogram of frequency of questions (i.e how many times does a single question repeats in the dataset)</li>
<li>check for null valued data points and filling the null values with empty string as mostly string data is missing</li>


<h3>FEATURE EXTRACTION</h3>
<li>freq_qid1 = Frequency of qid1's</li>
<li>freq_qid2 = Frequency of qid2's</li>
<li>q1len = Length of q1</li>
<li>q2len = Length of q2</li>
<li>q1_n_words = Number of words in Question 1</li>
<li>q2_n_words = Number of words in Question 2</li>
<li>word_Common = (Number of common unique words in Question 1 and Question 2)</li>
<li>word_Total =(Total num of words in Question 1 + Total num of words in Question 2)</li>
<li>word_share = (word_common)/(word_Total) (kind of intersection/union ratio)</li>
<li>freq_q1+freq_q2 = sum total of frequency of qid1 and qid2</li>
<li>freq_q1-freq_q2 = absolute difference of frequency of qid1 and qid2</li>
<li>The average word share and Common no. of words of qid1 and qid2 is more when they are duplicate(Similar)</li>
<li>The distributions of the word_Common feature in similar and non-similar questions are highly overlapping</li>


<h3>PREPROCESSING OF TEXT</h3>
<li>remove html tags</li>
<li>remove punctuations</li>
<li>perform stemming</li>
<li>remove stopwords
<li>expand contractions (eg wasn't -> was not)


<h3>ADVANCED FEATURE EXTRACTION</h3>
<h5>Definitions</h5>
<li>Token: You get a token by splitting sentence a space
<li>Stop_Word : stop words as per NLTK.
<li>Word : A token that is not a stop_word
<h5>Features</h5>
<li>cwc_min : Ratio of common_word_count to min lenghth of word count of Q1 and Q2
<li>cwc_min = common_word_count / (min(len(q1_words), len(q2_words))
<li>cwc_max : Ratio of common_word_count to max lenghth of word count of Q1 and Q2
<li>cwc_max = common_word_count / (max(len(q1_words), len(q2_words))
<li>csc_min : Ratio of common_stop_count to min lenghth of stop count of Q1 and Q2
<li>csc_min = common_stop_count / (min(len(q1_stops), len(q2_stops))
<li>csc_max : Ratio of common_stop_count to max lenghth of stop count of Q1 and Q2
<li>csc_max = common_stop_count / (max(len(q1_stops), len(q2_stops))
<li>ctc_min : Ratio of common_token_count to min lenghth of token count of Q1 and Q2
<li>ctc_min = common_token_count / (min(len(q1_tokens), len(q2_tokens))
<li>ctc_max : Ratio of common_token_count to max lenghth of token count of Q1 and Q2
<li>ctc_max = common_token_count / (max(len(q1_tokens), len(q2_tokens))
<li>last_word_eq : Check if First word of both questions is equal or not
<li>last_word_eq = int(q1_tokens[-1] == q2_tokens[-1])
<li>first_word_eq : Check if First word of both questions is equal or not
<li>first_word_eq = int(q1_tokens[0] == q2_tokens[0])
<li>abs_len_diff : Abs. length difference
<li>abs_len_diff = abs(len(q1_tokens) - len(q2_tokens))
<li>mean_len : Average Token Length of both Questions
<li>mean_len = (len(q1_tokens) + len(q2_tokens))/2
<li>fuzz_ratio : http://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/
<li>fuzz_partial_ratio : http://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/
<li>token_sort_ratio : http://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/
<li>token_set_ratio : http://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/
<li>longest_substr_ratio : Ratio of length longest common substring to min length of token count of Q1 and Q2
<li>longest_substr_ratio = len(longest common substring) / (min(len(q1_tokens), len(q2_tokens))


<h3>ANALYSIS OF EXTRACTED FEATURES</h3>
<li>word cloud of duplicate question pairs is plotted
<li>word cloud of non duplicate question pairs is plotted
<li>a total of 15 NLP features are made now.


<h3>VISUALIZATION</h3>
<li>t-SNE and PCA are used to visualize the 15-d data in 3-d


<h3>VECTORIZATION</h3>
<li>Used TFIDF for vectorization and made a dictionary (key:word, value:tf-idf score)
<li>Used TFIDF word2vec by using GLOVE model instead of Google's Word2Vec model
<li>This is done separately for all question1's and then all the question2's
<li>Text vectors made have 384 dimensions (both question1 and question2 vectors)


<h3>FINAL DATAFRAME PREPARATION</h3>
  <h5>Finally these data frames are merged</h5>
<li>Dataframe on which simple preprocessing is done
<li>Dataframe which has the NLP features
<li>Dataframe which has the vectors for all question1's
<li>Dataframe which has the vectors for all question2's
<li>The final DataFrame has 794 features.



<h3>TRAIN TEST SPLIT</h3>
<li>Training data -> 70%
<li>Testing data -> 30%
  
  

<h3>MODELS</h3>
<li>A random model is built which gives a log loss of <b>0.89</b> which is the <b>worst case log loss</b>
<li>Logistic Regression model is used and the hyperparameter chosen for tuning is alpha 
     l2 regularization is used and calibrated classifier cross validation is used. <br>
     Confusion matrix is plotted <br>
  Best value of log loss is = <b>0.43</b>
<li>SVM classifier model is used and the hyperparameter chosen for tuning is alpha
     l1 regularization is used and calibrated classifier cross validation is used. <br>
     Confusion matrix is plotted <br>
  Best value of log loss is = <b>0.44</b>
<li>XGBoost model is used<br>
     Confusion matrix is plotted <br>
  Best value of log loss is = <b>0.36(without much hyperparameter tuning)</b> <br>
  XGBoost v1 log loss is = <b>0.33</b> 
<li>Decision Tree model is used by using RandomizedSearchCV on some parameters <br>
     Confusion matrix is plotted <br>
  Best value of log loss is = <b>0.41</b>
<li>Random Forest model is used by using RandomizedSearchCV on some parameters <br>
     Confusion matrix is plotted <br>
  Best value of log loss is = <b>0.43</b>

