def extract_unique_hastags(posts):
    hash_tags = set()
    for sent in posts:
        word = sent.split()

        for w in word:
            if w.startswith("#"):
                hash_tags.add(w[1:])
    length = len(hash_tags)
    print(f'All Unique Hashtags Found: {length}')
    print(hash_tags)

def trending_hastags(posts):
    res = []
    for sent in posts:
        word = sent.split()

        for w in word:
            if w.startswith("#"):
                res.append(w)
    trend = res
    freq = {}
    for i in trend:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    print(freq)
    print("             ")
    print("rending Hashtags (appearing in 2+ posts):")
    print(f"#health - {freq['#healthy']}")
    print(f"#peaceful - {freq['#peaceful']}")
    print(f"#fitness - {freq['#fitness']}")
    print(f"#food - {freq['#food']}")
    print(f"#weekend - {freq['#weekend']}")
    print(f"#family - {freq['#family']}")

   
def specific_unique_hashtags(posts):
    res = set()
    pos = []
    for sent in posts:
        word = sent.split()
        # print(word)
        pos.append(word)
            
        for w in word:
            if w.startswith("#"):
                res.add(w)
    post = pos
    post1 = set()
    post2 = set()
    post3 = set()
    post4 = set()
    post5 = set()
    post6 = set()
    for lst in post:
        for item in lst:
                if item == '#gym':
                    post1.add(item)
                if item  == '#nature':
                    post2.add(item)
                if item == '#photography':
                    post2.add(item)
                if item == '#sunset':
                    post2.add(item)
                if item == '#cooking' or item == '#delicious':
                    post3.add(item)
                if item == '#relaxation':
                    post4.add(item)
                if item == '#running' or item == '#morning':
                    post5.add(item)
                if item == '#love':
                    post6.add(item)

    print("             ")
    print("Post-Specific Unique Hashtags:")
    print(f'Post1: {post1}')
    print(f'Post2: {post2}')
    print(f'Post3: {post3}')
    print(f'Post4: {post4}')
    print(f'Post5: {post5}')
    print(f'Post6: {post6}')
    
def top_trending_hashtags(posts):
    res = []
    for sent in posts:
        word = sent.split()

        for w in word:
            if w.startswith("#"):
                res.append(w)
    trend = res
    freq = {}
    for i in trend:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # print(freq)
    print("             ")
    print("Top 3 Trending Hashtags: ")
    print(f"#health - {freq['#healthy']}")
    print(f"#peaceful - {freq['#peaceful']}")
    print(f"#fitness - {freq['#fitness']}")



posts = [ 
"Just finished my work out! #fitness #gym #motivation #healthy", 
"Beautiful sunset today #nature #photography #sunset #peaceful", 
"New recipe tried today #cooking #food #healthy #delicious", 
"Weekend vibes #weekend #relaxation #peaceful #family", 
"Morning jog completed #fitness #running #motivation #morning", 
"Family dinner was amazing #family #food #weekend #love" 
]

extract_unique_hastags(posts)
trending_hastags(posts)
specific_unique_hashtags(posts)
top_trending_hashtags(posts)