from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# two sentences to compare
s1 = "I love programming in Python"
s2 = "Python coding is fun"

# one different sentence to compare
s3 = "The weather is nice today"


em1 = model.encode(s1)
em3 = model.encode(s3)
em2 = model.encode(s2)


print("Similarity between s1 and s2:", util.cos_sim(em1, em2))
print("Similarity between s1 and s3:", util.cos_sim(em1, em3))