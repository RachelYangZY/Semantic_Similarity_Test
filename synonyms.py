def cosine_similarity(vec1, vec2):
    # This function returns the cosine similarity between the sparse vectors vec1 and vec2, stored as dictionaries.
    dot_product = 0
    vec1_sum_squares = 0
    vec2_sum_squares = 0
    for key in vec1:
        if key in vec2:
            dot_product += vec1[key] * vec2[key]
        vec1_sum_squares += vec1[key] ** 2
    for key in vec2:
        vec2_sum_squares += vec2[key] ** 2
    sim = dot_product / ((vec1_sum_squares * vec2_sum_squares) ** 0.5)
    return sim

def build_semantic_descriptors(sentences):
    # This function takes in a list sentences which contains lists of strings (words) representing sentences, and
    # returns a dictionary d such that for every word w that appears in at least one of the sentences, d[w] is itself a dictionary which represents the semantic descriptor of w (note: the variable names here are arbitrary).

    d = {}
    for sentence in sentences:
        for word in sentence:
            if word not in d:
                d[word] = {}
            for i in range(len(sentence)):
                if sentence.index(sentence[i]) == i: # ensures that words in a sentence arent repeated
                    if sentence[i] in d[word]:
                        d[word][sentence[i]] += 1
                    elif sentence[i] != word:
                        d[word][sentence[i]] = 1
    return d


# test
# NFTU_opening = [["i", "am", "a", "sick", "man"], ["i", "am", "a", "spiteful", "man"], ["i", "am", "an", "unattractive", "man"], ["i", "believe", "my", "liver", "is", "diseased"], ["however", "i", "know", "nothing", "at", "all", "about", "my", "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
# d = build_semantic_descriptors(NFTU_opening)

# { "man": {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}, "liver": {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}, ... }

def build_semantic_descriptors_from_files(filenames):
    #account for double punctuations, such as !!?
    f = ""
    for i in range(len(filenames)):
        f = f + open(filenames[i], "r", encoding="latin1").read()
    f = f.replace("!", ".").replace("?", ".")
    f = f.replace(",", " ").replace("-", " ").replace("--", " ").replace(":", " ").replace(";", " ")
    # replace("\n", "").replace("\"", " ").replace("'", " "). replace("(", " ").replace(")", " ").replace("*", " ").replace("/", " ").replace("=", " ")
    f = f.lower()
    f = f.split(".")
    for i in range(len(f)):
        f[i] = f[i].split()
    return build_semantic_descriptors(f)



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    # What if word not in semantic_descriptors?
    # What if the choice/word doesn't have any semantic descriptors?
    highest_sim = -1
    best_choice = choices[0]
    for choice in choices:
        if (choice not in semantic_descriptors) or (word not in semantic_descriptors):
            sim = -1
        else:
            sim = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])
        if sim > highest_sim:  # > rather than >= to get the lowest index if tied
            highest_sim = sim
            best_choice = choice
    return best_choice



def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    test = open(filename, "r", encoding="latin1").read()
    test = test.lower()
    test = test.split("\n")

    correct = 0

    for i in range(len(test)):
        test[i] = test[i].split(" ")
        best_choice = most_similar_word(test[i][0], test[i][2:], semantic_descriptors, similarity_fn)
        if best_choice == test[i][1]:
            correct += 1

    percentage = correct/(len(test)) * 100
    return percentage

#test
# sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
# res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
# print(res, "of the guesses were correct")







f = 'I, Robot: the best novel by Asimov; the worst; or neither?'
f = f.replace("!", ".").replace("?", ".")
f = f.replace(",", " ").replace("-", " ").replace("--", " ").replace(":", " ").replace(";", " ")
# replace("\n", "").replace("\"", " ").replace("'", " "). replace("(", " ").replace(")", " ").replace("*", " ").replace("/", " ").replace("=", " ")
f = f.lower()
f = f.split(".")
for i in range(len(f)):
    f[i] = f[i].split()
g = build_semantic_descriptors(f)












