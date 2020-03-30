#This is the program for Text Summarization in python.
#'py' file is not supported for upload, so I upload it in 'doc' format.
#kindly,change it to 'py' or 'ipynb' format.
text='As the world entered the era of big data, the need for its storage also grew. It was the main challenge and concern for the enterprise industries until 2010. The main focus was on building framework and solutions to store data. Now when Hadoop and other frameworks have successfully solved the problem of storage, the focus has shifted to the processing of this data. Data Science is the secret sauce here. All the ideas which you see in Hollywood sci-fi movies can actually turn into reality by Data Science. Data Science is the future of Artificial Intelligence. Therefore, it is very important to understand what is Data Science and how can it add value to your business.Traditionally, the data that we had was mostly structured and small in size, which could be analyzed by using the simple BI tools. Unlike data in the traditional systems which was mostly structured, today most of the data is unstructured or semi-structured. Let’s have a look at the data trends in the image given below which shows that by 2020, more than 80 % of the data will be unstructured.'
print(text)
from gensim.summarization import summarize
print(summarize(text,word_count=25))
