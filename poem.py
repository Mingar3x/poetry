import random as r

LINE_TEMPLATES = [
        "The {adj} {n} {v} {prep} the {adj2} {n2}",
        "{quant} {n} {v} {prep} the {n2}",
        "A {adj} {n} {v} like {n2}",
        "{quant} {n} is {adj}, yet {quant} is",
        "{adj} {n}, {adj2} {n2}, {v} and {v2}",
        "Tonight the {n} {v} {prep} moonlight"
        "Never is the {n} {adj}"
        "{bignum} {n}."
        "always {adj}, never {adj2}",
        "{v}.",
]
n = [
    "river", "pine", "dawn", "hill", "leaf", "cloud", "stone", "meadow", "ocean", 
    "street", "window", "lamp", "train", "tower", "alley", "coffee", "crowd"
    "heart", "hand", "letter", "memory", "promise", "kiss", "silence"
]
adj = [
    "quiet", "ancient", "soft", "golden", "lonely", "gentle", "wild", "clear",
    "neon", "restless", "narrow", "bright", "rusted", "endless", "warm",
    "tender", "faint", "true", "hidden", "soft", "aching"
]
v = [
    "whispers", "wanders", "sleeps", "breathes", "glows", "cradles", "rests", "rises",
    "hums", "hurries", "blinks", "sleeps", "echoes", "fades", "sparks", "lingers"
    "keeps", "holds", "remembers", "waits", "longs", "answers", "searches"
]
prep = [
    "within", "beside", "between", "inside",
    "under", "through", "behind", "around", "against",
    "beneath", "above", "beyond", "among"
]
bignum = r.randrange(1,8)*1000
quant = [
        "many", "each", "no", "a", "most", "every"
]
curr_n = []
curr_adj = []
topic_n = ""
topic_adj = ""
topic_v = ""