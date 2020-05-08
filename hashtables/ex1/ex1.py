def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    if len(weights) < 2:
        return None
    use_limit = limit
    for item1 in weights:
        for item2 in weights:
            use_limit = item1 + item2
            cache[use_limit] = item1, item2

    answer_one = weights.index(cache[limit][0])
    weights[answer_one] = "A"
    answer_two = weights.index(cache[limit][1])
    

    if len(weights) < 3:
        return  answer_two, answer_one
    elif len(weights) > 3:
        return answer_one, answer_two