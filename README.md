# Information-Retrieval
ISNA News Search Engine is an information retrieval project implemented on the ISNA news collected in 2021. This project is implemented in 3 different sections:

Phase 1: Simple Indexing: Building the Inverted Index
Phase 2: Ranking docs based on tf-idf: Vector space and tf-idf ranked based retrieval
Phase 3: Categorizing docs into clusters (subjects)

## Simple Indexing
In this section the documents are indexed using an inverted index. First the tokens in each document in extracted and preprocessed using the preprocessing tool and then tokens are indexed using an inverted index. When the client enters a query, the engine searches in the index and retrieves the documents containing all the words in the query by applying an intersection on the results. If no document has all the tokens the documents containing all but one are retrieved and so on.

## Indexing using vector space and tf-idf
This is a more advanced search engine that leverages the cosine similarity and vector spaces for better retrieval. The vectors for each of the documents in the dataset are created using the tf-idf calculations. The formula in depicted bellow.
img
To reduce memory usage index elimination was applied. Moreover, for faster retrieval of the documents a champion list was used for each of the elemenets in the inverted index. The score of the relevance of each of the documents with a given query is calculated using the cosine similarity function.
img

## Machine learning applied in document retrieval
For this section, the dataset was expanded to include many more documents and in order to index and retrieve the new dataset in an efficient way some machine learning algorithms were applied.

### 1) K-Means Clustering
K-Means algorithm was applied to cluster the documents into smaller groups with a center representing the cluster. As a result, when a new query arrives its similarity is first calculated with only the centers of the clusters and then with the documents in the most similar cluster. The way we can imporve the time efficiecy of the search engine.

### 2) KNN Classification
Another way of searching for a specific document is with searching in the category. Cosequently, I used KNN to classify Documents with no label and then process the query based on these labels.