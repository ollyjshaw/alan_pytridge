from alan_pytridge.pint import Alan


def test_nothing_found_in_empty_list():
    words = []
    phrase = Alan().getPhrase(words)
    assert phrase == "Lynn, I've pierced my foot on a spike!!"


def test_nothing_found_in_list_with_no_partridge_words():
    words = ["foo", "bar", "baz"]
    phrase = Alan().getPhrase(words)
    assert phrase == "Lynn, I've pierced my foot on a spike!!"


def test_finds_a_single_partridge_words():
    words = ["foo", "Dan", "baz"]
    phrase = Alan().getPhrase(words)
    assert phrase == "Mine's a Pint!"


def test_finds_multiple_partridge_words():
    words = ["foo", "Dan", "Lynn", "baz"]
    phrase = Alan().getPhrase(words)
    assert phrase == "Mine's a Pint!!"


def test_finds_multiple_partridge_words2():
    words = ["Dan", "foo", "Dan", "Lynn", "baz"]
    phrase = Alan().getPhrase(words)
    assert phrase == "Mine's a Pint!!!"
