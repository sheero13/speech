#spacy

# import spacy

# nlp = spacy.load("en_core_web_sm")
# print("NER tester started. Type 'exit' to stop.\n")

# while True:
#     text = input("Enter Text: ")

#     if text.lower() == "exit":
#         print("Exiting...")
#         break

#     doc = nlp(text)

#     print("\nEntities found:")
#     if doc.ents:
#         for ent in doc.ents:
#             print(ent.text, ent.label_)
#     else:
#         print("No entities found.")

#     print("-" * 40)

#-----------------------------------------------------------------------

#train

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# import pandas as pd
# import numpy as np
# import pickle
# import ast
# import tensorflow as tf

# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.layers import Input, Embedding, LSTM, Bidirectional, Dense, TimeDistributed
# from tensorflow.keras.models import Model

# df = pd.read_csv(r"NER\ner.csv", encoding="latin1")
# df.columns = df.columns.str.strip()

# sentences = []
# tags_list = []

# for _, row in df.iterrows():
#     words = row["Sentence"].split()
#     tags = ast.literal_eval(row["Tag"])
#     if len(words) == len(tags):
#         sentences.append(words)
#         tags_list.append(tags)

# print("Total sentences:", len(sentences))

# sentences = sentences[:5000]
# tags_list = tags_list[:5000]

# all_words = set(w for s in sentences for w in s)
# all_tags = set(t for s in tags_list for t in s)

# word2idx = {w: i + 2 for i, w in enumerate(all_words)}
# word2idx["PAD"] = 0
# word2idx["UNK"] = 1

# tag2idx = {t: i for i, t in enumerate(all_tags)}

# max_len = 20  

# X = [[word2idx.get(w, 1) for w in s] for s in sentences]
# y = [[tag2idx[t] for t in s] for s in tags_list]

# X = pad_sequences(X, maxlen=max_len, padding="post", value=0)
# y = pad_sequences(y, maxlen=max_len, padding="post", value=tag2idx["O"])

# X = np.array(X, dtype=np.int16)
# y = np.array(y, dtype=np.int16)

# print("Data prepared.")

# input_layer = Input(shape=(max_len,))

# embedding = Embedding(
#     input_dim=len(word2idx),
#     output_dim=32 
# )(input_layer)

# bilstm = Bidirectional(
#     LSTM(32, return_sequences=True)
# )(embedding)

# output = TimeDistributed(
#     Dense(len(tag2idx), activation="softmax")
# )(bilstm)

# model = Model(input_layer, output)

# model.compile(
#     optimizer="adam",
#     loss="sparse_categorical_crossentropy",
#     metrics=["accuracy"]
# )

# model.summary()

# dataset = tf.data.Dataset.from_tensor_slices((X, y))
# dataset = dataset.shuffle(1000).batch(4)

# print("Training...")

# model.fit(dataset, epochs=5)

# model.save("ner_bilstm_model.h5")

# with open("word2idx.pkl", "wb") as f:
#     pickle.dump(word2idx, f)

# with open("tag2idx.pkl", "wb") as f:
#     pickle.dump(tag2idx, f)

# print("Training completed")

#------------------------------------------------------------------------------------------------------------------

#test

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# import numpy as np
# import pickle
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.sequence import pad_sequences


# print("Loading model...")

# model = load_model(r"NER\ner_bilstm_model.h5")

# with open(r"NER\word2idx.pkl", "rb") as f:
#     word2idx = pickle.load(f)

# with open(r"NER\tag2idx.pkl", "rb") as f:
#     tag2idx = pickle.load(f)

# idx2tag = {v: k for k, v in tag2idx.items()}

# max_len = 20   

# print("Model loaded successfully!\n")

# def predict_sentence(sentence):
#     words = sentence.split()


#     seq = [word2idx.get(w, 1) for w in words]  # 1 = UNK

#     padded = pad_sequences([seq], maxlen=max_len, padding="post", value=0)

#     preds = model.predict(padded, verbose=0)
#     pred_tags = np.argmax(preds[0], axis=-1)

#     print("\nPrediction:\n")
#     for word, tag_idx in zip(words, pred_tags[:len(words)]):
#         print(f"{word:15} --> {idx2tag[tag_idx]}")
# while True:
#     sentence = input("\nEnter sentence (or type 'exit'): ")
#     if sentence.lower() == "exit":
#         break

#     predict_sentence(sentence)
